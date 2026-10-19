

# Generated at 2022-06-13 11:51:32.541299
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    pass

# Generated at 2022-06-13 11:51:33.146764
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cb = C

# Generated at 2022-06-13 11:51:38.256859
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    module = CallbackModule()
    print("CALLBACK_VERSION=" + str(module.CALLBACK_VERSION))
    print("CALLBACK_TYPE=" + str(module.CALLBACK_TYPE))
    print("CALLBACK_NAME=" + str(module.CALLBACK_NAME))

test_CallbackModule()

if __name__ == "__main__":
    pass

# Generated at 2022-06-13 11:51:39.337928
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    assert True


# Generated at 2022-06-13 11:51:40.281413
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert 1

test_CallbackModule()

# Generated at 2022-06-13 11:51:48.001485
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.plugins.callback import CallbackBase

    class CallbackModule(CallbackBase):
        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'oneline'

        def _command_generic_msg(self, hostname, result, caption):
            stdout = result.get('stdout', '').replace('\n', '\\n').replace('\r', '\\r')
            if 'stderr' in result and result['stderr']:
                stderr = result.get('stderr', '').replace('\n', '\\n').replace('\r', '\\r')

# Generated at 2022-06-13 11:51:56.892391
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    c = CallbackModule()

    result = object()
    result.host = object()
    result.host.name = "server1"

    result.task = object()
    result.task.action = "something"

    result.result = dict()
    result.result['stdout'] = "some data"
    result.result['rc'] = 0

    c.runner = object()
    c.runner.get_test = lambda: False
    c.runner.display = object()
    c.runner.display.colorize = lambda data, color: data
    c.runner.display.verbosity = 0

    c.v2_runner_on_ok(result)

# Generated at 2022-06-13 11:51:59.979612
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    module = CallbackModule()
    assert module.CALLBACK_TYPE == 'stdout'



# Generated at 2022-06-13 11:52:10.019944
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback import CallbackModule
    import json
    import sys

    runner_result = {'changed': True}
    runner_result_json = json.dumps(runner_result)

    class MockHost:
        def __init__(self):
            self._name = "host"

        def get_name(self):
            return self._name

    class MockTask:
        def __init__(self):
            self._action = "test"

        def action(self):
            return self._action

    class MockResult:
        def __init__(self, result_json):
            self._result = json.loads(result_json)
            self._host = MockHost()
            self._task = MockTask()

        def _result(self):
            return self._result


# Generated at 2022-06-13 11:52:21.578363
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Setup
    class MyDisplay:
        def display(self, msg, color=False):
            assert msg == 'localhost | SUCCESS => {"changed": false, "foo": false, "invocation": {"module_args": {"name": "coke"}}, "results": "coke"}'
    my_display = MyDisplay()
    class MyHost:
        def get_name(self):
            return 'localhost'
    my_host = MyHost()
    class MyResult:
        def __init__(self):
            self._result = {'changed': False, 'foo': False, 'invocation': {'module_args': {'name': 'coke'}}, 'results': 'coke'}
            self._task = {'action': 'test'}
            self._host = my_host
    mock_result = MyResult

# Generated at 2022-06-13 11:52:26.759574
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    pass

# Generated at 2022-06-13 11:52:36.984886
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible import context, utils, constants as C
    context.CLIARGS = utils.parse_kv(C.DEFAULT_CLI_ARGS)
    import sys
    sys.argv = ['./ansible-playbook', '-o one-line']
    import logging
    logging.basicConfig(level=logging.DEBUG)
    callback = CallbackModule()
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-13 11:52:39.349294
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import ansible.plugins.callback.oneline as target
    b = target.CallbackModule()
    b.v2_runner_on_failed({'exception': 'exc'})
    assert True

# Generated at 2022-06-13 11:52:48.530317
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.plugins.callback import CallbackBase

    class TestCallbackModule(CallbackBase):
        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'oneline'

    test_module = TestCallbackModule()


# Generated at 2022-06-13 11:53:03.078004
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    callback_module = CallbackModule()

    NO_CHANGE = 5

# Generated at 2022-06-13 11:53:04.256476
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    CallbackModule()

# Generated at 2022-06-13 11:53:13.536009
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():

    import ansible.constants as C

    class Host:

        def get_name(self):
            return "myhostname"

    class Task:

        def __init__(self):
            self.action = C.ACTION_COMMAND

    class Result:

        def __init__(self, result):
            self._result = result
            self._host = Host()
            self._task = Task()

    class Display:

        def __init__(self):
            self.msg = ""
            self.color = None

        def display(self, msg, color):
            self.msg = msg
            self.color = color

    callbacks = CallbackModule()
    callbacks._display = Display()


# Generated at 2022-06-13 11:53:22.805157
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Mocked class of ansible._common_util_common.Result
    class Result:
        _result = dict()
        _host = dict()

        def __init__(self, host, results):
            self._host = host
            self._result = results

    # Mocked class of ansible.runner.action_base.ActionBaseV2.ActionBaseV2
    class ActionBaseV2:
        action = ''

        def __init__(self, action):
            self.action = action

    # Mocked class of ansible.playbook.play_context.PlayContext.PlayContext
    class PlayContext:
        def __init__(self):
            self.verbosity = 2

    # Mocked class of ansible.cli.cli_common.display
    class Display:
        verbosity = 2


# Generated at 2022-06-13 11:53:25.777531
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # initialize a fake class
    cb = CallbackModule()
    result = {'exception': 'some exception'}
    cb.v2_runner_on_failed(result)


# Generated at 2022-06-13 11:53:33.354978
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    ret = {}
    ret['stdout'] = 'hello'
    ret['rc'] = 0
    ret['changed'] = True
    class Result():
        def __init__(self):
            self._result = ret
            self._host = 'hostname'
            self._task = ''
    result = Result()
    callback = CallbackModule()
    callback.v2_runner_on_ok(result)
    assert result._result.get('changed', False)

# Generated at 2022-06-13 11:53:49.816983
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    my_dict = {
          "ansible_job_id": "",
          "invocation": {
            "module_args": {}
          },
          "msg": "The task includes an option with an undefined variable. The error was: 'unset' is undefined",
          "rc": 1
        }
    result = MockRunnerResult(my_dict)
    callback = CallbackModule()
    callback.v2_runner_on_failed(result, ignore_errors=False)
# End of unit test for method v2_runner_on_failed of class CallbackModule



# Generated at 2022-06-13 11:53:58.774268
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    test = CallbackModule()

    test._display = {}
    test._display.__dict__ = {}
    test._display.__dict__['verbosity'] = 0

    result = {
        "_host": "localhost",
        "_result": {
            "exception": "error test"
        }
    }
    test.v2_runner_on_failed(result)

    test._display.__dict__['verbosity'] = 1
    test.v2_runner_on_failed(result)

    test._display.__dict__['verbosity'] = 3
    test.v2_runner_on_failed(result)

    result = {
        "_host": "localhost",
        "_result": {}
    }
    test.v2_runner_on_failed(result)

# Generated at 2022-06-13 11:53:59.465613
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert(CallbackModule)

# Generated at 2022-06-13 11:54:03.105216
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    #Test whether the callback instance can be created
    this_callback = CallbackModule()
    #Test the method using an empty result instance
    #So we are not testing the methods that are called within this method
    this_result = Result()

    #Test whether the result instance is empty before calling the method
    assert len(this_result.get_result()) == 0

    #Call the method
    this_callback.v2_runner_on_failed(this_result, this_result)

    #Test whether the result instance is empty after calling the method
    assert len(this_result.get_result()) == 0


# Generated at 2022-06-13 11:54:06.588398
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    c = CallbackModule()
    assert c.CALLBACK_NAME == 'oneline'
    assert c.CALLBACK_TYPE == 'stdout'
    assert c.CALLBACK_VERSION == 2.0

# Generated at 2022-06-13 11:54:17.448262
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = FakeResult(1, 'Error')

# Generated at 2022-06-13 11:54:19.079072
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    obj = CallbackModule()
    assert obj
    assert isinstance(obj, CallbackModule)

# Generated at 2022-06-13 11:54:25.709303
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    # Declare an instance of class CallbackModule and set the Ansible options
    obj = CallbackModule()

    # Declare a mock object which will simulate a player object returned by ansible
    class MockResult():
        def __init__(self):
            self._host = MockHost()
            self._result = {'exception':'An exception occured during task execution.'}

    # Declare a mock object which will simulate a player object returned by ansible
    class MockHost():
        def __init__(self):
            self.get_name = lambda: "mock_host"

    # Call the tested method with a mock object
    obj.v2_runner_on_failed(MockResult())
    # Check the result
    assert len(obj._display.display.call_args_list) == 1


# Generated at 2022-06-13 11:54:35.298512
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    '''
    This function demonstrates the unit test for method v2_runner_on_failed
    of class CallbackModule.

    Parameters
    ----------
    result : Unknown
        The result is unknown, therefore no type annotation is made.

    ignore_errors : bool, optional
        The default value is False.

    Returns
    -------
    None

    '''
    result = None
    ignore_errors = False
    unknown = CallbackModule.v2_runner_on_failed(result, ignore_errors)
    assert unknown is None


# Generated at 2022-06-13 11:54:40.395806
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule().v2_runner_on_failed("result", "ignore_errors") is None
    assert CallbackModule().v2_runner_on_ok("result") is None
    assert CallbackModule().v2_runner_on_skipped("result") is None
    assert CallbackModule().v2_runner_on_unreachable("result") is None

# Generated at 2022-06-13 11:55:07.561883
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible.utils.display import Display
    from ansible.utils.color import stringc
    from ansible.vars import AnsibleVars
    display = Display()
    options = AnsibleVars()
    oneline = CallbackModule(display, options)

    assert oneline is not None
    assert oneline.verbosity == 0
    assert oneline._display == display
    assert oneline._options == options
    assert oneline.disabled is False
    assert oneline.FILTER_COUNT == 0
    assert oneline.FILTER_ALL == 1
    assert oneline.FILTER_REPLACEMENTS == 2
    assert oneline.FILTER_FAILED_HOSTS == 3
    assert oneline.FILTER_UNDEFINED_VARS == 4
    assert oneline.FILTER_UNSAFE_V

# Generated at 2022-06-13 11:55:09.521229
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cb = CallbackModule()
    assert(cb)


# Generated at 2022-06-13 11:55:10.533354
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule(display=object)

# Generated at 2022-06-13 11:55:20.603785
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    # Lets create an object of CallbackModule to check whether it is constructed
    # correctly or not

    x = CallbackModule()
    assert x.CALLBACK_TYPE == 'stdout'
    assert x.CALLBACK_VERSION == 2.0
    assert x.CALLBACK_NAME == 'oneline'

    # Lets test the v2_runner_on_failed() method
    # First we need to create a result object and pass it to v2_runner_on_failed


# Generated at 2022-06-13 11:55:32.088541
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback import CallbackBase
    from ansible import constants as C
    callback = CallbackModule()
    result = CallbackBase()
    result._host = CallbackBase()
    result._host.get_name = lambda: "test_host"
    result._result = {
        "changed": False,
    }
    result._task = CallbackBase()
    result._task.action = "action"

    with patch('ansible.plugins.callback.CallbackBase.display', return_value=None) as mock_display:
        callback.v2_runner_on_ok(result)
        mock_display.assert_called_once()
        args, kwargs = mock_display.call_args


# Generated at 2022-06-13 11:55:38.299151
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    hostname = 'test-host'
    result = {'exception': 'test-exception'}
    cb = CallbackModule()
    expected = "test-host | An exception occurred during task execution. To see the full traceback, use -vvv. The error was: test-exception"
    actual = cb.v2_runner_on_failed('result', 'ignore_errors=False')
    assert expected == actual


# Generated at 2022-06-13 11:55:41.726491
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cb = CallbackModule()
    assert cb.CALLBACK_VERSION == 2.0
    assert cb.CALLBACK_TYPE == 'stdout'
    assert cb.CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:55:42.843900
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    #TODO
    pass

# Generated at 2022-06-13 11:55:48.265584
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    
    # Test case 1
    print("Test case 1: ")
    test = CallbackModule()
    test.v2_runner_on_unreachable("test1")
    test.v2_runner_on_skipped("test2")
    test.v2_runner_on_ok("test3")
    test.v2_runner_on_failed("test4")

    # Test case 2
    print("Test case 2: ")

test_CallbackModule()

# Generated at 2022-06-13 11:55:49.436642
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    CallbackModule("test").v2_runner_on_ok("test")

# Generated at 2022-06-13 11:56:24.982912
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # arrange
    import sys
    import unittest
    from contextlib import contextmanager
    from io import StringIO
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import callback_loader

    TEST_CASE = ['TaskResult', 'Block', 'ImmutableDict']

# Generated at 2022-06-13 11:56:34.176910
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import sys
    import unittest

    class MockDisplay(object):
        def display(self, msg, color=None):
            sys.stdout.write("MOCK MSG: " + msg + "\n")

    class MockHost(object):
        def get_name(self):
            return "Test.Host"

    class MockResult(object):
        def __init__(self, changed, task):
            self._result = {'changed':changed}
            self._task = task

        def __getattr__(self, attr):
            return self._result[attr]

    class MockTask(object):
        def __init__(self, action):
            self.action = action

    class TestOnelineCallbackModule(unittest.TestCase):
        def setUp(self):
            self.display = MockDisplay()
            self

# Generated at 2022-06-13 11:56:42.241671
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import unittest
    
    class TestDisplay():
        def display(self, str, color):
            print(str)
    
    test = CallbackModule(TestDisplay())
    test.v2_runner_on_ok({'changed': False, '_host':{'get_name': lambda : 'localhost'},'_result':{'invocation':{'module_name':'shell','module_args':'ls'}, 'stdout':'stdout'}})


if __name__ == '__main__':
    test_CallbackModule_v2_runner_on_ok()

# Generated at 2022-06-13 11:56:52.454745
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    """
    Test method v2_runner_on_failed of class CallbackModule
    """
    import pymongo

    vm = VirtualMachine("localhost")
    vm.set_libvirt_guest_agent("/var/lib/libvirt/qemu/libvirt-guest-agent-test.so")
    vm.start()
    callbackmodule = CallbackModule()
    # Test with pymongo client because it is the only package that can use libvirt-guest-agent-test plugin
    result = Result(host=Host(name="localhost"), task=Task(),
                    result={"exception": "an exception", "module_stderr": "stderr"})
    callbackmodule.v2_runner_on_failed(result)
    vm.destroy()



# Generated at 2022-06-13 11:57:00.844013
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import load_extra_vars
    from ansible.plugins.loader import callback_loader
    import ansible
    import os

    callback = callback_loader.get('oneline')()
    options = ansible.context.CLIARGS
    loader = DataLoader()

# Generated at 2022-06-13 11:57:12.250234
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():

    # Setup test object
    import mock
    import ansible.plugins.loader as plugin_loader
    mock_display = mock.Mock()
    mock_display.display = mock.Mock()
    cb = plugin_loader.get_callback_plugin('oneline')
    cb.set_options()
    cb.set_runner(mock.Mock())
    cb._display = mock_display

    # Verify with both 'changed' and 'invocation' results
    for changed in [True, False]:
        result = mock.Mock()
        result.is_changed.return_value = changed
        result.get_task_name.return_value = 'foo'
        cb.v2_runner_on_ok(result)

# Generated at 2022-06-13 11:57:12.699336
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    pass

# Generated at 2022-06-13 11:57:14.649781
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    callback = CallbackModule()
    assert isinstance(callback, CallbackModule)
    assert isinstance(callback, CallbackBase)


# Generated at 2022-06-13 11:57:15.751327
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    x = CallbackModule
    assert x is not None

# Generated at 2022-06-13 11:57:25.649375
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback.oneline import CallbackModule
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    from ansible.plugins.callback import CallbackBase
    from ansible.utils.sentinel import Sentinel
    from ansible.parsing.yaml.dumper import AnsibleDumper

    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

# Generated at 2022-06-13 11:58:54.901934
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import __builtin__ as builtins
    builtins.__dict__['_'] = lambda x: 'test_string'

    c = CallbackModule()
    c.set_options(verbosity=0)
    c.v2_runner_on_failed(result=set())

    c = CallbackModule()
    c.set_options(verbosity=3)
    c.v2_runner_on_failed(result=set())


# Generated at 2022-06-13 11:58:56.009935
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    pass


# Generated at 2022-06-13 11:58:56.936922
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    pass

# Generated at 2022-06-13 11:58:57.777290
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    callback = CallbackModule()
    assert callback is not None

# Generated at 2022-06-13 11:59:06.697838
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.plugins.callback import CallbackBase

    class MockDisplay(CallbackBase):
        def __init__(self):
            self.verbosity = None
            self.data = []
        def display(self, data, color):
            self.data.append(data)

    class MockTask:
        def __init__(self):
            self.action = None

    class MockResult:
        def __init__(self):
            self.host = MockHost()
            self.task = MockTask()
            self._result = {}

    class MockHost:
        def __init__(self):
            self.name = None
        def get_name(self):
            return self.name

    # Test for stdout
    display = MockDisplay()
    display.verbosity = 3  # minimal verbosity
    result = MockResult()

# Generated at 2022-06-13 11:59:14.863866
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.utils.display import Display
    from ansible.plugins.callback.default import CallbackModule as callbackm

    display = Display()
    callback = callbackm(display)


# Generated at 2022-06-13 11:59:21.213488
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    class _CallbackModule(CallbackModule):
        # Need to export _dump_results to make it available for unit testing
        def _dump_results(self, result, indent=4):
            return CallbackModule._dump_results(self, result, indent)
    import ansible.utils
    import ansible.constants
    import ansible.plugins
    import ansible.utils.encrypt

    # Init mock objects
    my_display = ansible.utils.display.Display()
    my_stdout = ansible.utils.encrypt.get_stdout(None, my_display)
    my_stdout.verbosity = 1
    module = _CallbackModule(stdout=my_stdout)

    # Init vars
    ansible.constants.DEFAULT_LOCAL_TMP = "test/test"

# Generated at 2022-06-13 11:59:28.500860
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cb = CallbackModule()


# Generated at 2022-06-13 11:59:34.072230
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    c = CallbackModule()

    c.CALLBACK_VERSION = 2.0
    assert c.CALLBACK_VERSION == 2.0

    c.CALLBACK_TYPE = 'stdout'
    assert c.CALLBACK_TYPE == 'stdout'

    c.CALLBACK_NAME = 'oneline'
    assert c.CALLBACK_NAME == 'oneline'



# Generated at 2022-06-13 11:59:34.651228
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    return CallbackModule()