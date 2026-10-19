

# Generated at 2022-06-13 11:51:39.733802
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():

    from ansible.plugins.callback import CallbackBase
    from ansible import constants as C
    from ansible import configuration as C

    class CallbackModule(CallbackBase):

        '''
        This is the default callback interface, which simply prints messages
        to stdout when new callback events are received.
        '''

        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'minimal'

        def v2_on_file_diff(self, result):
            if 'diff' in result._result and result._result['diff']:
                self._display.display(self._get_diff(result._result['diff']))

    args = {'type': 'stdout', 'also_log_to_stdout': True, 'display_callback_events': True}
    display = Callback

# Generated at 2022-06-13 11:51:47.638729
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    class Host():
        def get_name():
            return 'localhost'
    class Result():
        def __init__(self, _host):
            self._host = _host
        def _result(self):
            return dict(changed=True)
    class Task():
        def action():
            return 'shell'
    display = dict()
    display['display'] = print
    c = CallbackModule(display)
    result = Result(Host)
    result._task = Task()
    c.v2_runner_on_ok(result)
    result._result = dict(changed=False)
    c.v2_runner_on_ok(result)
    result._task.action = lambda: 'debug'
    result._result = dict(changed=True)
    c.v2_runner_on_ok(result)
   

# Generated at 2022-06-13 11:51:50.427924
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    v2_runner_on_failed = CallbackModule.v2_runner_on_failed
    assert (v2_runner_on_failed(result, ignore_errors=False))

# Generated at 2022-06-13 11:51:54.059799
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    callback = CallbackModule()
    assert callback
    assert callback.CALLBACK_VERSION == 2.0
    assert callback.CALLBACK_TYPE == 'stdout'
    assert callback.CALLBACK_NAME == 'minimal'

# Generated at 2022-06-13 11:51:59.137745
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    cb = CallbackModule()

    # Verify if the method gets called without error
    cb.v2_on_file_diff(Result)

    # Verify if the method gets called without error
    result = Result()
    cb.v2_on_file_diff(result)

    # Verify if the method gets called without error
    result._result = {'diff': []}
    cb.v2_on_file_diff(result)



# Generated at 2022-06-13 11:52:09.776546
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # create CallbackModule object (mock)
    callback = CallbackModule()
    # get mock module
    import mock
    # use mock to mock method display of object callback, then return mock object
    callback.display = mock.Mock(return_value="Mock object")
    # create result object
    import ansible.vars.hostvars
    import ansible.executor.task_result
    class HostVars:
        def __init__(self):
            super(HostVars, self).__init__()
            self.hostname = "localhost"
    result = ansible.vars.hostvars.HostVars()
    result._result = ansible.executor.task_result.TaskResult()

# Generated at 2022-06-13 11:52:11.548210
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cb = CallbackModule()
    assert cb

# Generated at 2022-06-13 11:52:13.080372
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert 'Action' == 'v2_runner_on_ok'

# Generated at 2022-06-13 11:52:23.449169
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import sys
    sys.path.append('ansible')
    sys.argv = ['ansible', '-m', 'command', '-a', 'ls', 'ubuntu']
    from ansible.cli import CLI
    from ansible.inventory.manager import InventoryManager
    import json

    ansible_cli = CLI(args={'module_path': '/usr/local/lib/python2.7/dist-packages/ansible/modules/', 'connection': 'local'})
    inventory = InventoryManager(
        sources=[{'name': 'test', 'hosts': ['ubuntu'], 'vars': {'ansible_user': 'ubuntu', 'ansible_password': 'ubuntu'}}]
    )
    ansible_cli.options.inventory = inventory
    cb = CallbackModule()
    ansible_cli.run()

    result

# Generated at 2022-06-13 11:52:34.739732
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():

    """
    Test for method v2_runner_on_ok of class CallbackModule
    """

    from ansible.plugins.callback import CallbackModule

    my_obj = CallbackModule()

    from collections import namedtuple

    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_result import TaskResult
    TaskResult._fields=('_task', '_host', '_result')

    result = TaskResult(
        _task = 'test_task',
        _host = 'test_host',
        _result = {
            'changed': True,
            'stdout': 'test_stdout',
            'stderr': 'test_stderr',
            'msg': 'test_msg'
        }
    )

    my_obj.v2_runner_on_ok

# Generated at 2022-06-13 11:52:48.178777
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.plugins.callback import CallbackBase
    from ansible import constants as C

    cb = CallbackBase()
    cb._display = C.Display()
    cb._dump_results = lambda x,y: ""
    cb._handle_exception = lambda x: ""
    cb._handle_warnings = lambda x: ""
    
    result = lambda: None # mock object
    result._task = lambda: None
    result._task.action = "module_name"
    result._host = lambda: None
    result._host.get_name = lambda: "localhost"
    result._result = {
        "warnings": "some_warnings",
        "msg": "some_msg"
    }

    cb.v2_runner_on_failed(result) # should not raise error

    import sys

# Generated at 2022-06-13 11:52:50.608987
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cb = CallbackModule()
    cb.v2_runner_on_failed('result', ignore_errors=False)

# Generated at 2022-06-13 11:53:01.061387
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    def fake_display(buf, color):
        return True

    def fake_handle_exception(result):
        return True

    def fake_handle_warnings(result):
        return True

    c = CallbackModule()
    c._display = fake_display
    c._handle_exception = fake_handle_exception
    c._handle_warnings = fake_handle_warnings

    result = _Result()
    result._result = {'rc': 1, 'stdout': 'stdout', 'stderr': 'stderr', 'msg': 'msg'}
    result._task = _Task()
    result._task.action = 'action'
    result._host = _Host()
    result._host.get_name = lambda: 'hostname'
    c.v2_runner_on_failed(result)



# Generated at 2022-06-13 11:53:08.919811
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.module_utils._text import to_text

    import os
    import sys
    import textwrap
    import json

    fake_result = dict()
    fake_result["_ansible_parsed"] = True
    fake_result["changed"] = False
    fake_result["failed"] = False
    fake_result["rc"] = 0
    fake_result["stderr"] = ""
    fake_result["stdout"] = "hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha"

# Generated at 2022-06-13 11:53:19.961771
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():

    result = {
        '_host': {
            'get_name': lambda: 'localhost',
        },
        '_result': {
            'stdout': '',
            'stderr': '',
            'msg': '',
            'changed': True,
        }
    }

    callback_module = CallbackModule()

# Generated at 2022-06-13 11:53:27.514670
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    callback = CallbackModule()
    result = {
        "changed": True,
        "cmd": "echo Hello World",
        "delta": "0:00:00.008813",
        "end": "2017-08-11 16:41:00.790589",
        "failed": True,
        "invocation": {
            "module_args": "echo Hello World",
            "module_complex_args": {},
            "module_name": "command"
        },
        "rc": 2,
        "start": "2017-08-11 16:41:00.781776",
        "stderr": "bash: line 1: echo: command not found",
        "stdout": "",
        "stdout_lines": [],
        "warnings": []
    }
    host = "ubuntu"

# Generated at 2022-06-13 11:53:29.458048
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cb = CallbackModule()
    assert cb is not None

# Generated at 2022-06-13 11:53:39.049323
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    from ansible.playbook.play_context import PlayContext

    class FakeHost(object):
        def vars_as_redacted(self):
            return {}

    class FakeResult(object):
        def __init__(self):
            self._host = FakeHost()
            self._result = {
                'diff': '',
            }

    try:
        import __builtin__ as builtins  # python2
    except:
        import builtins  # python3

    class FakeDisplay(object):
        def __init__(self):
            self.buf = ''

        def display(self, msg, color=None):
            self.buf += msg + '\n'

    orig_display = CallbackModule._display
    class_inst = CallbackModule()
    class_inst.set_options({'diff': False})


# Generated at 2022-06-13 11:53:42.281742
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    callback = CallbackModule()
    assert(callback.CALLBACK_VERSION == 2.0)
    assert(callback.CALLBACK_TYPE   == 'stdout')
    assert(callback.CALLBACK_NAME   == 'minimal')

# Generated at 2022-06-13 11:53:45.566989
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    callbackModule = CallbackModule()
    assert callbackModule.CALLBACK_TYPE == 'stdout'
    assert callbackModule.CALLBACK_VERSION == 2.0

# Generated at 2022-06-13 11:54:01.069060
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    """
    Test the output when the callback plugin is used with the action 'ping'
    which is not in the CALLBACK_ACTION_SKIPPED_LIST.
    """
    # Generate a result with a fake task and a fake host for the test
    result = type('', (object,), {'_host': {'get_name': lambda: 'host1'}, '_task': {'action': 'ping'}})()
    # Add a result to the result in order to be able to test it

# Generated at 2022-06-13 11:54:11.358484
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # Setup
    from io import StringIO
    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 4
    display.set_output_stream(StringIO())

    # Test
    test = CallbackModule()
    test._display = display
    test.v2_on_file_diff({
        '_result': {
            'changed': True,
            'diff': 'diff --git a/x b/x\nindex xx..xx 100644\n--- a/x\n+++ b/x\n@@ -1,1 +1,1 @@\n-x\n+y\n'
        }
    })

    # Verify

# Generated at 2022-06-13 11:54:21.247721
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    import json
    import mock
    import os

    # make sure env vars don't interfere with result
    if 'GIT_DIFF' in os.environ: del os.environ['GIT_DIFF']
    if 'HG_DIFF' in os.environ: del os.environ['HG_DIFF']

    # Set up the objects we need to call our method under test
    class Config:
        pass
    config = Config()
    config.color = True

    # Set up the objects we need to call our method under test
    mock_result = mock.MagicMock()

# Generated at 2022-06-13 11:54:23.283728
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    obj = CallbackModule()
    assert obj


# Generated at 2022-06-13 11:54:30.081398
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # make an instance of class
    testClass = CallbackModule()
    # make a mock object 'result' for argument of the method
    result = {'stdout': "I change this file!", 'stderr': '', 'rc': 1, 'msg': ''}
    # call the method passing the mock object as argument
    testClass.v2_runner_on_failed(result)
    # make another mock object for argument
    result = {'stdout': "", 'stderr': '', 'rc': 0, 'msg': ''}
    # call the method passing the mock object as argument
    testClass.v2_runner_on_failed(result)
    # make another mock object for argument
    result = {'stdout': "", 'stderr': '', 'rc': 2, 'msg': ''}
    # call the method

# Generated at 2022-06-13 11:54:42.896912
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import re
    import sys
    import unittest
    import json
    # Stub used to replace the AnsibleModule class
    class Stub(object):
        def __init__(self):
            pass
        def fail_json(self, *a, **kw):
            self.exception = kw['err']
        def exit_json(self, *a, **kw):
            pass
    class TestDisplay(object):
        def __init__(self, str_out, color):
            self.str_out = str_out
            self.color = color
        def display(self, msg, color):
            pass
    class Test(unittest.TestCase):
        '''
        TestCase for class CallbackModule
        '''
        def setUp(self):
            self.callback = CallbackModule()

# Generated at 2022-06-13 11:54:47.939367
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    from ansible.module_utils.common.collections import ImmutableDict

    cb = CallbackModule()

    result = ImmutableDict(diff={u'after': u'', u'before': u'', u'before_header': u'', u'after_header': u''})
    cb.v2_on_file_diff(result)


# Generated at 2022-06-13 11:54:54.700161
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    class TestFailedAnsibleTask(object):
        def __init__(self):
            self.action = 'setup'

    class TestFailedAnsibleHost(object):
        def __init__(self):
            self.name = 'test_host'

        def get_name(self):
            return self.name

    class TestFailedAnsibleResult(object):
        def __init__(self, result, task):
            self._result = result
            self._result['msg'] = 'Task failed'
            self._task = task
            self._host = TestFailedAnsibleHost()

    class TestFailedAnsibleModule(CallbackModule):
        def __init__(self, display):
            super(TestFailedAnsibleModule, self).__init__(display)
            self._display = display

   

# Generated at 2022-06-13 11:55:02.258409
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    c = CallbackModule()
    c._display = Display()
    task = Task()
    host = Host()
    task._task.action = 'get_url'
    result = Result()
    result._host = host
    result._result = {'changed': True}
    result._task = task
    c.v2_runner_on_ok(result)
    assert c._dump_results(result._result) == "{\n    \"changed\": true\n}"
    assert c._display.displayed.pop() == "\x1b[32mhost | SUCCESS => {\n    \"changed\": true\n}\x1b[0m"
    result._result = {'changed': False}
    c.v2_runner_on_ok(result)

# Generated at 2022-06-13 11:55:12.560824
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
	
	import os
	import sys
	sys.path.append(os.path.dirname(os.path.dirname(__file__)))
	from ansible.plugins.callback.minimal import CallbackModule
	
	import json
	from ansible.parsing.dataloader import DataLoader

	# Creating CallbackModule instance
	callbackModule = CallbackModule()
	
	# Creating "result" object which is required to be passed as an input to the method
	result = type('', (object,), {})()
	result._host = type('', (object,), {})()
	result._host.get_name = lambda: "test-host"
	result._result = {'changed': False}

	callbackModule.v2_runner_on_ok(result)

# Generated at 2022-06-13 11:55:29.917609
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    mod = CallbackModule()
    assert len(mod.CALLBACK_NAME) > 0
    assert mod.CALLBACK_VERSION == 2.0
    assert mod.CALLBACK_TYPE == 'stdout'

# Generated at 2022-06-13 11:55:40.214948
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # prepare
    from ansible import context
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback import CallbackBase
    from ansible.plugins.callback.default import CallbackModule
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="hosts")
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 11:55:43.512049
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cb = CallbackModule()
    assert cb.CALLBACK_VERSION == 2.0
    assert cb.CALLBACK_TYPE == 'stdout'
    assert cb.CALLBACK_NAME == 'minimal'


# Generated at 2022-06-13 11:55:44.768586
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    isinstance(CallbackModule(), CallbackModule)

# Generated at 2022-06-13 11:55:52.145455
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    callback = CallbackModule()
    result = {'_result': {'stdout': 'Test stdout', 'stderr': 'Test stderr', 'rc': 1, 'msg': 'Test message'}}
    result_with_module_stderr = {'_result': {'stdout': 'Test stdout', 'stderr': 'Test stderr', 'rc': 1, 'module_stderr': 'Test message', 'msg': 'Test message'}}
    result_with_module_stderr_null_stderr = {'_result': {'stdout': 'Test stdout', 'stderr': '', 'rc': 1, 'module_stderr': 'Test message', 'msg': 'Test message'}}

# Generated at 2022-06-13 11:55:57.482188
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # initialization for usage of v2_runner_on_ok
    callback = CallbackModule()
    # first, we create a dictionary to substitute AnsibleTask in order to
    # call v2_runner_on_ok without AnsibleTask and result._task.action
    # and then we create an object to substitute AnsibleTask object
    result_action = {}
    result_action['action'] = "command"
    result_action['default_action'] = "command"
    AnsibleTask = type('AnsibleTask', (), result_action)
    # second, we create a dictionary to simulate the object AnsibleHost
    # and then we create an object to substitute AnsibleHost object
    result_host = {}
    result_host['get_name'] = lambda: "localhost"
    AnsibleHost = type('AnsibleHost', (), result_host)

# Generated at 2022-06-13 11:56:02.482963
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    obj = CallbackModule()

    # Assert instance object
    assert isinstance(obj, CallbackModule)
    assert isinstance(obj, CallbackBase)
    assert obj.CALLBACK_TYPE == 'stdout'
    assert obj.CALLBACK_NAME == 'minimal'
    assert obj.CALLBACK_VERSION == 2.0
    assert obj._display.verbosity == 0

# Generated at 2022-06-13 11:56:11.074106
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    import unittest
    import sys

    class Test_v2_on_file_diff(unittest.TestCase):

        @classmethod
        def setUpClass(self):
            # remove any possible output from tests
            if len(sys.stdout.getvalue()) > 0:
                sys.stdout.truncate(0)
                sys.stdout.seek(0)
            if len(sys.stderr.getvalue()) > 0:
                sys.stderr.truncate(0)
                sys.stderr.seek(0)

        def test_v2_on_file_diff_output(self):
            myCallbackModule = CallbackModule()

# Generated at 2022-06-13 11:56:16.140053
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    module = CallbackModule()
    assert module.CALLBACK_VERSION == 2.0
    assert module.CALLBACK_TYPE == 'stdout'
    assert module.CALLBACK_NAME == 'minimal'


if __name__ == "__main__":
    test_CallbackModule()

# Generated at 2022-06-13 11:56:17.815202
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():

    # Tests if method v2_runner_on_ok can be called
    cb = CallbackModule()
    cb.v2_runner_on_ok("")


# Generated at 2022-06-13 11:56:52.404181
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_executor import TaskExecutor
    from ansible.report.recap_preset import RecapPreset
    
    cb = CallbackModule()
    host, result = MockHost(), TaskResult(host=MockHost(), task=MockTask())
    result._result['changed'] = True
    
    # Inject the callback into the TaskExecutor
    te = TaskExecutor(MockPlayContext())
    te._tqm._stdout_callback = cb
    te._tqm._stdout_silent_cb = cb
    
    returnable = te._tqm.RUN_OK

    # Run the callback method
    cb.v2

# Generated at 2022-06-13 11:56:57.390554
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    
    # Create an instance of class CallbackModule
    ansible_callback = CallbackModule()

    # Assert that function v2_on_file_diff exists
    assert hasattr(ansible_callback, "v2_on_file_diff") == True

    # Assert that the v2_on_file_diff is a function
    assert callable(getattr(ansible_callback, "v2_on_file_diff")) == True

# Generated at 2022-06-13 11:57:07.078489
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    c = CallbackModule()
    result = "this is a test"

    result_dict = {'diff': result}
    result_ok = {'diff': None}

    result_empty = {}

    # test with change
    if c._display.display(c._get_diff(result_dict['diff'])) == "---\n+++\n@@ -1 +1 @@\n-this is a test\n+this is a test\n\\ No newline at end of file\n":
        assert True
    else:
        assert False

    # test without change
    if c._get_diff(result_ok['diff']) is None:
        assert True
    else:
        assert False

    # test empty diff
    if c._get_diff(result_empty['diff']) is None:
        assert True

# Generated at 2022-06-13 11:57:07.667394
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    pass

# Generated at 2022-06-13 11:57:15.152779
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible import context

    context._init_global_context(load_plugins=False)
    # set our global options
    context._init_global_context()

    # load plugins
    from ansible.plugins import module_loader
    context.CLIARGS = module_loader.ArgumentParser('')
    context.CLIARGS = context.CLIARGS.parse_args([''])

    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 1


# Generated at 2022-06-13 11:57:17.376500
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
	clbkmod_object = CallbackModule()
	assert hasattr(clbkmod_object, '_command_generic_msg')

# Generated at 2022-06-13 11:57:27.157909
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    task = "set_fact"
    host = "localhost"
    action = "TASK: set_fact"
    result = {"_ansible_no_log": False, "_ansible_verbose_always": True, "changed": False, "failed": True, "msg": "ERROR! 'ansible_date_time.epoch' is undefined", "stderr": "", "stdout": ""}
    ignore_errors = False
    ex = Exception("boom")

# Generated at 2022-06-13 11:57:33.887244
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    cb = CallbackModule()
    result = MockResult(MockHost('test_host'), MockTask(MockActionModule('test_action')), ({'changed': 'test_changed'}))
    assert cb.v2_runner_on_ok(result) == "\ntest_host | SUCCESS => {\n    \"changed\": \"test_changed\"\n}"
    cb = CallbackModule()
    result = MockResult(MockHost('test_host'), MockTask(MockActionModule('test_action')), {'changed': False})
    assert cb.v2_runner_on_ok(result) == "\ntest_host | SUCCESS => {}"

# Generated at 2022-06-13 11:57:41.401194
# Unit test for method v2_on_file_diff of class CallbackModule

# Generated at 2022-06-13 11:57:46.390667
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible.plugins.callback import CallbackBase
    from ansible import constants as C
    my_test = CallbackModule()
    assert my_test.CALLBACK_VERSION == 2.0
    assert my_test.CALLBACK_TYPE == 'stdout'
    assert my_test.CALLBACK_NAME == 'minimal'


# Generated at 2022-06-13 11:59:05.229560
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    cbm = CallbackModule()
    assert cbm._dump_results == CallbackBase._dump_results

# Generated at 2022-06-13 11:59:11.020737
# Unit test for constructor of class CallbackModule

# Generated at 2022-06-13 11:59:21.142973
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    class Result:
        def __init__(self, name=None, _host=None, _result=None, _result_action=None):
            self._host = Host(name)
            self._result = _result
            self._task = _result_action
            pass
        pass
    class Host:
        def __init__(self, name=None):
            self.name = name
            pass
        def get_name(self):
            return self.name
        pass

    ret = dict(
        stdout_lines=["asdfa","asd"]
    )
    result = Result(name="some_host", _result=ret, _result_action="command")
    cb = CallbackModule()
    cb.v2_runner_on_failed(result, ignore_errors=False)



# Generated at 2022-06-13 11:59:21.907247
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pass

# Generated at 2022-06-13 11:59:24.203386
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    tag = "[test_CallbackModule_v2_runner_on_ok]"

    cb = CallbackModule()
    print(tag + str(cb.v2_runner_on_ok))


# Generated at 2022-06-13 11:59:26.470354
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    b = CallbackModule()
    b.__del__()

# Generated at 2022-06-13 11:59:36.615703
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    # Preparing objects
    display = DummyDisplay()
    result  = DummyResult()
    result._result = dict()

    context = dict(
        role_path = '',
        diff = 'diff content'
    )
    task = Task()
    play = Play.load(dict(
        context = PlayContext(),
        hosts = 'localhost',
        tasks = []
    ))

    result._task = task
    result._task.action = 'replace'
    result._task._uuid = 'test'
    result._host = DummyHost()
    result._host.get_name.return_value = 'localhost'

    callback = CallbackModule()
   

# Generated at 2022-06-13 11:59:39.157618
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cb = CallbackModule()
    result = MockResult()
    cb.v2_runner_on_failed(result)


# Generated at 2022-06-13 11:59:40.090998
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule


# Generated at 2022-06-13 11:59:45.531003
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    callback = CallbackModule()
    callback._clean_results = lambda results, action: results
    callback._dump_results = lambda results, indent: repr(results)
    callback._display = lambda msg, color: print(msg)
    
    result = _MockResult()
    result._result = {
        'warnings': '',
        'changed': True,
    }
    
    callback.v2_runner_on_ok(result)
