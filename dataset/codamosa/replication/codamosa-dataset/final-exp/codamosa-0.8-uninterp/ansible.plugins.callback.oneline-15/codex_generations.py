

# Generated at 2022-06-13 11:51:30.077659
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    print(CallbackModule())

# Generated at 2022-06-13 11:51:35.396937
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    print("Test case 1 - Bad Input:")
    input_data = dict()
    # test case 1
    expected_result = "An exception occurred during task execution. To see the full traceback, use -vvv. The error was: "
    actual_result = CallbackModule._command_generic_msg(input_data)
    assert expected_result == actual_result



# Generated at 2022-06-13 11:51:43.238165
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    stdout_stream = BytesIO()
    failed_result = dict(
        _host=dict(
            get_name=lambda: 'hostname',
        ),
        _result=dict(
            exception='An exception',
            msg='An error message',
        ),
    )
    callback = CallbackModule(display=DisplayManager(stdout_stream))
    callback.v2_runner_on_failed(failed_result)
    assert stdout_stream.getvalue().decode() == 'hostname | FAILED! => {\n    "msg": "An error message", \n    "exception": "An exception"\n}\n'


# Generated at 2022-06-13 11:51:47.092351
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    callback_module_instance = CallbackModule()
    assert callback_module_instance.CALLBACK_TYPE is 'stdout'
    assert callback_module_instance.CALLBACK_NAME is 'oneline'
    assert callback_module_instance.CALLBACK_VERSION is 2.0

# Generated at 2022-06-13 11:51:53.175765
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback.oneline import CallbackModule
    callback = CallbackModule()
    from ansible.executor.task_result import TaskResult
    import json
    import ansible.constants as C
    result = TaskResult(host=None, task=None, return_data=json.loads('{"changed": false, "failed": false}'))
    callback.v2_runner_on_ok(result)

# Generated at 2022-06-13 11:51:54.208655
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    pass
#    assert CallbackModule() is not None

# Generated at 2022-06-13 11:51:57.327538
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    module = CallbackModule()
    assert module.CALLBACK_VERSION == 2.0
    assert module.CALLBACK_TYPE == 'stdout'
    assert module.CALLBACK_NAME == 'oneline'


# Generated at 2022-06-13 11:52:05.326039
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    """
    This is the unit test for the constructor of the class CallbackModule
    It will pass in a fake ansible.plugins.callback.CallbackBase object and
    see if the _display is set to the input object _display

    Return:
    True if the test pass
    """
    fake_callback = CallbackBase()
    test_class = CallbackModule(display=fake_callback)
    if test_class._display == fake_callback:
        return True
    else:
        return False

# Generated at 2022-06-13 11:52:13.546684
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible import constants as C
    from ansible.module_utils.six import StringIO
    from ansible.plugins.callback.oneline import CallbackModule
    from ansible.utils.color import stringc

    # Create a mock class of the CallbackModule class with stubs implemented for the methods needed to pass the test
    class_name = 'CallbackModule'
    method_name = 'v2_runner_on_failed'

    class MockCallbackModule(CallbackModule):
        _dump_results_called = False
        _dump_results_called_with = None

        def __init__(self, *args, **kwargs):
            super(MockCallbackModule, self).__init__(*args, **kwargs)

        def _dump_results(self, result, indent=None):
            MockCallbackModule._dump_results_called = True

# Generated at 2022-06-13 11:52:16.783751
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    print(run.apply_async(v2_runner_on_ok, (result,), callback=v2_runner_on_ok.s()).get())

# Generated at 2022-06-13 11:52:29.267694
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # host name as a success
    result_with_host_name = {
        'exception': 'Exception',
        'module_stdout': 'Module Stdout',
        'module_stderr': 'Module Stderr',
        'msg': 'Message',
        'rc': '1',
    }
    module = CallbackModule()
    result = module.v2_runner_on_failed(result_with_host_name, ignore_errors=False)
    assert result == 'test | An exception occurred during task execution. To see the full traceback, use -vvv. The error was: Exception'


# Generated at 2022-06-13 11:52:43.725036
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.errors import AnsibleError
    from ansible.playbook.task import Task
    from ansible.plugins.callback import CallbackBase
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.constants import DEFAULT_HOST_LIST

    class CallbackModule(CallbackBase):
        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'oneline'


# Generated at 2022-06-13 11:52:46.833608
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    c = CallbackModule()
    assert c.CALLBACK_VERSION == 2.0
    assert c.CALLBACK_TYPE == 'stdout'
    assert c.CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:52:53.382000
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible_collections.jctanner.oo_ansible_plugin.plugins.callback.oneline import CallbackModule
    import json
    import sys
    CM = CallbackModule()
    result = MockResult()
    result._result = {'exception': 'An exception occurred during task execution. The full traceback is:\nset_fact: ok=0\nfoo:\n  bar:\n    - baz'}
    result._host = MockHost()
    result._host.get_name = lambda: "localhost"
    CM._display = MockDisplay()
    CM.v2_runner_on_failed(result)


# Generated at 2022-06-13 11:52:54.542418
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    module = CallbackModule()

# Generated at 2022-06-13 11:52:59.894142
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from collections import namedtuple
    from ansible.executor.task_result import TaskResult

    Task = namedtuple('Task', ['action'])

    cm = CallbackModule()
    result = TaskResult(None, None)
    result._result = {'changed': False}
    result._task = Task('shell')
    assert cm.v2_runner_on_ok(result) == None

# Generated at 2022-06-13 11:53:01.379933
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule()

if __name__ == '__main__':
    test_CallbackModule()

# Generated at 2022-06-13 11:53:03.486830
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    """Test for adding a host in the class CallbackModule"""
    testObject = CallbackModule()
    assert testObject



# Generated at 2022-06-13 11:53:05.814944
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    result_instance = CallbackModule()
    result_instance.v2_runner_on_ok({'changed': True})


# Generated at 2022-06-13 11:53:12.220165
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.playbook.task_include import TaskInclude
    task = TaskInclude()
    task._role = {'name': 'something'}
    from ansible.playbook.task import Task
    t = Task()
    t.name = 'task name'
    from ansible.executor.task_result import TaskResult
    r = TaskResult(host=None, task=t, return_data={})

# Generated at 2022-06-13 11:53:22.021385
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cb = CallbackModule()



# Generated at 2022-06-13 11:53:33.715138
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import collections
    import json

    class FakeHost:

        def get_name(self):
            return 'fakehost'

    class FakeResult:

        def __init__(self, result):
            self._result = result

        def get_name(self):
            return 'fakehost'

    class FakeDisplay:

        def __init__(self):
            self.str = ''

        def display(self, msg, color):
            self.str += msg

    display = FakeDisplay()
    fakehost = FakeHost()

    class FakeCallbackModule:

        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'oneline'
        _display = display

    # Tests with no exception
    callback_module = FakeCallbackModule()

# Generated at 2022-06-13 11:53:37.081881
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import ansible.plugins.callback.default
    callbackModule = ansible.plugins.callback.default.CallbackModule()

    # Create a result with multiple keys (same as ansible result)
    result = {"stdout": "\n123\n456\n"}

    # Execute the code being tested
    callbackModule.v2_runner_on_ok(result)

    # Verify that the output string is equal
    assert result["stdout"] == "123\n456\n"


# Generated at 2022-06-13 11:53:42.503157
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import ansible.plugins.callback.oneline
    print("Testing function v2_runner_on_ok of class CallbackModule")
    _display = None
    result = None
    cb = ansible.plugins.callback.oneline.CallbackModule(_display)
    _result = {"changed":True}
    result._result = _result
    result._host.get_name = lambda : "localhost"
    cb.v2_runner_on_ok(result)

# Generated at 2022-06-13 11:53:53.687195
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    """
    Test method v2_runner_on_ok of class CallbackModule
    """
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_iterator import PlayIterator
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.callback.oneline import CallbackModule
    from ansible.plugins.loader import callback_loader

    # Create a DataLoader object to be used by the plugins
    loader = DataLoader()

    # Create a variable manager to be used by the plugins
    variable_manager = VariableManager()

    # Create a result

# Generated at 2022-06-13 11:53:54.718344
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    return CallbackModule()


# Generated at 2022-06-13 11:53:55.271722
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    pass

# Generated at 2022-06-13 11:53:55.926667
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    pass

# Generated at 2022-06-13 11:54:01.743011
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible.plugins.callback import CallbackBase
    from ansible import constants as C
    cbm = CallbackModule()
    print(dir(cbm))
    print(cbm.CALLBACK_VERSION)
    print(cbm.CALLBACK_TYPE)
    print(cbm.CALLBACK_NAME)
    print(cbm._display)
    print(cbm._plugin_name)
    print(cbm._plugin_options)

test_CallbackModule()

# Generated at 2022-06-13 11:54:12.663923
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import pytest
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    
    fixture_data = {
        'task': {
            'action': 'raw'
        },
        '_result': {
        }
    }
    
    # test fixture 047: test execution of CallbackModule.v2_runner_on_ok method with changed status
    fixture_data['_result'] = {
        'changed': 1,
        'msg': 'some message',
        'ansible_facts': {
            'discovered_interpreter_python': '/usr/bin/python'
        }
    }
    result = dict(fixture_data, _host=AnsibleUnsafeText('localhost'))
    bm = CallbackModule()
    res = bm.v2_runner_on_

# Generated at 2022-06-13 11:54:41.955144
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Set up a CallbackModule object
    cbM = CallbackModule()

    # Set up a result object
    hostName = "dummyHost"
    result = {}
    result["stdout"] = "dummyStdout"
    result["stderr"] = "dummyStderr"
    result["rc"] = 1
    result["exception"] = "dummyException"

    # Set up a result._result object
    result._result = {}
    result._result["exception"] = "dummyException"
    result._result["stdout"] = "dummyStdout"
    result._result["stderr"] = "dummyStderr"
    result._result["rc"] = 1
    result._result["changed"] = False

    # Set up a result._task object
    result._task = {}


# Generated at 2022-06-13 11:54:51.027313
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    print('Test CallbackModule')
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.plugins.callback import CallbackBase
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 11:54:56.461488
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback import CallbackBase
    from ansible import constants as C

    class CallbackModule(CallbackBase):
        CALLBACK_VERSION = 2.0

    callback = CallbackModule()

    task_result = {'changed': True}

    # Control test case: test the change flag check.
    result = callback.v2_runner_on_ok({'_result': task_result})
    assert result == None

    # Remove the change flag, test if the output is OK.
    del task_result['changed']
    result = callback.v2_runner_on_ok({'_result': task_result})
    assert result == None

# Generated at 2022-06-13 11:55:02.804521
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    callback = CallbackModule()
    class Host:
        def get_name(self):
            return 'some-host'
    class Task:
        def __init__(self):
            self.action = 'debug'
            self.args = dict(msg='This is a message!')
    class Result:
        def __init__(self, task, host):
            self._task = task
            self._host = host
            self._result = dict(changed=True)
        def __getattr__(self, attrib):
            return self._result.get(attrib, None)
    result = Result(Task(), Host())
    callback.v2_runner_on_ok(result)


# Generated at 2022-06-13 11:55:12.928042
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    # Test when self._display.verbosity < 3
    mock_self = type('', (), {'_display':type('', (), {'verbosity':2}), '_dump_results':lambda self, result: ""})
    result = type('', (), {'_result':{'exception':'Test exception\nError: test error\n'}, '_task':type('', (), {'action':'Test action'}), '_host':type('', (), {'get_name':lambda self: 'Test hostname'})})
    assert CallbackModule.v2_runner_on_failed(mock_self, result) == None

    # Test when self._display.verbosity >= 3

# Generated at 2022-06-13 11:55:25.389901
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from collections import namedtuple

    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    # initialize needed objects
    loader = DataLoader()
    options = Options(connection='local', module_path='/path/to/mymodules', forks=100, become=None, become_method=None, become_user=None, check=False,
                      diff=False)
    passwords = dict(vault_pass='secret')

# Generated at 2022-06-13 11:55:34.502460
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback import CallbackBase
    from ansible import constants as C

    cb = CallbackModule()
    task_ansible_str_result = '[{"stdout": "", "invocation": {"module_args": {"name": "ping"}}}]'
    task_ansible_dict = {"changed": False, "invocation": {"module_args": {"name": "ping"}}}
    task_ansible_result = {}
    task_ansible_result["stdout"] = task_ansible_str_result
    host = CallbackBase()
    task = CallbackBase()
    result = CallbackBase()
    task.action = "command"
    result._result = task_ansible_result
    result._host = host
    result._task = task
    #result._task.action = "command"
   

# Generated at 2022-06-13 11:55:35.115089
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert(CallbackModule)

# Generated at 2022-06-13 11:55:42.776209
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # init and prepare class instance
    import ansible.plugins.callback as callback
    callback.CallbackModule = CallbackModule

    from ansible.plugins.callback import CallbackModule
    c = CallbackModule()

    # prepare result for test
    result = type('FakeResult', (object,), {})
    result._result = {
        'exception': 'Traceback',
        '_result': {
            'changed': False
        }
    }
    result._task = type('FakeTask', (object,), {'action': 'debug'})
    result._host = type('FakeHost', (object,), {'get_name': lambda: 'localhost'})

    # set verbosity to low
    c._display.verbosity = 0

    # Unit test v2_runner_on_failed

# Generated at 2022-06-13 11:55:51.327866
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    class FakeHost():
        def get_name():
            return 'localhost'
        get_name = staticmethod(get_name)
    
    class FakeResult():
        def __init__(self, host, result):
            self._host = host
            self._result = result
        def get_name():
            return self._host.get_name()
        get_name = staticmethod(get_name)
        
    class FakeTask():
        def __init__(self, action):
            self.action = action
        def get_action():
            return self.action
        get_action = staticmethod(get_action)
        
    class FakeDisplay():
        def __init__(self, verbosity):
            self.verbosity = verbosity

# Generated at 2022-06-13 11:56:29.786886
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    module = CallbackModule()
    assert(module.CALLBACK_VERSION == 2.0)
    assert(module.CALLBACK_TYPE == 'stdout')
    assert(module.CALLBACK_NAME == 'oneline')

# Generated at 2022-06-13 11:56:35.885465
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
	import json
	from ansible.plugins.callback import CallbackBase
	from ansible import constants as C
	result = CallbackBase()
	status = {'changed': True, 'msg': 'test message'}
	result._result = json.dumps(status)
	result._task = {'action': 'test'}
	result._host = {'get_name': 'test'}
	c = CallbackModule()
	c.v2_runner_on_ok(result)
	assert len(c._display.display.call_args_list) == 1, "There is only one call to display() method of CallbackBase class"

# Generated at 2022-06-13 11:56:37.812396
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible.plugins.callback.oneline import CallbackModule
    x = CallbackModule()
    assert x is not None

# Generated at 2022-06-13 11:56:39.185131
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
  assert True


# Generated at 2022-06-13 11:56:46.348883
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    class Test(object):
        name = 'myhost'
        result = {}
    class Test2(object):
        class Test3(object):
            name = 'myhost'
            result = {}
        _host = Test3()
    class Test4(object):
        _host = Test2()
    class Test5(object):
        action = 'test'
        _result = {'changed': False}
        _task = Test5()
    class Test6(object):
        display = Test()
        _display = Test()
    class Test7(object):
        _result = {'changed': False}
        _task = Test5()
        _dump_results = Test()
        _display = Test()
        v2_runner_on_ok = CallbackModule.v2_runner_on_ok
        result = Test7

# Generated at 2022-06-13 11:56:47.965834
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    obj = CallbackModule()
    assert(obj.CALLBACK_VERSION == 2.0)

# Generated at 2022-06-13 11:56:57.073431
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Just make sure that the callback is not returning a None object.
    runner_mock = lambda: None
    runner_mock.get_name = lambda: "test_host"
    host_mock = lambda: None
    host_mock.get_name = lambda: "test_host"
    result_mock = lambda: None
    result_mock._host = host_mock
    result_mock._result = {"changed": True}
    result_mock._task = None
    display_mock = lambda: None
    display_mock.display = lambda x, y: x
    display_mock.verbosity = 3

    # Configure the test object
    callback = CallbackModule()
    callback._dump_results = lambda x, y: ""
    callback._display = display_mock

    # Run the

# Generated at 2022-06-13 11:57:02.293181
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Define the test environment
    module = "setup"
    hostname = "test_host"

# Generated at 2022-06-13 11:57:09.972752
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    c = CallbackModule()
    c.set_options({})
    result = {'_host': {'get_name': (lambda : 'localhost')}, '_result': {'stderr': '', 'rc': 255, 'stdout': 'No route to host'}}
    assert c.v2_runner_on_failed(result) == "localhost | FAILED! => {'stderr': '', 'stdout': 'No route to host', 'rc': 255}"


# Generated at 2022-06-13 11:57:11.191016
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    obj = CallbackModule()
    assert obj


# Generated at 2022-06-13 11:58:42.652363
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import sys
    from ansible.plugins.callback.oneline import CallbackModule

    class Result(object):
        def __init__(self):
            self._result = {'exception': "", 'failed': True}
            self._task = Task()
            self._host = Host()
            self._result['exception'] = "An exception occurred during task execution. To see the full traceback, use -vvv. The error was: error"
            self.color = ""

        class Host(object):
            def __init__(self):
                self.get_name = lambda: ''

        class Task(object):
            def __init__(self):
                self.action = "No json"

    # Get object of class CallbackModule
    obj = CallbackModule()
    obj._display = Display()

    # Unit test for method with

# Generated at 2022-06-13 11:58:48.002639
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Test normal case
    cb_mod = CallbackModule()
    result = type('Result', (object,), {'_host': type('Host', (object,), {'get_name': lambda x: 'a'})})
    result._task = type('Task', (object,), {'action': 'ping'})
    result._result = {'stdout': '2', 'rc': 0}
    cb_mod.v2_runner_on_ok(result)

    # Test normal case
    cb_mod = CallbackModule()
    result = type('Result', (object,), {'_host': type('Host', (object,), {'get_name': lambda x: 'a'})})
    result._task = type('Task', (object,), {'action': 'command'})

# Generated at 2022-06-13 11:59:00.163155
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader

    from ansible.constants import __file__ as constants_filepath
    from os.path import abspath, dirname, join
    ansible_path = dirname(dirname(dirname(abspath(constants_filepath))))
    data_path = join(ansible_path, 'lib', 'ansible', 'plugins', 'callback')
    callback_path = join(data_path, 'oneline.py')

# Generated at 2022-06-13 11:59:03.211800
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    module = CallbackModule()
    assert module.CALLBACK_VERSION == 2.0
    assert module.CALLBACK_TYPE == 'stdout'
    assert module.CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:59:03.766000
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pass

# Generated at 2022-06-13 11:59:10.182436
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cb = CallbackModule()
    cb.v2_runner_on_failed()
    cb.v2_runner_on_ok()
    cb.v2_runner_on_unreachable()
    cb.v2_runner_on_skipped()
    cb._command_generic_msg('host',dict(stdout = 'out', stderr = 'err'), 'command')
    cb._command_generic_msg('host', dict(stdout = 'out'), 'command')
    #cb._play.verbosity = 0
    cb.v2_runner_on_failed({'_host': dict(name = 'host'), '_result': dict(exception = Exception('error'), _task = dict(action = 'action') )})

# Generated at 2022-06-13 11:59:20.982792
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    text1 = '''{"changed": false, "ping": "pong"}'''
    text2 = '''{"changed": true, "ping": "pong"}'''
    text3 = '''{"ping": "pong"}'''

    result1 = CallbackModule().v2_runner_on_ok(text1)
    result2 = CallbackModule().v2_runner_on_ok(text2)
    result3 = CallbackModule().v2_runner_on_ok(text3)

    assert result1 == "| SUCCESS => {'changed': False, 'ping': 'pong'}"
    assert result2 == "| CHANGED => {'changed': True, 'ping': 'pong'}"
    assert result3 == "| SKIPPED => {'ping': 'pong'}"


# Generated at 2022-06-13 11:59:25.779769
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result_obj = {}
    result_obj["_result"] = "error"
    result_obj["_host"] = {"_name" : "Test-Host"}
    result_obj_dict = {}
    result_obj_dict["_result"] = result_obj
    result_obj_dict["ignore_errors"] = False
    cb_obj = CallbackModule()
    assert cb_obj.v2_runner_on_failed(result_obj_dict) == None


# Generated at 2022-06-13 11:59:30.347822
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    task_result = {'exception': 'simple exception'}
    result = MockResult(task_result)
    callback = CallbackModule()
    callback.v2_runner_on_failed(result)


# Generated at 2022-06-13 11:59:40.929967
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible.plugins.callback import CallbackBase
    x = CallbackBase()
    assert(x.disabled is False)
    assert(x.blocked_paths is None)
    assert(x.get_option() is None)
    assert(x.task_start() is None)
    assert(x.task_ok() is None)
    assert(x.task_ok() is None)
    assert(x.task_failed() is None)
    assert(x.task_unreachable() is None)
    assert(x.task_skipped() is None)
    assert(x.play_start() is None)
    assert(x.play_ok() is None)
    assert(x.play_failed() is None)
    assert(x.cleanup_task() is None)