

# Generated at 2022-06-13 11:51:35.833714
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    import os

    # Create a minimal Ansible config
    ansible_cfg = open('ansible.cfg', 'w')
    ansible_cfg.write('[defaults]\n')
    ansible_cfg.write('callback_whitelist = minimal\n')
    ansible_cfg.close()

    # Create a minimal Ansible inventory
    inventory = open('hosts', 'w')
    inventory.write('[all]\n')
    inventory.write('localhost ansible_connection=local\n')
    inventory.close()

    # Create a minimal task file
    tasks = open('tasks.yml', 'w')
    tasks.write('---\n')
    tasks.write('- name: Test ansible callback minimal v2_on_file_diff\n')
    tasks.write('  copy:\n')
   

# Generated at 2022-06-13 11:51:37.835518
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Tests if it returns True for a fresh install
    assert CallbackModule.v2_runner_on_ok('ok') == True

# Generated at 2022-06-13 11:51:44.261513
# Unit test for method v2_on_file_diff of class CallbackModule

# Generated at 2022-06-13 11:51:45.381862
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    return True

# Generated at 2022-06-13 11:51:56.273275
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Setup
    result = type('obj', (object,), dict(
        _result = dict(
            changed = True,
            ansible_job_id = "job_id",
            ansible_facts = dict(
                one = "1",
                two = "2"
            )
        ),
        _host = type('obj', (object,), dict(
            get_name = lambda self: "host_name"
        ))(),
        _task = type('obj', (object,), dict(
            action = "MODULE_NO_JSON"
        ))(),
    ))
    instance = CallbackModule()

    # Exercise
    instance.v2_runner_on_ok(result)

    # Verify
    assert instance.v2_runner_on_ok == CallbackModule.v2_runner_on_ok

# Generated at 2022-06-13 11:52:08.533270
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    import systemd.daemon
    import threading
    import os
    import sys
    import tempfile

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a file in the temporary directory
    file = tempfile.NamedTemporaryFile(dir=tmpdir, delete=False)

    # Add some content to the file

# Generated at 2022-06-13 11:52:15.346361
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    class TestClass:
        def __init__(self):
            self.name = 'test_host'
    cm = CallbackModule()
    t = TestClass()
    result = TestClass()
    result.changed = True
    result._result = {}
    result._result['stdout'] = "stdout"
    result._host = t
    result._task = t
    result._task.action = 'shell'
    cm.v2_runner_on_ok(result)
    par = result._result['stdout'].rstrip()
    exp = "test_host | CHANGED => {\n    \"stdout\": \"stdout\"\n}"
    assert par == exp

# Generated at 2022-06-13 11:52:25.065157
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible import context
    from ansible.cli.playbook import PlaybookCLI
    from ansible.playbook import Playbook
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils._text import to_text
    from ansible.plugins.callback import CallbackBase
    from ansible.module_utils.common._collections_compat import Mapping


# Generated at 2022-06-13 11:52:35.968075
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    """Test method v2_runner_on_ok of class CallbackModule."""

    host = {'name': 'test-host'}
    task = {'action': 'my_action'}
    result = {
        'invocation': {
            'module_name': 'custom',
            'module_args': '''{"foo":"bar"}''',
            },
        'module_name': 'custom',
        'module_args': '{"foo":"bar"}',
        'changed': True,
    }

    callback = CallbackModule()
    callback._dump_results = lambda obj, indent=None : str(obj)
    callback._clean_results = lambda obj, action: None
    callback._handle_warnings = lambda obj: None
    callback._display = MockDisplay()


# Generated at 2022-06-13 11:52:43.683582
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    mock_result = TestResult()
    mock_result._task = TestTask()
    mock_result._task.action = 'test_action'
    mock_result._result = {
        'changed': True,
        'failed': False,
        'rc': 4,
        'stderr': 'This is a test error',
        'stdout': 'This is a test output',
        'msg': 'This is a test message'
    }
    mock_result._host = TestHost()
    mock_result._host.get_name.return_value = "localhost"
    mock_display = TestDisplay()

    mod = CallbackModule()
    mod.set_options(task_display_enabled=True)
    mod._display = mock_display

    mod.v2_runner_on_failed(mock_result)

# Generated at 2022-06-13 11:52:51.974812
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    result = type('result', (object,), {'_result': {
        'changed': False,
        'stdout': 'output',
        'stdout_lines': 'output lines',
    },
    '_task': type('task', (object,), {'action': 'command'})})()
    callback = CallbackModule()
    callback.v2_runner_on_ok(result)

# Generated at 2022-06-13 11:53:01.918259
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Set up test data
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    class Options:
        connection = "local"
        module_path = C.DEFAULT_MODULE_PATH
        module_name = C.DEFAULT_MODULE_NAME
        forks = 1
        become = False
        become_method = 'sudo'
        become_user = 'root'
        check = False
        diff = False
        timeout=10
    options = Options()

    loader = DataLoader()

# Generated at 2022-06-13 11:53:09.541516
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    # pylint: disable=redefined-outer-name
    # pylint: disable=no-value-for-parameter
    # pylint: disable=unused-variable
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.utils.vars import load_extra_vars
    import sys

    results = []

    class TestCallbackModule(CallbackModule):
        def __init__(self):
            self.callback = TestCallbackModule()

        def v2_runner_on_failed(self, result, ignore_errors=False):
            results.append(result)

        def v2_runner_on_ok(self, result):
            results.append(result)


# Generated at 2022-06-13 11:53:13.350691
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    callback_module = CallbackModule()
    result = MockedRunnerResult()
    result.changed = True
    callback_module.v2_runner_on_ok(result)


# Generated at 2022-06-13 11:53:14.084532
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule()

# Generated at 2022-06-13 11:53:19.168054
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    test_result = dict([('changed', True), ('module_stderr', 'This is an error message')])
    c_callback = CallbackModule()
    display_string = c_callback.v2_runner_on_failed(test_result, ignore_errors=False)
    expected_string = "| FAILED! => "
    assert expected_string in display_string


# Generated at 2022-06-13 11:53:25.592212
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Arrange
    hosts = [{'name': 'test'}]
    results = {'changed': False, '_ansible_verbose_always': True, '_ansible_no_log': False}
    result = {'_host': {'get_name': lambda: 'test'}, '_result': results, '_task': {'action': None}}
    class Display(object):
        def display(self, msg, color=None):
            print(msg)
    callback = CallbackModule(display=Display())
    # Act
    callback.v2_runner_on_ok(result)
    # Assert



# Generated at 2022-06-13 11:53:31.599153
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    test_result = dict(
        _host=Host(name='test_host'),
        _task=dict(action=dict(name='debug')),
        _result=dict()
    )

    inv_data = dict(
        ungrouped=dict(
            hosts=dict(
                test_host=dict()
            )
        )
    )
    inventory = InventoryManager(loader=None, sources=inv_data)
    variable_manager = VariableManager(loader=None, inventory=inventory)

    callback_minimal_obj = CallbackModule()

# Generated at 2022-06-13 11:53:35.270471
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Declare objects of class CallbackModule
    c = CallbackModule()
    result = 'ok'
    c.v2_runner_on_ok(result)
    assert c.v2_runner_on_ok(result) == 'ok'


# Generated at 2022-06-13 11:53:40.828686
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    '''
    Unit test for method v2_runner_on_failed

    Test CallbackModule.v2_runner_on_failed().
    '''

    ##################################################
    # Preparation
    ##################################################

    ##################################################
    # Initialization of CallbackModule
    ##################################################
    test_module = CallbackModule()

    ##################################################
    # Initialization of parameters
    ###############################################
    test_result = 'test_result'
    test_ignore_errors = False

    ##############################
    # Call to the method:
    # we call the method from the class that we want to test
    ##############################
    test_module.v2_runner_on_failed(test_result, test_ignore_errors)

    ############################################
    # Check the results

# Generated at 2022-06-13 11:53:48.524492
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    assert True

# Generated at 2022-06-13 11:53:52.206761
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    print()
    print('#########################################################################################################')
    print('Unit test for method v2_runner_on_failed of class CallbackModule')
    print('#########################################################################################################')
    print()
    pass


# Generated at 2022-06-13 11:53:54.965896
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    callback = CallbackModule()
    assert callback.CALLBACK_NAME == 'minimal'
    assert callback.CALLBACK_TYPE == 'stdout'
    assert callback.CALLBACK_VERSION == 2.0

# Generated at 2022-06-13 11:53:55.543639
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pass

# Generated at 2022-06-13 11:54:03.842781
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import unittest
    from ansible.plugins.callback.minimal import CallbackModule
    from ansible.inventory.host import Host
    import ansible.constants as C
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    class TestCallbackModule(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_v2_runner_on_ok(self):
            output = []
            cb = CallbackModule()
            cb._display =  DummyDisplay()
            cb._display.display = append_output
            cb._dump_results = lambda x,y: "dump_results"
            cb._handle_warnings = lambda x: None
            cb._clean

# Generated at 2022-06-13 11:54:15.110483
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    class _display(object):
        def display(self, text, color):
            self.color = color
            self.text = text
            
    test_display = _display()
    test_cb = CallbackModule()
    test_cb._display = test_display
    test_result = type("result", (object,), {
                                            "color" : "color",
                                            "text" : "text",
                                            "_result" : type("_result", (object,), {
                                                                                    "diff" : "diff"
                                                                                    })
                                            })
    test_cb.v2_on_file_diff(test_result)
    
    assert test_result._result.diff == "diff"
    assert test_result.color == "color"
    assert test_result.text

# Generated at 2022-06-13 11:54:24.214968
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.plugins.callback import CallbackBase
    from ansible.plugins.callback import CallbackModule
    from ansible.utils.display import Display
    from collections import namedtuple
    import json

    my_display = Display()
    my_callback_module = CallbackModule(my_display)


# Generated at 2022-06-13 11:54:31.084039
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible_collections.notmintest.not_a_real_collection.plugins.callback import CallbackModule

    plugin = CallbackModule()
    plugin.set_options({'display_skipped_hosts': True})
    class MockResult:
        result = {"stdout": "some stdout"}
        action = ""
        host = ""
    plugin.v2_runner_on_failed(MockResult())


# Generated at 2022-06-13 11:54:37.147365
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Stub method object
    stub_result = StubResult()
    stub_result._host = None
    stub_result._result = 'FAILED'
    stub_result._task = None
    # Stub CallbackModule object
    stub_callback = CallbackModule()
    assert stub_callback.v2_runner_on_failed(stub_result) == None

# Generated at 2022-06-13 11:54:47.271879
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = {'_ansible_verbosity': 1, '_ansible_no_log': False, '_ansible_debug': False, '_ansible_diff': True, '_ansible_verbose_always': False, '_ansible_version': '2.4.2.0', 'invocation': {'module_args': {}}, 'changed': False, '_ansible_parsed': True, 'ansible_facts': {}, 'ansible_included_var_files': [], 'ansible_config_version': '3.0', 'ansible_failed_result': None}
    result['_ansible_parsed'] = True
    

# Generated at 2022-06-13 11:55:12.265855
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    '''
        This method tests the def v2_on_file_diff() of class CallbackModule.
        This is a method which prints the a diff if there is a diff else
        returns a message of no diff.
    '''
    class test_obj:
        class test_host:
            def get_name():
                return 'test.local'
        _host = test_host()

    result = {}
    result['diff'] = {'after': 'new', 'before': 'old', 'after_header': '', 'before_header': '', 'before_header': '+++ /Users/jake/python/Unit Test Project/ansible/plugins/callback/minimal.py\n'}

    self = CallbackModule()
    self._dump_results = test_dump_results
    self._display = test_obj
    self

# Generated at 2022-06-13 11:55:22.388137
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    diff_input1 = """diff -ruN 1.orig/file.txt 2.changed/file.txt
--- 1.orig/file.txt   2017-03-28 23:22:27.713289800 +0000
+++ 2.changed/file.txt    2017-03-28 23:22:27.757290000 +0000
@@ -1,4 +1,4 @@
-1. Line 1 of file 1.orig/file.txt
+1. Line 1 of file 1.changed/file.txt
 2. Line 2 of file 1.orig/file.txt
 3. Line 3 of file 1.orig/file.txt
 4. Line 4 of file 1.orig/file.txt"""


# Generated at 2022-06-13 11:55:30.885004
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    class FakeDisplay(object):
        def __init__(self, test):
            self.test = test
            self.display_messages = []

        def display(self, msg, **kwargs):
            self.display_messages.append(msg)

    class FakeTask(object):
        def __init__(self, action):
            self.action = action

    class FakeHost(object):
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    class FakeResult(object):
        def __init__(self, name, action, result):
            self._result = result
            self._host = FakeHost(name)
            self._task = FakeTask(action)


# Generated at 2022-06-13 11:55:38.180065
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    class Test_CallbackModule_v2_runner_on_ok():
        def __init__(self):
            self.results = []

        def display(self, msg, color=None):
            self.results.append(msg)

    test = CallbackModule()
    test._display = Test_CallbackModule_v2_runner_on_ok()

    test.v2_runner_on_ok({'_result': {}})

    assert test._display.results[0] == '| SUCCESS => {}'

# Generated at 2022-06-13 11:55:44.189047
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
  result = {'_task': {'action': 'shell'}, '_host': {'get_name': lambda: 'localhost'}}
  result['_result'] = {'failed': True, 'msg': 'FAILED!'}
  default_callback = CallbackModule()
  assert default_callback.v2_runner_on_failed(result) is None
  assert default_callback.v2_runner_on_failed(result, ignore_errors=True) is None


# Generated at 2022-06-13 11:55:51.891481
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    callback = CallbackModule()
    def _v2_runner_on_ok(result):
        """Call method v2_runner_on_ok of class CallbackModule """
        return callback.v2_runner_on_ok(result)

    # Test without changed
    _result = dict(changed=False)
    _result = type('Result', (object,), dict(_result=_result))
    _result = type('Result', (object,), dict(_result=_result))
    assert type(_v2_runner_on_ok(_result)) == type(None)

    # Test with changed
    _result = dict(changed=True)
    _result = type('Result', (object,), dict(_result=_result))
    _result = type('Result', (object,), dict(_result=_result))

# Generated at 2022-06-13 11:55:55.128736
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    print("Testing method v2_runner_on_failed...")
    cb = CallbackModule()
    class result:
        _task = ""
    cb.v2_runner_on_failed(result)


# Generated at 2022-06-13 11:55:56.364134
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    callback_module = CallbackModule()

# Generated at 2022-06-13 11:55:56.981687
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    me=CallbackModule()

# Generated at 2022-06-13 11:56:07.032697
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    
    import unittest
    from unittest.mock import MagicMock
    from unittest.mock import patch
    from ansible import constants as C
    from ansible.plugins.callback import CallbackBase
    from ansible.plugins.callback.minimal import CallbackModule
    from collections import namedtuple

    class Test_CallbackModule(unittest.TestCase):

        def setUp(self):
            self.callback_module = CallbackModule()
            self.callback_module.CALLBACK_VERSION = 2.0
            self.callback_module.CALLBACK_TYPE = 'stdout'
            self.callback_module.CALLBACK_NAME = 'minimal'
            self.callback_module._handle_warnings  = MagicMock()
            self.callback_module._dump_results = MagicMock()

# Generated at 2022-06-13 11:56:42.922311
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # input arguments used in the unit test
    result = {}
    ignore_errors=False
    
    # unit test
    test_obj = CallbackModule()
    test_obj._handle_warnings = _handle_warnings_mock
    test_obj._display = _display_mock
    test_obj._handle_exception = _handle_exception_mock
    test_obj._dump_results = _dump_results_mock
    test_obj._clean_results = _clean_results_mock
    test_obj.v2_runner_on_failed(result, ignore_errors)



# Generated at 2022-06-13 11:56:47.087090
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    mod = CallbackModule()
    assert mod.CALLBACK_VERSION == 2.0
    assert mod.CALLBACK_TYPE == 'stdout'
    assert mod.CALLBACK_NAME == 'minimal'
    assert mod._display.colorize == 'minimal'

# Generated at 2022-06-13 11:56:56.268586
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    import ansible.plugins.callback.minimal
    import ansible.utils.template
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.playbook.handler
    import ansible.inventory.host
    import ansible.vars.manager
    C = ansible.constants
    T = ansible.utils.template
    P = ansible.playbook.play
    TK = ansible.playbook.task
    B = ansible.playbook.block
    H = ansible.playbook.handler
    I = ansible.inventory.host
    V = ansible.vars.manager


# Generated at 2022-06-13 11:56:56.636565
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert True

# Generated at 2022-06-13 11:57:00.161280
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    C.CLIARGS = {}
    callback = CallbackModule()
    assert hasattr(callback, '_dump_results')
    assert hasattr(callback, '_handle_exception')
    assert hasattr(callback, '_handle_warnings')
    assert hasattr(callback, '_clean_results')
    assert hasattr(callback, '_get_diff')
    assert hasattr(callback, '_command_generic_msg')
    assert hasattr(callback, 'CALLBACK_VERSION')
    assert hasattr(callback, 'CALLBACK_TYPE')
    assert hasattr(callback, 'CALLBACK_NAME')

# Generated at 2022-06-13 11:57:07.216194
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    result = {}
    result_task = {}
    result_result = {}
    result_result['changed'] = True

    result_host = {}
    result_host.get_name = lambda: "test"

    result._task = result_task
    result._result = result_result
    result._host = result_host

    minimal_callback = CallbackModule()
    minimal_callback.v2_runner_on_ok(result)



# Generated at 2022-06-13 11:57:14.891201
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
  import random
  from ansible.playbook.task_include import TaskInclude
  from ansible.playbook.handler_task_include import HandlerTaskInclude
  from ansible.playbook.block import Block
  from ansible.playbook.role.tasks import Tasks
  cb = CallbackModule()
  for i in range(random.randint(5, 10)):
    task1 = TaskInclude()
    task1._parent = HandlerTaskInclude()
    task1._block = Block(parent=task1)
    task1._role = Tasks()
    task1._task = dict(action=dict(__ansible_argspec__=dict(var1=1, var2=2)))
    task1._host = dict(name="host_%d" % i)

# Generated at 2022-06-13 11:57:24.950175
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    cbm = CallbackModule()
    class MyResult():
        def __init__(self):
            self._host = class_host_name()
            self._result = {
                            "changed": True,
                            "invocation": {
                                            "module_args": {
                                                                "key": "val"
                                                            }
                                            }
                            }
            self._task = class_task()
    my_result = MyResult()
    # Test with changed result
    test_result = cbm.v2_runner_on_ok(my_result)
    assert "CHANGED" in test_result
    # Test with not changed result
    my_result._result['changed'] = False
    test_result = cbm.v2_runner_on_ok(my_result)

# Generated at 2022-06-13 11:57:25.860903
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pass


# Generated at 2022-06-13 11:57:30.755783
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
	cm=CallbackModule()
	result=dict(_host='host1',_result=dict(hostname='host1',changed=False))
	ret=cm.v2_runner_on_ok(result)
	print(ret)
	result=dict(_host='host2',_result=dict(hostname='host2',changed=True))
	ret=cm.v2_runner_on_ok(result)
	print(ret)



# Generated at 2022-06-13 11:58:58.491378
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    # Preparation
    # 1. Create a callback module
    module = CallbackModule()
    # 2. Set the displayer using ansible.utils.display.Display
    module._display = Display()

    # 3. Create a result for testing
    result = DummyResult()
    # 4. Set the host name
    result._host.get_name.return_value = "TestHost"

    # 5. Create a result._result
    result._result = {"changed":False, "rc":-1, "stdout":"This is a test stdout", "stderr":"This is a test stderr", "msg":"This is a test message"}

    # 6. Create a result._task
    result._task = DummyTask()
    result._task.action = "TestAction"

    # Tested function
    module.v2_runner_on

# Generated at 2022-06-13 11:58:59.823820
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    # set up CallbackModule object
    module = CallbackModule()
    assert module != None

# Generated at 2022-06-13 11:59:08.361880
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    debug = False

    def test_default_error_run():
        class FakeDisplay(object):
            def __init__(self):
                pass

            def display(self, msg, color=None):
                if debug:
                    print(msg)

        class FakeResult(object):
            def __init__(self):
                pass

            @property
            def _host(self):
                class FakeHost(object):
                    def __init__(self):
                        pass

                    def get_name(self):
                        return "fake0"

                return FakeHost()
            
            @property
            def _result(self):
                return {
                            "stdout": "fake std out!",
                            "stderr": "fake std error!",
                            "msg": "fake msg!",
                            "rc": -1
                        }

           

# Generated at 2022-06-13 11:59:10.153114
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    CallbackModule().v2_runner_on_failed({"_host": "localhost"})


# Generated at 2022-06-13 11:59:13.009843
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    try:
        assert isinstance(CallbackModule(), CallbackModule)
    except AssertionError:
        print("test_CallbackModule FAILED")
        return
    print("test_CallbackModule PASSED")

# Test the CallbackModule class
test_CallbackModule()

# Generated at 2022-06-13 11:59:14.481802
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    fake_result = FakeResult()
    tmp_module = CallbackModule()
    assert tmp_module.v2_runner_on_ok(fake_result) == None


# Generated at 2022-06-13 11:59:20.922285
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = dict()
    result['host_name'] = 'localhost'
    result['changed'] = False
    result['skipped'] = False
    result['module_name'] = 'ping'
    result['module_args'] = ''
    result['module_version'] = '2.0.0.1'
    result['stdout'] = 'PONG'
    result['stderr'] = ''
    result['rc'] = 0
    result['msg'] = 'All items completed'
    result['results'] = '<ping>'
    result['invocation'] = dict()
    result['invocation']['module_args'] = ''
    result['invocation']['module_name'] = 'ping'
    result['invocation']['module_version'] = '2.0.0.1'

# Generated at 2022-06-13 11:59:26.542796
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # Test when 'diff' not in result._result and result._result['diff']
    result = Mock()
    result._result = {'diff': "", 'parsed': True}
    obj = CallbackModule()

# Generated at 2022-06-13 11:59:31.224127
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    cb = CallbackModule()
    result = {'diff':'test text'}
    assert cb._get_diff(result) == 'test text'
    result = {'diff':''}
    assert cb._get_diff(result) == ''

# Generated at 2022-06-13 11:59:39.394162
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    result = {
    "_ansible_parsed": True,
    "changed": True,
    "_ansible_no_log": False,
    "invocation": {
        "module_args": {}
    },
    "stdout": "",
    "stdout_lines": []
    }
    # mock display object
    class Display:
        def display(self, msg, color):
            print(msg)
    display = Display()
    callback = CallbackModule()
    callback._display = display
    callback.v2_runner_on_ok(result)