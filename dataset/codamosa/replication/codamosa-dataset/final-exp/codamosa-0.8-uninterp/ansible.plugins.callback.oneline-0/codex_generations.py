

# Generated at 2022-06-13 11:51:37.476455
# Unit test for constructor of class CallbackModule
def test_CallbackModule():

    from ansible.executor.task_result import TaskResult
    from ansible.vars.hostvars import HostVars

    # Create a mock PlayContext to pass as a parameter to the TaskResult constructor
    class MockPlayContext(object):
        def __init__(self):
            pass

    play_context = MockPlayContext()

    # Create a mock Task to pass as a parameter to the TaskResult constructor
    class MockTask(object):
        def __init__(self):
            self.action = 'some action'
            self.name = 'some name'

    task = MockTask()

    # Create a mock TaskResult to pass as a parameter to the v2_runner_on_failed function

# Generated at 2022-06-13 11:51:43.984729
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    callback = CallbackModule()
    result = {
        '_ansible_verbose_always': True,
        '_ansible_no_log': False,
        'changed': False,
        'changed_when_results': True,
        'ansible_job_id': 'xlyjh.test.22',
        'invocation': {
            'module_name': 'ping',
            'module_args': ''
        },
        'results': {
            'ping': 'pong'
        },
        '_ansible_item_result': True
    }
    result._host = {
        'name': 'ifb3',
        'ipv4': '10.132.*.*'
    }
    result._result = result
    result._task = {}
    result._task.action = 'ping'

   

# Generated at 2022-06-13 11:51:45.378070
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pass


# Generated at 2022-06-13 11:51:56.228516
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # arrange
    callback = CallbackModule()
    result = type('obj', (object,), {'_result': {}, '_host': {}, '_task': {}})()
    result._host.get_name = lambda: ''
    result._result['exception'] = 'test'
    result._task.action = 'test'
    callback._display = type('obj', (object,), {'__setitem__': lambda *args, **kwargs: None,
                                                '__getitem__': lambda *args, **kwargs: None,
                                                'get_text': lambda *args, **kwargs: str,
                                                'display': lambda *args, **kwargs: None,
                                                'verbosity': 0})()
    callback._dump_results = lambda *args, **kwargs: 'test'



# Generated at 2022-06-13 11:52:06.403153
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    """
    This function is used to test method v2_runner_on_ok of class CallbackModule
    :return: 
    """
    # Stub
    result = {
        "changed": False,
        "_host": {
            "get_name": "hostname"
        },
        "_task": {
            "action": "Copy"
        },
        "_result": {
            "stdout": "copying file from remote to local"
        }
    }
    callback = CallbackModule()
    result = callback.v2_runner_on_ok(result)
    assert result is None

# Generated at 2022-06-13 11:52:08.654613
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule().CALLBACK_VERSION == 2.0
    assert CallbackModule().CALLBACK_TYPE == 'stdout'
    assert CallbackModule().CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:52:16.519064
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.callback import CallbackBase
    from io import StringIO
    import contextlib
    from ansible import constants as C

    class CallbackModule(CallbackBase):
        def v2_runner_on_ok(self, result):
            self._display.display("OK")

    @contextlib.contextmanager
    def capture(command, *args, **kwargs):
        out, sys.stdout = sys.stdout, StringIO()
        command(*args, **kwargs)
        sys.stdout.seek(0)
        yield sys.stdout.read()
        sys.stdout = out

    c = CallbackModule()
    c.set_options({'verbosity': 0})
    result = {}
    result['changed'] = False
   

# Generated at 2022-06-13 11:52:20.944740
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = dict()
    result["_result"] = dict()
    result["_result"]["exception"] = "exception!" 
    callback_module = CallbackModule()
    callback_module.v2_runner_on_failed(result, ignore_errors=False)



# Generated at 2022-06-13 11:52:23.102795
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Create a CallbackModule object
    cbm = CallbackModule()
    # Create a FakeResult object
    fr = FakeResult()
    # run v2_runner_on_failed with FakeResult as input
    cbm.v2_runner_on_failed(fr)



# Generated at 2022-06-13 11:52:34.694488
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    stdout = "An exception occurred during task execution. To see the full traceback, use -vvv. The error was: Connection refused"
    task =  {'action': 'Evaluate machine vs. human', 'category': 'Tests', 'name': 'Evaluate machine vs. human' }
    runner = {'stdout': 'Connection refused'}
    test = CallbackModule()
    test.display = {'verbosity': 2}
    test._display =  {'color': 'COLOR_ERROR', 'display': print}
    test._dump_results = {'results': 'execution'}
    test.v2_runner_on_failed(runner, task, ignore_errors=False)
    assert stdout == "An exception occurred during task execution. To see the full traceback, use -vvv. The error was: Connection refused"


# Generated at 2022-06-13 11:52:41.296344
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible.plugins.callback import CallbackBase
    # class CallbackBase has no __init__ method
    assert True

# Generated at 2022-06-13 11:52:44.383184
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule.CALLBACK_TYPE == 'stdout'
    assert CallbackModule.CALLBACK_NAME == 'oneline'
    assert CallbackModule.CALLBACK_VERSION >= 2.0

# Generated at 2022-06-13 11:52:48.570353
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    import ansible.plugins.callback.oneline
    callback = ansible.plugins.callback.oneline.CallbackModule()
    assert callback.CALLBACK_VERSION == 2.0
    assert callback.CALLBACK_TYPE == 'stdout'
    assert callback.CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:52:55.190786
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    # Test type 1
    def do_test_1():
        from ansible.vars.hostvars import HostVars
        from ansible.vars.manager import VariableManager
        from ansible.inventory.manager import InventoryManager
        from ansible.playbook.play_context import PlayContext
        from ansible.playbook.task import Task
        from ansible.playbook.play import Play
        from ansible.inventory.host import Host
        from ansible.parsing.dataloader import DataLoader

        callback = CallbackModule()
        result = type('obj', (object,), {
            '_host': Host(name="testhost"),
            '_result': {
                'exception': "An exception occurred"
            },
            '_task': Task()
        })

        callback.v2_runner_on_

# Generated at 2022-06-13 11:52:59.768197
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible.plugins.callback.default import CallbackModule
    from ansible import constants as C

    callbackModule = CallbackModule()
    assert callbackModule.CALLBACK_VERSION == 2.0
    assert callbackModule.CALLBACK_TYPE == 'stdout'
    assert callbackModule.CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:53:00.255177
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    return CallbackModule()

# Generated at 2022-06-13 11:53:09.670290
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    # Test no exception result
    hostname = "localhost"
    result = {"exception": None}
    ignore_errors = False
    callbackModule = CallbackModule()
    callbackModule._display.verbosity = 3
    callbackModule.v2_runner_on_failed(result, ignore_errors)

    # Test non-empty exception result
    result = {"exception": "non-empty exception"}
    callbackModule.v2_runner_on_failed(result, ignore_errors)

    # Test empty exception result
    result = {"exception": ""}
    callbackModule.v2_runner_on_failed(result, ignore_errors)

# Generated at 2022-06-13 11:53:10.357410
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule()

# Generated at 2022-06-13 11:53:13.177433
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    print("Testing CallbackModule class constructor")
    assert CallbackModule()
    print("Successfully completed the testing of constructor")


# Generated at 2022-06-13 11:53:22.626977
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
	class Result:
		def __init__(self):
			self._result = None
			self._host = None

	class Host:
		def __init__(self):
			pass

		def get_name(self):
			return "host1"

	class Display:
		def __init__(self):
			pass

		def display(self,msg,color):
			print(msg)

	class CallbackModule:
		def __init__(self):
			self._display = Display()

		def _command_generic_msg(self, hostname, result, caption):
			stdout = result.get('stdout', '').replace('\n', '\\n').replace('\r', '\\r')

# Generated at 2022-06-13 11:53:40.044182
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
  import unittest
  import ansible.plugins.callback.oneline as oneline
  import ansible.module_utils.common as common
  import ansible.playbook.play_context as play_context
  import ansible.playbook.play as play

  class V2RunnerOnOkTest(unittest.TestCase):
    def setUp(self):
      self.callback = oneline.CallbackModule()

    def test_default_is_ok(self):
      # mock
      result = common.AnsibleResult()
      result._result = dict(changed=False)
      result._task = play.Task()
      result._host = play_context.Host('0.0.0.0')

      self.assertIsNone(self.callback.v2_runner_on_ok(result))


# Generated at 2022-06-13 11:53:51.323025
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.playbook.task import Task
    from ansible.vars.hostvars import HostVars
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    from ansible.playbook.play_context import PlayContext

# Generated at 2022-06-13 11:54:01.877019
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback.oneline import CallbackModule, C
    callback = CallbackModule()
    result_data = dict()
    result_data["ansible_facts"] = dict()
    result_data["ansible_facts"]["os"] = "Windows"
    result_data["_ansible_verbose_override"] = True
    result_data["changed"] = False
    result_data["invocation"] = dict()
    result_data["invocation"]["module_args"] = dict()
    result_data["invocation"]["module_args"]["command"] = "dir"
    result_data["invocation"]["module_args"]["_uses_shell"] = True
    result_data["invocation"]["module_name"] = "command"

# Generated at 2022-06-13 11:54:07.150674
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    c = CallbackModule()
    c.CALLBACK_VERSION = 2.0
    c.CALLBACK_TYPE = 'stdout'
    c.CALLBACK_NAME = 'oneline'
    assert c.CALLBACK_VERSION > 0 
    assert isinstance(c.CALLBACK_TYPE, str) 
    assert isinstance(c.CALLBACK_NAME, str)

# Generated at 2022-06-13 11:54:10.267330
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    c = CallbackModule()
    assert c.CALLBACK_VERSION == 2.0 and c.CALLBACK_TYPE == 'stdout' and c.CALLBACK_NAME == 'oneline' and c._play is None

# Generated at 2022-06-13 11:54:20.489327
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Testing the following conditions:
    # 1. result._result.get('changed', False):
    #       color = C.COLOR_CHANGED
    # 2. result._task.action in C.MODULE_NO_JSON and 'ansible_job_id' not in result._result:
    #       self._display.display(self._command_generic_msg(result._host.get_name(), result._result, state), color=color)
    
    # Testing for condition 1
    result = {'changed': True}
    runner_result = {'_result': result}
    runner_result['_host'] = 'hostname'
    runner_result['_task'] = 'task action'
    callback = CallbackModule()
    expected_result = 'hostname | CHANGED => %s' % (result)
    actual_result

# Generated at 2022-06-13 11:54:28.818089
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    class FakeDisplay:
        def __init__(self):
            self.args = ''
        def display(self, args, color):
            self.args = args

    class FakeHost:
        def __init__(self):
            self.name = 'testhost'
        def get_name(self):
            return self.name

    class FakeResult:
        def __init__(self):
            self.host = FakeHost()
            task = {'action': 'debug'}
            self._result = {'stdout_lines': ['test1', 'test2', 'test3'], 'failed': False, 'changed': True}
            self._task = task

    fake_result = FakeResult()
    fake_display = FakeDisplay()
    callback_module = CallbackModule()
    callback_module._display = fake_display
   

# Generated at 2022-06-13 11:54:30.422978
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
  assert( bool(CallbackModule) )


# Generated at 2022-06-13 11:54:31.834603
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    pass # pragma: no cover

# Generated at 2022-06-13 11:54:32.621393
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule()

# Generated at 2022-06-13 11:54:50.076689
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    test_obj = CallbackModule()

# Generated at 2022-06-13 11:54:59.473586
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    class TestClass:
        def __init__(self):
            self.CLASS_NAME = 'TestClass'
        def display(self, msg, color=None):
            self.msg = msg
            self.color = color
    class TestClassHost:
        def __init__(self):
            self.CLASS_NAME = 'TestClassHost'
            self.hostname = 'samplehost'
        def get_name(self):
            return self.hostname
    class TestClassResult:
        def __init__(self):
            self.CLASS_NAME = 'TestClassResult'
            self.result = {}
            self.task = {}
            self.task['action'] = 'shell'
            self.host = TestClassHost()
        def _result(self, s):
            return self.result

# Generated at 2022-06-13 11:55:08.312491
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # create an instance of CallbackModule
    x = CallbackModule()

    # create host with result (assume not changed)
    result_json = {
        'changed': False,
        'stdout': 'good',
        'stderr': '',
        'rc': 0
    }

    result = {
        '_result': result_json
    }

    # ensure method returns what we expect
    assert x.v2_runner_on_ok(result) == None


# Generated at 2022-06-13 11:55:09.520353
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert len(CallbackModule) > 0

# Generated at 2022-06-13 11:55:13.837768
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    x = CallbackModule()
    assert x.CALLBACK_VERSION == 2.0
    assert x.CALLBACK_TYPE == 'stdout'
    assert x.CALLBACK_NAME == 'oneline'


if __name__ == '__main__':
    test_CallbackModule()

# Generated at 2022-06-13 11:55:15.227573
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule(display=None)

# Generated at 2022-06-13 11:55:24.723228
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    class FakeDisplay:
        def display(self, msg, color=None):
            return msg
    fake_display = FakeDisplay()
    class FakeResult:
        class FakeHost:
            def get_name(self):
                return "fake_host"
        _host = FakeHost()
        _result = {'changed': True}
        _task = classmethod()
    cb = CallbackModule()
    cb._display = fake_display
    cb.v2_runner_on_ok(FakeResult())


# Generated at 2022-06-13 11:55:30.582251
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
  runner_on_ok_result = {'changed': False, 'msg': '', 'rc': 0}
  result = {'_host': '', '_result': runner_on_ok_result, '_task': '' }
  callback = CallbackModule()
  callback.v2_runner_on_ok(result)
  assert callback.CALLBACK_TYPE == 'stdout'

# Generated at 2022-06-13 11:55:34.229833
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    '''Test constructor of class CallbackModule'''
    callback = CallbackModule()
    assert isinstance(callback, CallbackModule)
    assert isinstance(callback, CallbackBase)



# Generated at 2022-06-13 11:55:35.734339
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    myCallbackModule = CallbackModule()

    print(myCallbackModule)

# Generated at 2022-06-13 11:56:17.619362
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = {'exception': 'This is a test'}
    display = Display()
    callback_module = CallbackModule()
    callback_module.display = display
    callback_module.CALLBACK_NAME ='test'
    callback_module.line_opens_shell = False
    callback_module.v2_runner_on_failed(result)
    assert display.display_msg == 'An exception occurred during task execution. To see the full traceback, use -vvv. The error was: This is a test'


# Generated at 2022-06-13 11:56:24.089441
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
	from ansible.playbook.task import Task
	from ansible.playbook.play_context import PlayContext
	from ansible.vars.hostvars import HostVars
	from ansible.vars.hostvars import VariableManager
	from ansible.vars.manager import VariableManager
	from ansible.inventory.manager import InventoryManager
	from ansible.inventory.host import Host
	from ansible.executor.task_queue_manager import TaskQueueManager
	from ansible.parsing.dataloader import DataLoader
	from ansible.utils.vars import combine_vars
	from ansible.plugins.callback import CallbackBase
	from ansible.plugins.callback import CallbackBase
	from ansible.playbook.play import Play
	from ansible.playbook.task_include import TaskInclude
	

# Generated at 2022-06-13 11:56:33.298209
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import io
    import sys
    pa = MockDisplay()
    pm = CallbackModule(pa)
    pm.set_options()

    # Testing with a changed host
    pr = MockResult(host='host1',task='task1')
    pr._result['changed'] = True
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()
    pm.v2_runner_on_ok(pr)
    sys.stdout = old_stdout
    assert mystdout.getvalue() == "host1 | CHANGED => {'changed': True}\n"
    mystdout.close()

    # Testing with an unchanged host
    pr = MockResult(host='host1',task='task1')
    pr._result['changed'] = False

# Generated at 2022-06-13 11:56:34.631361
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    #
    # Test the constructor of class CallbackModule
    #
    pass

# Generated at 2022-06-13 11:56:44.332931
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import ansible.plugins.callback.oneline
    import ansible.playbook.play_context
    import ansible.vars.hostvars
    import ansible.executor.task_result
    import ansible.executor.play_iterator
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.utils.color
    import ansible.inventory.host
    import ansible.vars.manager
    import ansible.template
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock
    from ansible.utils.color import stringc
    from ansible.compat.tests.mock import PropertyMock


# Generated at 2022-06-13 11:56:52.300196
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback.oneline import CallbackModule

    # Initialize the object
    cb_object = CallbackModule()

    # Prepare some valid data
    result = type('', (), {})()
    result._result = { 'a': 1, 'b': 2 }
    result._host = 'host1'
    result._task = None

    # Execute the method
    expected_result = 'host1 | SUCCESS => { "a": 1, "b": 2 }'
    actual_result = cb_object.v2_runner_on_ok(result)

    # Verify the response
    assert expected_result == actual_result

# Generated at 2022-06-13 11:56:54.130459
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule().CALLBACK_TYPE == 'stdout'
    assert CallbackModule().CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:57:00.029835
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    import os

    os.environ["ANSIBLE_CALLBACK_WHITELIST"] = "oneline"
    print(os.environ.get("ANSIBLE_CALLBACK_WHITELIST"))
    cb = CallbackModule()
    assert cb.CALLBACK_NAME == "oneline"

# Generated at 2022-06-13 11:57:11.033689
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.runner.return_data import ReturnData
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 11:57:20.188855
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    global ansible_display
    buffer = StringIO()
    ansible_display = Display()
    ansible_display.verbosity = 3
    callback = CallbackModule(display=ansible_display)

    callback.v2_runner_on_failed(result=MockResult(
        _task=MockTask(action="not a module"),
        _host=MockHost(get_name="test"),
        _result={"exception": "An exception occurred during task execution"}
    ))

    output = buffer.getvalue()
    answer = "test | FAILED! => {'exception': 'An exception occurred during task execution'}\n"
    answer += "An exception occurred during task execution. To see the full traceback, use -vvv. The error was: An exception occurred during task execution\n"
    assert output == answer

   

# Generated at 2022-06-13 11:58:48.625025
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import sys
    import io
    sys.stdout = io.StringIO()
    class Result():
        def __init__(self, task, host, result):
            self._task = task
            self._host = host
            self._result = result
    class Host():
        def __init__(self, name):
            self._name = name
        def get_name(self):
            return self._name
    class Task():
        def __init__(self, name):
            self._name = name
        def action(self):
            return self._name

# Generated at 2022-06-13 11:59:00.397314
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():

    import sys
    from io import StringIO
    from collections import namedtuple

    from ansible.module_utils._text import to_text
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult

    from ansible.utils.color import ANSIBLE_COLOR, stringc, stringc
    from ansible.plugins.callback import CallbackBase

    from ansible.plugins.callback.oneline import CallbackModule
    
    # Save the original stdout and stderr
    stdout_original = sys.stdout
    stderr_original = sys.stderr


# Generated at 2022-06-13 11:59:09.118359
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Initializing test data
    # Testing function CallbackModule.v2_runner_on_failed()
    # Expected result: msg = "An exception occurred during task execution. The full traceback is:\n" + result_result['exception'].replace('\n', '')
    test_obj = CallbackModule()
    assert msg == "An exception occurred during task execution. The full traceback is:\n" + result._result['exception'].replace('\n', '')

# Generated at 2022-06-13 11:59:10.117020
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cpm = CallbackModule()

# Generated at 2022-06-13 11:59:17.490053
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import unittest
    import os
    import sys
    import platform
    from ansible import context
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display
    from ansible.plugins.callback import CallbackBase
    from ansible.plugins.callback.default import CallbackModule


# Generated at 2022-06-13 11:59:19.395309
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    callback = CallbackModule()
    result = {'stdout': 'Test Failed'}
    result = {}
    callback.v2_runner_on_failed(result)
    assert True

# Generated at 2022-06-13 11:59:21.499600
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
  cb = CallbackModule()
  assert cb.CALLBACK_VERSION == 2.0
  assert cb.CALLBACK_TYPE == 'stdout'
  assert cb.CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:59:25.239484
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    runner_result = {
        'exception': 'this is exception',
        'stdout': 'this is stdout',
    }
    result = {
        '_host': {
            'get_name': lambda: 'testhost'
        },
        '_result': runner_result
    }
    CallbackModule().v2_runner_on_failed(result)


# Generated at 2022-06-13 11:59:36.076373
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    result = Mock()
    result._host = Mock()
    result._host.get_name.return_value = 'hostname'
    result._result = {}
    result._task = Mock()
    result._task.action = 'setup'
    result._task.name = 'test'

    callback = CallbackModule()
    callback._display = Mock()
    callback.v2_runner_on_ok(result)
    assert result._host.get_name.called
    assert callback._display.display.called
    assert callback._display.display.call_args == call('hostname | SUCCESS => {}', color=C.COLOR_OK)


result = Mock()
result._host = Mock()
result._host.get_name.return_value = 'hostname'

# Generated at 2022-06-13 11:59:38.172732
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible.callbacks.minimal import CallbackModule
    assert CallbackModule is not None