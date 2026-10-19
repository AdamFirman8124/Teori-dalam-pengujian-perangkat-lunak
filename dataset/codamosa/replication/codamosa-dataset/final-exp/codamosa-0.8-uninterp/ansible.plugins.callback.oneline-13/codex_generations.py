

# Generated at 2022-06-13 11:51:33.757330
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    cbm = CallbackModule()
    res = dict()
    fb = dict()
    fb["action"] = "command"
    fb["changed"] = False
    res["result"] = fb
    cbm.v2_runner_on_ok(res)


# Generated at 2022-06-13 11:51:35.293380
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule.CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:51:44.430593
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback import CallbackModule
    # Task variables are available as a dict-like object
    import json

    result = json.dumps({"changed": False,
                         "invocation": {"module_args": ""}})

    result_changed = json.dumps({"changed": True,
                                 "invocation": {"module_args": ""}})

    result_failed = json.dumps({"failed": True,
                                "invocation": {"module_args": ""}})

    result_unreachable = json.dumps({"unreachable": True,
                                     "invocation": {"module_args": ""}})

    result_skipped = json.dumps({"skipped": True,
                                 "invocation": {"module_args": ""}})

    result_changed_silent = json.d

# Generated at 2022-06-13 11:51:48.442534
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule(display=None).CALLBACK_VERSION == 2.0
    assert CallbackModule(display=None).CALLBACK_TYPE == 'stdout'
    assert CallbackModule(display=None).CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:51:51.812956
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    module = CallbackModule()
    assert module.CALLBACK_VERSION == 2.0
    assert module.CALLBACK_TYPE == 'stdout'
    assert module.CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:51:57.405859
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    m_callback = CallbackModule()
    m_result = Result()
    m_result._result = {'exception': 'This is exception text'}
    m_result._task = 'task'
    m_result._task.action = 'action'
    m_result._host = 'hostname'
    #invoke the tested method
    m_callback.v2_runner_on_failed(m_result, ignore_errors=False)


# Generated at 2022-06-13 11:52:08.900662
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import pytest
    from ansible.plugins.callback.oneline import CallbackModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    oneline = CallbackModule()
    oneline.set_options(verbosity=0)

# Generated at 2022-06-13 11:52:16.683749
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    class MyDisplay:
        def __init__(self):
            self.messages = []
        def display(self, msg, color=None):
            self.messages.append(msg)
    display = MyDisplay()
    c = CallbackModule()
    c._display = display
    result = {u'changed': False, u'invocation': {u'module_name': u'win_ping'}}
    result['_result'] = result
    result['_host'] = {'get_name': lambda: 'server'}
    result['_task'] = {'action': u'module'}
    c.v2_runner_on_ok(result)

# Generated at 2022-06-13 11:52:22.649018
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    class FakeHost:
        def get_name(self):
            return 'host'
    class FakeResult:
        def __init__(self, host, outcome):
            self._host = host
            self._result = outcome
            self._task = FakeTask('action')
    class FakeTask:
        def __init__(self, action):
            self.action = action

    host = FakeHost()
    failed = FakeResult(host, {'msg': 'ERROR'})
    skipped = FakeResult(host, {'skipped': True, 'msg': 'SKIPPED'})
    c = CallbackModule()
    assert c.v2_runner_on_failed(failed) == 'host | FAILED! => {"msg": "ERROR"}'
    assert c.v2_runner_on_failed(skipped) is None
# Unit

# Generated at 2022-06-13 11:52:34.248720
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import mock
    import sys

    # Create a mock object for class _Display
    display_obj = mock.Mock()

    # Create a mock object for class Runner
    runner_obj = mock.Mock()
    runner_obj.get_name.return_value = 'localhost'
    runner_obj.get_result.return_value = { 'exception': 'Test Exception'}

    # Create a mock object for class Task
    task_obj = mock.Mock()
    task_obj.get_action.return_value = 'debug'

    # Create a mock object for class Result
    result_obj = mock.Mock()
    result_obj.task = task_obj
    result_obj.get_result.return_value = { 'exception': 'Test Exception'}

# Generated at 2022-06-13 11:52:39.283165
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    pass

# Generated at 2022-06-13 11:52:40.577227
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert ('name' in CallbackModule.__dict__)

# Generated at 2022-06-13 11:52:50.831356
# Unit test for constructor of class CallbackModule
def test_CallbackModule():

    c = CallbackModule()
    c._display = c

    test_dict = {
        'rc': 0,
        'stdout': 'result of `test command`',
    }

    # test v2_runner_on_failed
    test_hostname = 'host'
    test_result = "The error message"
    res = c.v2_runner_on_failed(test_result)
    assert res == "host | FAILED! => The error message"

    # test v2_runner_on_ok with changed = False
    test_results = {
        'rc': 0,
        'stdout': 'result of `test command`',
        'changed': False,
        'ansible_job_id': '1718068050'
    }
    res = c.v2_runner_on_ok

# Generated at 2022-06-13 11:52:54.498915
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    module = CallbackModule()
    assert 'oneline' == module.CALLBACK_NAME
    assert 'stdout' == module.CALLBACK_TYPE
    assert 2.0 == module.CALLBACK_VERSION

# Generated at 2022-06-13 11:53:02.988829
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    bm = CallbackModule()
    # case 1: If 'exception' in result._result but self._display.verbosity < 3.
    #         The value of msg should be "An exception occurred during task execution. To see the full traceback, use -vvv. The error was: %s" % error
    result_1 = {}
    result_1['exception'] = "Hello World"
    result_1['_host'] = "hostname"

    result_1['_result'] = {}
    result_1['_result']['_task'] = {}
    result_1['_result']['_task']['action'] = "C.MODULE_NO_JSON"

    bm._display = {}
    bm._display['verbosity'] = 2

# Generated at 2022-06-13 11:53:12.764376
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    '''
    This is the default callback interface, which simply prints messages
    to stdout when new callback events are received.
    '''

    from ansible.plugins.callback import CallbackBase
    from ansible import constants as C


    class CallbackModule(CallbackBase):

        '''
        This is the default callback interface, which simply prints messages
        to stdout when new callback events are received.
        '''

        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'oneline'

        def _command_generic_msg(self, hostname, result, caption):
            stdout = result.get('stdout', '').replace('\\n', '').replace('\r', '\\r')

# Generated at 2022-06-13 11:53:13.928490
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # TODO
    pass


# Generated at 2022-06-13 11:53:23.053293
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    '''
    Simulate a successful task execution on the localhost
    '''
    from ansible.plugins.callback.oneline import CallbackModule
    import json
    import pprint
    CM = CallbackModule()
    CM._display = MockDisplay()

# Generated at 2022-06-13 11:53:25.899615
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    module = CallbackModule()

    assert module.CALLBACK_NAME == 'oneline'
    assert module.CALLBACK_TYPE == 'stdout'
    assert module.CALLBACK_VERSION == 2.0

# Generated at 2022-06-13 11:53:29.340980
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    global objCallbackModule
    objCallbackModule = CallbackModule()
    assert repr(objCallbackModule)
    assert isinstance(objCallbackModule, CallbackModule)


# Generated at 2022-06-13 11:53:47.620605
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    class TestHost:
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    class TestResult:
        def __init__(self, host, result):
            self._host = host
            self._result = result

        def __getattribute__(self, name):
            if name in ['_host', '_result']:
                return object.__getattribute__(self, name)
            return getattr(self._result, name)

        def _task(self):
            return self._result

    class TestDisplay:
        def __init__(self):
            self.buffer = []

        def display(self, msg, color):
            self.buffer.append(msg)

        def pop(self):
            return self.buffer.pop()


# Generated at 2022-06-13 11:53:57.535303
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from unittest.mock import MagicMock, patch

    class TestResult:
        def __init__(self, r):
            self._result = r

    class TestHost:
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    class TestDisplay:
        def __init__(self, verbosity):
            self.verbosity = verbosity

    class TestCallbackModule:
        def __init__(self, result):
            self._result = result

        def _display(self, msg, color):
            print(msg)

        def _dump_results(self, result, indent=0):
            return "dump_results"


# Generated at 2022-06-13 11:54:03.260849
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Setup
    result = {
        "_result": {
            "exception": "Some exception occurred",
            "rc": 1
        },
        "_task": {
            "action": "PING"
        },
        "_host": {
            "get_name": lambda: "test_host"
        }
    }

    # Run: Check that the v2_runner_on_failed method returns the correct output
    assert "test_host | FAILED! => {'exception': 'Some exception occurred', 'rc': 1}" == CallbackModule.v2_runner_on_failed(result)


# Generated at 2022-06-13 11:54:14.660236
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost,127.0.0.1')

# Generated at 2022-06-13 11:54:23.819616
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    from ansible.utils.display import Display
    from ansible.plugins.callback import CallbackBase

    display = Display()
    callback = CallbackBase()

    #case 1
    #Input data for function test
    callback.CALLBACK_VERSION = 2.0
    callback.CALLBACK_TYPE = "stdout"
    callback.CALLBACK_NAME = "oneline"
    class result:
        def __init__(self):
            self._result = {'exception': "An exception occurred during task execution. The full traceback is:\n" + "Full traceback" }
            self._task = "task"
            class host:
                def get_name(self):
                    return "hostname"
            self._host = host()
    resultObj = result()
    ignore_errors = False
    display._verbosity = 3

# Generated at 2022-06-13 11:54:30.201086
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    runner_result = { 'changed': True }
    task_action = 'some module'
    task_name = 'some task'
    display_message = None
    class display_mockup:
        def __init__(self):
            pass
        def display(self, message, color):
            nonlocal display_message
            display_message = message
    class result_mockup:
        def __init__(self):
            self._result = runner_result
            self._host = Host(name='testhost')
            self._task = Task(action=task_action, name=task_name)
    display = display_mockup()
    result = result_mockup()
    callback = CallbackModule()
    callback._display = display
    callback.v2_runner_on_ok(result)

# Generated at 2022-06-13 11:54:34.318099
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    callback = CallbackModule()
    assert callback.CALLBACK_VERSION == 2.0
    assert callback.CALLBACK_TYPE == 'stdout'
    assert callback.CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:54:44.844893
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result_dict = dict()

# Generated at 2022-06-13 11:54:47.847398
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    ansible_result = {'skipped': False, 'changed': False, 'failed': False}
    hostInfo = {'name': 'example-host', 'force_color': True}
    task_info = {'action': 'shell command', 'name': 'command'}

    result = {'_result': ansible_result, '_task': task_info, '_host': hostInfo}

    oneline_out = CallbackModule()
    assert oneline_out.v2_runner_on_ok(result) == None


# Generated at 2022-06-13 11:54:54.624363
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import mock
    import ansible.plugins.callback.oneline
    import ansible.utils.display
    callback = ansible.plugins.callback.oneline.CallbackModule()
    callback._display = mock.create_autospec(ansible.utils.display.Display)
    hostname = 'localhost'
    result = {'rc': 1}
    callback.v2_runner_on_failed(result, ignore_errors=False)
    callback._display.display.assert_called_with("localhost | FAILED! => {'rc': 1}", color='red')
    callback._display.verbosity = 4
    callback.v2_runner_on_failed(result, ignore_errors=False)
    callback._display.display.assert_called_with("localhost | FAILED! => {'rc': 1}", color='red')


# Generated at 2022-06-13 11:55:20.102122
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    plugin = CallbackModule()
    result = type('', (), {})()
    result._result = {'changed': True}
    result._result['stdout'] = 'test output'
    result._result['stderr'] = 'test error'
    result._result['rc'] = 0
    result._task = type('', (), {})()
    result._task.action = 'shell'
    import ansible
    result._host = type('', (), {})()
    result._host.__module__ = ansible.__version__
    result._host.get_name = lambda: 'mock-host-name'
    assert '%s | FAILED! => %s' % (result._host.get_name(), result._result) == plugin.v2_runner_on_failed(result)

# Generated at 2022-06-13 11:55:29.717042
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible.plugins import callback_loader
    callback = callback_loader.get('oneline', {})
    callback_obj = callback()
    for i in callback_obj.CALLBACK_VERSION, callback_obj.CALLBACK_TYPE, callback_obj.CALLBACK_NAME:
        assert i != '', str(i) + ' must not be blank.'
    assert True == isinstance(callback_obj, CallbackModule), "test_CallbackModule() failed."

if __name__ == '__main__':
    from pytest import main
    main([__file__])

# Generated at 2022-06-13 11:55:38.338210
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.runner.return_data import ReturnData
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager

    result = ReturnData({'hostname': 'localhost', 'exception': 'exception message'}, Host('localhost'), VariableManager())
    cb = CallbackModule()
    cb.v2_runner_on_failed(result)
    assert cb._display.color == '\033[91m'
    assert cb._display.display_msg == 'An exception occurred during task execution. To see the full traceback, use -vvv. The error was: exception message'

# Generated at 2022-06-13 11:55:39.135481
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    x = CallbackModule()

# Generated at 2022-06-13 11:55:45.538091
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    test_obj = CallbackModule()
    result = DummyResult()
    result._host = DummyHost()
    result._host.get_name.return_value = 'Dummy Host'
    result._result = {
        'changed': False,
    }
    result._task = DummyTask()
    result._task.action = 'Dummy Action'
    result._result = {
        'changed': True,
    }
    # Call v2_runner_on_ok of class CallbackModule
    test_obj.v2_runner_on_ok(result)


# Generated at 2022-06-13 11:55:46.999620
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cb = CallbackModule()
    assert cb.CALLBACK_TYPE == 'stdout'

# Generated at 2022-06-13 11:55:50.033691
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    hostname = 'Rasp'
    result = {'changed':False}
    color = C.COLOR_OK
    state = 'SUCCESS'
    assert CallbackModule.v2_runner_on_ok(hostname, result, color, state) == None


# Generated at 2022-06-13 11:55:51.626416
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    # Test CallbackModule constructor
    global _
    global callback
    _ = CallbackModule()
    callback = CallbackModule()

# Generated at 2022-06-13 11:55:54.231520
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    """
    This function is used to test the constructor of the class CallbackModule
    """
    obj = CallbackModule()
    assert isinstance(obj, CallbackModule)

# Generated at 2022-06-13 11:56:04.199894
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    print("\n======= Test =======")
    from ansible.plugins.callback import CallbackBase
    from ansible import constants as C

    class CallbackModule(CallbackBase):
        '''
        Callback for Ansible.
        '''

        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'oneline'

        def v2_runner_on_failed(self, result, ignore_errors=False):
            if 'exception' in result._result:
                if self._display.verbosity < 3:
                    # extract just the actual error message from the exception text
                    error = result._result['exception'].strip().split('\n')[-1]

# Generated at 2022-06-13 11:56:40.387113
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback import CallbackBase
    test_object = CallbackBase()
    assert test_object.v2_runner_on_ok() is None


# Generated at 2022-06-13 11:56:46.706771
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = {}
    result_key_errors = []
    result_key_errors.append("rc")
    result_key_errors.append("stdout")
    result_key_errors.append("_ansible_parsed")
    result_key_errors.append("_ansible_no_log")
    result_key_errors.append("_ansible_item_label")
    result_key_errors.append("_ansible_verbose_always")
    result_key_errors.append("cmd")
    result_key_errors.append("date")
    result_key_errors.append("start")
    result_key_errors.append("invocation")
    result_key_errors.append("delta")
    result_key_errors.append("end")
    result_key_errors.append("msg")
   

# Generated at 2022-06-13 11:56:55.898446
# Unit test for method v2_runner_on_failed of class CallbackModule

# Generated at 2022-06-13 11:57:03.345845
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    # Create a mock PluginManager object
    plugin_manager = Mock()

    # Create a mock display object
    display = Mock()

    # Create a mock result object
    result = Mock()

    # Create a mock host object
    host = Mock()

    # Create a mock task object
    task = Mock()

    # Create a mock result object
    exception = Mock()

#    # Create a callback_oneline object
#    callback_oneline = CallbackModule(plugin_manager=plugin_manager, display=display)
   
    # Create a callback_oneline object
    callback_oneline = CallbackModule(display=display)

    # Tell the mock result object that the attribute result is
    # a dictionary containing the dictionary {'exception': exception}
    result.get.return_value = {'exception' : exception }

    # Tell

# Generated at 2022-06-13 11:57:13.254963
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    import json
    import sys

    if sys.version_info.major < 3:
        import StringIO as io
    else:
        import io

    class FakeDisplay(object):
        def __init__(self):
            self.output = io.StringIO()

        def display(self, msg, color=None):
            self.output.write(msg)
            self.output.write('\n')

    task = Task()
    task.action = 'setup'
    task.name = 'Gathering Facts'
    task.args = {}
    task.tags = []

    fake_display = FakeDisplay()

    play_context = FakePlayContext()
    variable_manager = VariableManager()

    result = FakeResult()
   

# Generated at 2022-06-13 11:57:14.297772
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    pass


# Generated at 2022-06-13 11:57:24.559007
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.task import Task
    from ansible.plugins.strategy import StrategyBase
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager.set_inventory(inventory)
    variable_manager.set_inventory(inventory)
    variable_manager.extra_vars = {'customer': 'test', 'disabled': True}

# Generated at 2022-06-13 11:57:33.017745
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = Mock()
    result.host = Mock()
    result.host.get_name.return_value = 'hostname'
    result._result = {
                        'exception': 'An exception occurred during task execution.\nTraceback?\nTraceback?\nTraceback?',
                        'rc': 1
                    }

    display = Mock()
    display.color = False
    display.verbosity = 3
    display.display.return_value = 'failed'
    cb = CallbackModule()
    cb._display = display

    assert cb.v2_runner_on_failed(result) == True
    assert display.display.call_count == 1
    call = display.display.call_args_list[0]

# Generated at 2022-06-13 11:57:40.798112
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # CallbackModule(display, verbosity).v2_runner_on_ok(result)
    ansible.cli.CLI.setup()

# Generated at 2022-06-13 11:57:44.305165
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Test1: no arguments
    a = CallbackModule()
    b = a.v2_runner_on_ok()
    expected = True
    actual = b is None
    assert expected == actual

# Generated at 2022-06-13 11:59:20.762265
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    class TestCallbackModule(CallbackModule):
        def __init__(self):
            self.display = TestDisplay()

    class TestDisplay(object):
        def __init__(self):
            self._last_display = None
        def display(self, msg, color):
            self._last_display = msg
        @property
        def last_display(self):
            return self._last_display


# Generated at 2022-06-13 11:59:26.607927
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    '''
    Unit test for method v2_runner_on_failed of class CallbackModule
    '''
    print("In test_CallbackModule_v2_runner_on_failed()")
    c = CallbackModule()

    import json
    import collections
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager,host_list='/etc/ansible/hosts')
    variable_manager.set_inventory(inventory)

    # create data structure that represents our play,

# Generated at 2022-06-13 11:59:36.680851
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import ansible.plugins.callback.oneline
    import ansible.vars
    import ansible.inventory.host
    import collections
    ckwargs = collections.namedtuple(
        'Ckwargs',
        ['callback_whitelist']
    )
    ansible_options = collections.namedtuple('AnsibleOptions', ['connection'])
    runner = collections.namedtuple('Runner', ['inventory', 'options'])
    runner.options = ansible_options('local')
    runner.inventory = ansible.inventory.Inventory(host_list=[])
    host = ansible.inventory.host.Host(name='test_host')
    runner.inventory.add_host(host)
    result = collections.namedtuple('Result', ['_result', '_task', '_host'])
    result._result = {}

# Generated at 2022-06-13 11:59:41.973295
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    callback = CallbackModule()
    result = dict()
    result['exception'] = "An"
    result['_task'] = dict()
    result['_task']['action'] = 'abc'
    result['_host'] = dict()
    result['_host']['get_name'] = lambda x: "a host name"
    callback.v2_runner_on_failed(result)

# Generated at 2022-06-13 11:59:51.065525
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    # Test parameters
    callback = CallbackModule()
    # Test execution
    result = callback.v2_runner_on_failed({'rc':-1, 'stdout':'foo'})
    assert result == 'localhost | FAILED! => {u\'rc\': -1, u\'stdout\': u\'foo\'}', 'Test Failed'
    result = callback.v2_runner_on_ok({'rc':-1, 'changed':True, 'stdout':'foo'})
    assert result == 'localhost | CHANGED => {u\'rc\': -1, u\'changed\': True, u\'stdout\': u\'foo\'}', 'Test Failed'
    result = callback.v2_runner_on_unreachable({'rc':-1, 'stdout':'foo'})

# Generated at 2022-06-13 11:59:52.077105
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    c = CallbackModule()

# Generated at 2022-06-13 12:00:01.553236
# Unit test for method v2_runner_on_failed of class CallbackModule

# Generated at 2022-06-13 12:00:02.355407
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cb = CallbackModule()

# Generated at 2022-06-13 12:00:03.146319
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert 'CallbackModule' in globals()

# Generated at 2022-06-13 12:00:09.947880
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    """Test for constructor of class CallbackModule."""

    class Options(object):
        verbosity = 1
        one_line = True
        show_custom_stats = None
        callbacks = None
        callback_whitelist = None
        callback_plugins = None
        transport = 'ssh'

    def get_option(option):
        """Fake get_option."""
        return getattr(Options, option)

    class Display(object):
        """Fake Display."""
        verbosity = 1
        display = print

    options = Options()
    stdout = []

    def fake_display(msg, color=None, stderr=False, screen_only=False, log_only=False):
        stdout.append(msg)

    display = Display()
    display.display = fake_display
    plugin = CallbackModule()
