

# Generated at 2022-06-13 11:51:34.074934
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    obj = CallbackModule()
    assert obj.version == 2.0
    assert obj.type == 'stdout'
    assert obj.name == 'minimal'
    assert obj.CALLBACK_VERSION == 2.0
    assert obj.CALLBACK_TYPE == 'stdout'
    assert obj.CALLBACK_NAME == 'minimal'
    assert obj.CALLBACK_NEEDS_WHITELIST == False

# Generated at 2022-06-13 11:51:43.563629
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import mock
    from ansible.plugins.loader import callback_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.callback import CallbackBase
    from ansible import constants as C

# Generated at 2022-06-13 11:51:44.351614
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    assert 1


# Generated at 2022-06-13 11:51:54.051463
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    from ansible.plugins.callback.minimal import CallbackModule
    import yaml
    data = yaml.load("""
    diff: |
        ---
        +++ /home/tangqiang/ansible_task/temp/add.txt    2017-11-21 11:08:28.895451201 +0800
        @@ -0,0 +1,2 @@
        +hello
        +world
        """)

    result = {"diff": data['diff']}
    cb = CallbackModule()
    ret = cb._get_diff(result['diff'])
    
    assert (ret == result['diff']), "Failed to get diff"

# Generated at 2022-06-13 11:51:55.076309
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    pass


# Generated at 2022-06-13 11:52:04.674586
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # Create an instance of the CallbackModule
    callbackmodule = CallbackModule()
    
    # Create a task result
    task_result = {}
    task_result['diff'] = [{'before': '', 'after': '', 'before_header': '', 'after_header': '', 'before_mode': '100755', 'after_mode': '100755'}]
    
    # Create a result object
    result = {}
    result['_result'] = task_result
    
    # Test the method
    callbackmodule.v2_on_file_diff(result)

# Generated at 2022-06-13 11:52:09.440639
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import copy
    new_result = copy.deepcopy(result)
    new_result['_result']['changed'] = True
    runner_on_failed = CallbackModule()
    runner_on_failed.v2_runner_on_failed(new_result)
    new_result['_result']['changed'] = False
    runner_on_failed.v2_runner_on_failed(new_result)


# Generated at 2022-06-13 11:52:12.337663
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    """
    Constructor test
        - creates class instance without exception
    """
    CallbackModule()

# Generated at 2022-06-13 11:52:16.384965
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Parameters
    result = {}
    ignore_errors = False

    # Call function
    callback = CallbackModule()
    callback.v2_runner_on_failed(result, ignore_errors)

    # Test assertions


# Generated at 2022-06-13 11:52:19.893140
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    module = CallbackModule()
    module._display = Display()
    module.v2_runner_on_ok("test")
    assert module._display.content == "test | SUCCESS => {}\n"


# Generated at 2022-06-13 11:52:26.670432
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    module = CallbackModule()
    assert module.CALLBACK_TYPE == 'stdout'
    assert module.CALLBACK_VERSION == 2.0
    assert module.CALLBACK_NAME == 'minimal'

# Generated at 2022-06-13 11:52:36.961485
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import os
    os.environ["ANSIBLE_STDOUT_CALLBACK"] = "default"
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()

    #import ansible.plugins.loader as plugin_loader
    #plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../plugins/callback'))
    #callback = plugin_loader.get('default', 'CallbackModule')

    from ansible.plugins.callback import CallbackBase
    from ansible.plugins.callback.minimal import CallbackModule
    callback = CallbackModule(play_context, display=CallBackDisplay())


# Generated at 2022-06-13 11:52:46.868088
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():

    # Test for case when module name is one of the module names in the list
    # C.MODULE_NO_JSON

    # Initializing the required parameters
    result = {}
    result._result = {'changed': False}
    result._task = {}
    result._task.action = 'command'
    result._host = {}
    result._host.get_name = lambda : 'test_host'

    # Executing the function under test
    obj_result = CallbackModule()
    obj_result.v2_runner_on_ok(result)

    # Assertion to check the setup, test, and teardown operations

# Generated at 2022-06-13 11:52:49.733163
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    obj = CallbackModule()
    assert obj.CALLBACK_VERSION == 2.0
    assert obj.CALLBACK_TYPE == 'stdout'
    assert obj.CALLBACK_NAME == 'minimal'

# Generated at 2022-06-13 11:53:00.460773
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    from ansible.plugins.callback.minimal import CallbackModule
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    task = Task()
    task._ds = dict(action='file exists')
    task._uuid = 'test_uuid'
    result = TaskResult(host=Host('test_host.foo.bar'), task=task, return_data={'diff': 'foo'})

    callback = CallbackModule()

# Generated at 2022-06-13 11:53:01.633150
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    assert CallbackModule.v2_runner_on_ok("this is a result") == None

# Generated at 2022-06-13 11:53:09.455112
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # Define TestCallbackModule to use CallbackModule's methods
    class TestCallbackModule(CallbackModule):

        def __init__(self, display=None):
            self._display = display

        def _get_diff(self, diff):
            return diff

    # Define a diff object
    diff = {'before': 'This is a test before.', 'after': 'This is a test after.', 'before_header': 'Test file before', 'after_header': 'Test file after'}
    callback = TestCallbackModule()

    # Define expected output from v2_on_file_diff
    expected = 'differ: --- %s\n' % diff.get('before_header') + '+++ %s\n' % diff.get('after_header')
    expected += '@@ -1,4 +1,4 @@\n'


# Generated at 2022-06-13 11:53:12.805103
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    """
    Check if the constructor of CallbackModule class,
    creates different instances of the CallbackModule class.
    """
    result = CallbackModule()
    assert result is not None

# Generated at 2022-06-13 11:53:14.802798
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    c = CallbackModule()
    c.v2_runner_on_failed(result, ignore_errors=True)

# Generated at 2022-06-13 11:53:23.674232
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    def mock_dump_results(results, indent):
        return indent + "Mocked dump"
    def mock_display(text, color=None):
        print(text)

    result = MagicMock()
    result.action_on_unreachable = None
    result.action = 'stdout'
    result.changed = True
    result.host_unreachable = False
    result._host = MagicMock()
    result._host.get_name.return_value = "Mocked host"
    result._result = None

    cm = CallbackModule()
    cm._dump_results = mock_dump_results
    cm._display = MagicMock()

    cm.v2_runner_on_ok(result)

    result._result = "ok"
    cm.v2_runner_on_ok(result)

    result

# Generated at 2022-06-13 11:53:35.063983
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # Test 1
    result1 = {'diff': {'before': 'before_string', 'after': 'after_string', 'before_header': 'before_header_string', 'after_header': 'after_header_string'}}
    c = CallbackModule()
    c.v2_on_file_diff(result1)

# Generated at 2022-06-13 11:53:42.168920
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Test mocks:
    class Result():
        def __init__(self):
            self._result = {}
            self._task = {}
            self._task.action = ''
            self._host = {}
            self._host.get_name = lambda: 'test.example.com'
    class Display():
        def __init__(self):
            self.stdout = ''
        def display(self, string, color=''):
            self.stdout += string + '\n'
    C.COLOR_OK = 'color_ok'
    C.COLOR_CHANGED = 'color_changed'
    # Test method:
    callbackModule = CallbackModule()
    callbackModule._display = Display()
    result = Result()
    result._result = {'changed': False, 'diff': {}}
    callbackModule.v2

# Generated at 2022-06-13 11:53:53.491261
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    import types
    import unittest

    from ansible.plugins.callback.minimal import CallbackModule
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.utils.addresses import parse_address

    class TestRunner(object):
        '''
        Controls the flow of play during the execution of a playbook.

        Automatically loads the inventory, and based on options passed in,
        runs through the play in an order determined by the dependency graph,
        loading callbacks as needed.

        :kwargs: Optional keyword arguments for configuring the runner
        '''


# Generated at 2022-06-13 11:54:02.857740
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    """test the v2_on_file_diff method"""
    import json

    cbm = CallbackModule()


# Generated at 2022-06-13 11:54:14.154299
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    result_host = dict()
    result_host['changed'] = False

# Generated at 2022-06-13 11:54:15.108050
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    x = CallbackModule()
    assert True

# Generated at 2022-06-13 11:54:23.899498
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import io
    from ansible.plugins.callback import CallbackBase
    
    class Test_CallbackModule_v2_runner_on_failed(CallbackBase):
        def __init__(self):
            self.stdout = io.StringIO()
            self._display = self

        def display(self, msg, color=None, stderr=False, screen_only=False, log_only=False):
            self.stdout.write(msg)

    # create instance of class Test_CallbackModule_v2_runner_on_failed
    tcm = Test_CallbackModule_v2_runner_on_failed()

    # invoke method v2_runner_on_failed
    tcm.v2_runner_on_failed(None, ignore_errors=False)


# Generated at 2022-06-13 11:54:30.219632
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    test1 = _TestObject(
        _result = _ResultObject(
            _host = _HostObject(
                get_name = lambda: 'test1'
            ),
            _task = _TaskObject(
                action = 'test_action'
            ),
            get = lambda x: {
                'changed': True
            }.get(x),
            get_lines = lambda: ['test']
        )
    )

# Generated at 2022-06-13 11:54:42.441996
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    # Setup
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.plugins.callback import CallbackBase
    loader = DataLoader()
    display = Display()
    play_context = PlayContext()
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    callbackBase = CallbackBase()
    host = inventory.get_host('localhost')

# Generated at 2022-06-13 11:54:50.287412
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    """
    Unit test for method v2_on_file_diff of class CallbackModule
    """
    mock_display = MagicMock()
    mock_result = MagicMock()
    mock_result.return_value.configure_mock(**{'_result.get.return_value': 'Foobar'})
    mock_result_instance = mock_result()
    callback = CallbackModule()
    callback._display = mock_display
    callback.v2_on_file_diff(mock_result_instance)
    assert mock_display.called is True
    assert mock_result.called is True
    assert mock_result_instance._result.get.called is True

# Generated at 2022-06-13 11:55:13.223998
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import unittest
    import os
    import json

    TEST_FILE = 'test_callback_minimal.test_v2_runner_on_ok.json'

    class TestCallbackModuleInitMinimal(unittest.TestCase):
        def test_v2_runner_on_ok_ok(self):
            current_directory = os.path.abspath(os.path.dirname(__file__))
            expected_result_path = os.path.join(current_directory, 'data', TEST_FILE)
            with open(expected_result_path, 'r') as results_file:
                expected_result = json.load(results_file)

# Generated at 2022-06-13 11:55:13.938893
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pass

# Generated at 2022-06-13 11:55:27.714607
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    host = "testHost"
    testtask = "testtask"

# Generated at 2022-06-13 11:55:31.717313
# Unit test for constructor of class CallbackModule
def test_CallbackModule():

    # Test if subsequent instantiation is equal
    c = CallbackModule()
    c2 = CallbackModule()
    assert c == c2

    # Test for instance of the class
    assert isinstance(c, CallbackModule) == True

# Test for the method _command_generic_msg

# Generated at 2022-06-13 11:55:34.717000
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    c = CallbackModule()
    c.v2_runner_on_failed(result=None, ignore_errors=False)
    assert True


# Generated at 2022-06-13 11:55:40.214274
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    callback = CallbackModule()
    result = {}
    result['diff'] = [{"before": "test_before\n", "after": "\n", "before_header": "test_before_header", "after_header": "test_after_header"}]
    assert callback._get_diff(result['diff']) == 'before: test_before_header\nafter: test_after_header\n\ntest_before-\n+\n\n'



# Generated at 2022-06-13 11:55:45.776843
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # Create the object
    x = CallbackModule()

    # Create a result
    result = Result(host='localhost', task=None, task_result=None, stdout='', stderr='', stdout_lines=[], stderr_lines=[], changed=False, failed=False)
    
    # Create a diff result
    result._result = {'diff': {'after': 'line1\nline2'}}

    # Call the method
    x.v2_on_file_diff(result)

# Generated at 2022-06-13 11:55:53.043496
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
  result = {}
  result['_result']= {}
  result['action']='a string'
  result['_host']=''
  result['_result']['changed']=True
  result['_result']['module_stderr'] = 'module std error'
  result['_result']['module_stdout'] = 'module std out'
  result['_result']['rc'] = 0
  result['_result']['stderr'] = 'standard error'
  result['_result']['stdout'] = 'standard out'
  result['_result']['warnings'] = ['warning1', 'warning2']
  cb = CallbackModule()
  # Check result when called on an 'ok' event
  cb.v2_runner_on_ok(result)
  # Check result when

# Generated at 2022-06-13 11:56:03.202155
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    from ansible_collections.ansible.community.tests.unit.compat.mock import Mock
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch

    mock_display = Mock()
    mock_result = Mock()
    mock_result.result_json = lambda: {'json_data': 'ok'}
    mock_result._host.get_name.return_value = 'host123'
    mock_result._task.action = 'shell'
    mock_result._result = {'changed': True}
    mock_result.result_json = lambda: {'json_data': 'ok'}

    mock_display.display = Mock()


# Generated at 2022-06-13 11:56:10.710754
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    from ansible.vars.manager import VariableManager

    play_context = PlayContext()
    task_result = TaskResult(host=None, task=None)

    host = HostVars(name='localhost', variables=HostVarsVars(variable_manager=VariableManager()))
    task_result._host = host

    callback = CallbackModule()
    assert callback.v2_runner_on_failed(task_result) == None



# Generated at 2022-06-13 11:56:44.333129
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
	result = {}
	result['_host'] = {}
	result['_host']['get_name'] = lambda: '192.168.1.1'
	result['_task'] = {}
	result['_task']['action'] = 'ping'
	result['_result'] = {}
	result['_result']['changed'] = True
	callback = CallbackModule()
	callback.v2_runner_on_ok(result)


# Generated at 2022-06-13 11:56:54.180396
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Arrange
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import load_extra_vars
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.plugins.callback import CallbackBase
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible import context


# Generated at 2022-06-13 11:57:02.093644
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    ########
    #
    # TEST 1: No diff present in result --> no output on display
    #
    ########
    from ansible.vars.unsafe_proxy import UnsafeText
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.callback import CallbackBase
    from ansible.vars.manager import Variable

# Generated at 2022-06-13 11:57:06.331550
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    c=CallbackModule()
    assert c.CALLBACK_TYPE == 'stdout'
    assert c.CALLBACK_VERSION == 2.0
    assert c.CALLBACK_NAME == 'minimal'

# Generated at 2022-06-13 11:57:12.210347
# Unit test for method v2_on_file_diff of class CallbackModule

# Generated at 2022-06-13 11:57:21.894898
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.playbook.play_context import PlayContext
    playcontext = PlayContext()
    pc = PlayContext()


# Generated at 2022-06-13 11:57:31.021102
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible.plugins.callback import CallbackBase
    from ansible import constants as C
    from ansible.plugins.callback.minimal import CallbackModule

    class TestCall(CallbackBase):
        pass

    test_call = TestCall()

    assert test_call.CALLBACK_VERSION == 2.0
    assert test_call.CALLBACK_TYPE == 'stdout'
    assert test_call.CALLBACK_NAME == 'minimal'

    assert test_call.CALLBACK_VERSION == CallbackModule.CALLBACK_VERSION == CallbackBase.CALLBACK_VERSION
    assert test_call.CALLBACK_TYPE == CallbackModule.CALLBACK_TYPE == CallbackBase.CALLBACK_TYPE

# Generated at 2022-06-13 11:57:39.818015
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['127.0.0.1'], variable_manager=variable_manager, host_list=['127.0.0.1'])
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 11:57:49.164449
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():

    # Prepare Mock Object for Test
    callback = CallbackModule()

# Generated at 2022-06-13 11:58:00.688440
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    import json
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.runner.task_result import TaskResult
    from ansible.runner.return_data import ReturnData

    # initialize needed objects
    variable_manager = VariableManager()
    loader = variable_manager
    inventory = Inventory(loader)
    play_source = dict(
        name="minimal test playbook",
        hosts='webservers',
        gather_facts='no',
        tasks=[dict(action=dict(module='shell', args='ls'), register='shell_out'),
               dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))]
    )

# Generated at 2022-06-13 11:59:17.887167
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    config = {}
    display = 'all'
    options = {}
    callback = CallbackModule(display, config, options)
    assert callback.CALLBACK_TYPE == 'stdout'
    assert callback.CALLBACK_VERSION == 2.0
    assert callback.CALLBACK_NAME == 'minimal'
    assert callback._plugin_options == {}
    assert callback._plugin_config == {}

# Generated at 2022-06-13 11:59:20.366337
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    result = dict()
    result['diff'] = 'diff'

    class _display:
        def display(self, str):
            pass

    _display = _display()
    cb_mod = CallbackModule(display=_display)
    cb_mod.v2_on_file_diff(result)

# Generated at 2022-06-13 11:59:22.047925
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    mod = CallbackModule()
    mod.v2_runner_on_ok(None, None)
    mod.v2_runner_on_failed(None, None, None)

# Generated at 2022-06-13 11:59:28.899117
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    from ansible.plugins.callback.minimal import CallbackModule
    from ansible.utils.color import stringc
    from ansible.template import Templar
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    display_object = {'display': stringc}
    loader_object = DataLoader()
    templar_object = Templar(loader=loader_object)
    inventory_obj = InventoryManager(loader=loader_object)
    variable_manager = VariableManager(loader=loader_object, inventory=inventory_obj)

# Generated at 2022-06-13 11:59:37.623087
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.vars.hostvars import HostVars, HostVarsVars
    from ansible import context
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.loader import callback_loader
    from ansible.plugins.callback.minimal import CallbackModule

    test_callback = CallbackModule()
    task = Task()
    task.action = 'copy'
    task_result = TaskResult(host=None, task=task, return_data=None)

# Generated at 2022-06-13 11:59:47.508207
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    import ansible.utils.template as template
    import ansible.utils.unsafe_proxy as unsafe_proxy
    import ansible.utils.passwords as passwords

    class test_display():

        def display(self, msg, color=None):
            print(msg)

    class test_host():

        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    class test_task():

        def __init__(self, action):
            self.action = action

    class test_result():

        def __init__(self, host, action, result):
            self._host = host
            self._task = test_task(action)
            self._result = result

    plugin = CallbackModule()
    plugin._display = test_display()

    assert plugin

# Generated at 2022-06-13 11:59:54.683705
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    r1 = {
        "_host": {
            "get_name": lambda: "host1"
        },
        "_result": {
            "changed": False
        },
        "_task": {
            "action": "action1"
        }
    }
    c1 = CallbackModule()
    c1._display = _MockDisplay()
    c1.v2_runner_on_ok(r1)
    assert(c1._display._color == C.COLOR_OK)

    r2 = {
        "_host": {
            "get_name": lambda: "host2"
        },
        "_result": {
            "changed": True
        },
        "_task": {
            "action": "action2"
        }
    }
    c2 = CallbackModule()
    c2._display = _

# Generated at 2022-06-13 12:00:03.365521
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import unittest
    import mock

    class TestDisplay():
        def __init__(self):
            self.display_result = None

        def display(self, data, color=None):
            self.display_result = data

    class TestResult():
        def __init__(self):
            self.host = TestHost()
            self.result = {
                'stderr': "test stderr",
                'stdout': "test stdout",
                'msg': "test msg"
            }

    class TestHost():
        def get_name(self):
            return 'testHost'

    test_result = TestResult()
    test_display = TestDisplay()

    test_instance = CallbackModule()
    test_instance._display = test_display


# Generated at 2022-06-13 12:00:05.378412
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    c = CallbackModule()
    c._display.display("", color=C.COLOR_ERROR)
    assert True == True


# Generated at 2022-06-13 12:00:13.318415
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C
    import os

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["/tmp/ansible/ansible-yml/hosts"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)