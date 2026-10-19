

# Generated at 2022-06-13 11:51:35.904747
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = {'_ansible_verbose_always': False, '_ansible_no_log': False, '_ansible_verbose': False}
    result['_ansible_parsed'] = True
    result['changed'] = False
    result['_ansible_no_log'] = False
    result['msg'] = 'Unknown Error occurred.'
    result['failed'] = True
    result['_ansible_item_result'] = False
    result['stdout'] = 'Successful.'
    result['invocation'] = {'module_name': 'collectd'}
    result['_ansible_parsed'] = True
    result['rc'] = 0
    result['stderr'] = ''


# Generated at 2022-06-13 11:51:44.912503
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.playbook.play_context import PlayContext
    play_context = PlayContext()
    play_context._remote_tmp = '/home/ansible/.ansible/tmp'
    play_context._connection = 'local'
    play_context._play_path = '/home/ansible/test.yaml'
    play_context._playbook = '/home/ansible/test.yaml'
    play_context._role_path = '/home/ansible/roles:/usr/share/ansible/roles'
    play_context.connection = 'local'
    play_context.network_os = 'default'
    play_context.remote_addr = '127.0.0.1'
    play_context.port = 22
    play_context.become = False

# Generated at 2022-06-13 11:51:55.829655
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
        # pylint: disable=protected-access,too-many-locals,too-many-statements
        # TODO: enable pylint:fix-me below
        # pylint: disable=fixme
        # TODO: write this test
        # TODO: This test is wrong. It will only work as a unit test if we
        # stub a lot of stuff out.  We would be better off creating a
        # functional test that uses the real Ansible code and feeding in
        # playbooks and generating test results.
        # TODO: We can remove the TODO from above once we have created at least
        # one functional test that uses the real Ansible code.
        from ansible_collections.ansible.community.tests.unit.test_utils.test_cases import TestCase
        from ansible.module_utils._text import to

# Generated at 2022-06-13 11:52:08.338149
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    _result = {'changed': False, 'diff': {'before': 'old', 'after': 'new'}, 'invocation': {'module_args': {'path': '/etc/hosts', 'follow': False, 'state': 'directory', 'force': False}}, '_ansible_no_log': False, 'path': '/etc/hosts', '_ansible_item_result': True, 'state': 'directory', 'item': 'hosts', '_ansible_item_label': ['hosts'], '_ansible_parsed': True, 'changed': False, '_ansible_item_label': ['hosts']}
    # Unit test for method v2_on_file_diff of class CallbackModule
    # with 'old' as before, 'new' as after.
    # expected to raise an error.
   

# Generated at 2022-06-13 11:52:10.599634
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # FIXME: Actually test something
    plugin = CallbackModule()
    plugin.v2_runner_on_ok(None)
    assert True

# Generated at 2022-06-13 11:52:12.185956
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    assert False == True  # TODO: write me


# Generated at 2022-06-13 11:52:22.775723
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # Setup test
    import textwrap
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import merge_hash
    from ansible.utils.vars import combine_vars
    from ansible.inventory.group import Group
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    dummy_loader = DataLoader()
    variable_manager = VariableManager

# Generated at 2022-06-13 11:52:34.347307
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    '''CallbackModule.v2_runner_on_ok unit test'''
    # create test object
    cb_mod = CallbackModule()
    result = type('result', (object,), {'_task': type('task',(object,), {'action': 'action'})})
    result._result = {'changed': True, 'rc': 0, 'module_stdout': '', 'module_stderr': ''}
    # test common condition
    if cb_mod.v2_runner_on_ok(result) is None:
        assert True
    # test _result changed True
    if 'CHANGED' in cb_mod.v2_runner_on_ok(result):
        assert True

# Generated at 2022-06-13 11:52:43.542988
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    
    # create an instance of the class CallbackModule
    callback_module = CallbackModule()

    # create a variable with the result of a diff between two files
    result = {
        "diff" : "diff --git a/playbook b/playbook\nindex ca3f2d0..a8180c8 100644\n--- a/playbook\n+++ b/playbook\n@@ -5,5 +5,5 @@\n-hosts: all\n+hosts: localhost\n tasks:\n  - name: ping\n   ping:\n"
    }

    # call the v2_on_file_diff method with the variable defined above
    callback_module.v2_on_file_diff(result)

# Generated at 2022-06-13 11:52:48.302270
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    module = CallbackModule()
    result = {
        '_result': {
            'diff': [
                '[before]\n',
                '[after]\n',
            ],
        },
    }
    expected = '[before]\n[after]\n'
    assert expected == module.v2_on_file_diff(result)

# Generated at 2022-06-13 11:53:01.241477
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Create instance of class to be tested
    callback = CallbackModule()

    # Create mocks
    result = MockResult()
    result._result = dict(no_display=True,
                          msg="changed",
                          changed=True)
    result._host = MockHost()
    result._host.get_name.return_value = "Tester"

    # Assert that result._result is not None
    assert result._result is not None

    # Call method
    callback.v2_runner_on_failed(result, ignore_errors=False)

    # Check that expected output was displayed
    assert print("Tester | FAILED! => {'no_display': True, 'msg': 'changed', 'changed': True}", color=C.COLOR_ERROR)

# Generated at 2022-06-13 11:53:06.944729
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # see if we get a TypeError result when passing an empty result
    # parameter to the decorated method.
    testResult = CallbackModule()
    with pytest.raises(TypeError) as err:
        testResult.v2_on_file_diff({})

    # see if we get a TypeError result when passing a None result
    # parameter to the decorated method.
    testResult = CallbackModule()
    with pytest.raises(TypeError) as err:
        testResult.v2_on_file_diff(None)

# Generated at 2022-06-13 11:53:14.373542
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import json
    import textwrap
    from ansible.plugins.callback.minimal import CallbackModule

    cb = CallbackModule()

# Generated at 2022-06-13 11:53:21.878831
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = {'_result': {'failed': True}, '_host': {'get_name': lambda: 'test host'}}
    mock_display = Mock()

    callbackModule = CallbackModule()
    callbackModule._display = mock_display

    callbackModule.v2_runner_on_failed(result)

    assert mock_display.method_calls[0][0] == 'display'
    assert mock_display.method_calls[0][1] == ("test host | FAILED! => {'failed': True}",)
    assert mock_display.method_calls[0][2] == {'color': 'red'}


# Generated at 2022-06-13 11:53:27.856517
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    module = CallbackModule()
    expected = 'test | SUCCESS => {' + "\n" + '    "changed": false' + "\n" + '}' + "\n"
    actual = module.v2_runner_on_ok(Result(Host('test'), Task('test'), {'changed': False}))
    assert(expected == actual)

    expected = 'test | SUCCESS => {' + "\n" + '    "changed": true' + "\n" + '}' + "\n"
    actual = module.v2_runner_on_ok(Result(Host('test'), Task('test'), {'changed': True}))
    assert(expected == actual)


# Generated at 2022-06-13 11:53:37.296919
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import json
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False, encoding='utf-8') as f:
        cm = CallbackModule()
        result = {
            'changed': True,
            'ansible_facts': {
                'a': 'b'
            }
        }
        iresult = cm._init_result(result)
        cm.v2_runner_on_ok(iresult)
        # Slight hack to get the value from the sys.stdout.write call
        out = f.write(cm._display.display.buffer[0])
        out = out[:out.find('|')]
        out = json.loads(out)
        assert out == 'b'

# Generated at 2022-06-13 11:53:37.813395
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    pass

# Generated at 2022-06-13 11:53:38.309424
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pass

# Generated at 2022-06-13 11:53:39.914815
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    try:
        CallbackModule()
        assert True
    except AssertionError:
        assert False

# Generated at 2022-06-13 11:53:50.944938
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # Setup
    # print("Calling setup method")
    test_result = MagicMock()
    test_result._result = {'diff': 'some_diff'}
    test_result._result['diff'] = 'some_diff'

    test_obj = CallbackModule()
    test_obj._display = type("MagicMock", (object,), {"display": MagicMock()})
    test_obj._get_diff = MagicMock(return_value='some_diff')
    # test_obj._display.display = MagicMock()

    # Exercise
    # print("Calling exercise method")
    test_obj.v2_on_file_diff(test_result)

    # Verify
    # print("Calling verify method")
    test_obj._display.display.assert_called_once_with('some_diff')

    #

# Generated at 2022-06-13 11:54:00.937188
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # setup test values
    result = {}
    # create test object
    obj = CallbackModule(display=None)
    # set up test object
    obj.set_options({})

    # run test
    obj.v2_on_file_diff(result)


# Generated at 2022-06-13 11:54:04.018965
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    cb = CallbackModule()
    result = {'changed': True, 'rc': 0, 'stdout': 'This is a stdout', 'stderr': 'This is a stderr', 'msg': 'This is a msg', 'failed': False}
    cb.v2_runner_on_ok(result)


# Generated at 2022-06-13 11:54:12.613378
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # The return values of v2_runner_on_ok are not checked here
    print()
    print("Test for method v2_runner_on_ok of class CallbackModule")
    # Initialization
    result = 'FAILURE'
    # Expected results
    expected_result = 'SUCCESS'
    # Code to be tested
    test_object = CallbackModule()
    test_object.v2_runner_on_ok(result)
    # Assertion - Check whether the expected and actual results match
    assert expected_result == test_object.check_result


# Generated at 2022-06-13 11:54:17.931461
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    result = dict()
    result['_host'] = dict()
    result['_host']['get_name'] = lambda: 'TestHost'
    result['_result'] = dict()
    result['_result']['changed'] = False

    callback = CallbackModule()
    buffer = callback.v2_runner_on_ok(result)
    assert 'TestHost | SUCCESS => ' in buffer


# Generated at 2022-06-13 11:54:21.938451
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    module = CallbackModule()
    class FakeFile:
        def __init__(self, name, total_size):
            self.name = name
            self.total_size = total_size
            self.size = 0
        def read(self, bytes):
            self.size += bytes
            if self.size >= self.total_size:
                raise EOFError
    class FakeHost:
        def __init__(self, name):
            self.name = name
    class FakeResult:
        def __init__(self, host, diff):
            self._result = {'inserts': 1, 'removes': 1, 'dst_binary': False, 'src_binary': False, 'dst': FakeFile('dst', 1024*1024), 'src': FakeFile('src', 1024*1024), 'diff': diff}
            self

# Generated at 2022-06-13 11:54:28.795403
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    result_str = "@@ -1,3 +1,3 @@\n 1\n-2\n+2.1\n 3\n"
    result_dict = {'diff': {'after': '3\n', 'before': '1\n2\n3\n',
                         'before_header': 'file.txt', 'after_header': 'file.txt',
                         'before_lines': ['1\n','2\n','3\n'], 'after_lines': ['1\n','2.1\n','3\n'],
                         'before_size': 5, 'after_size': 6,
                         'delta': 1, 'matched': 2,
                         'offset': 1, 'encoding': 'None',
                         'newfile': False, 'diff': result_str, 'diffstat':''}}

    ans

# Generated at 2022-06-13 11:54:33.918133
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # create instance of class CallbackModule
    instance = CallbackModule()
    # create mock variable result
    result = ''
    # run method v2_runner_on_failed of class CallbackModule
    instance.v2_runner_on_failed(result)


# Generated at 2022-06-13 11:54:36.773998
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    c = CallbackModule()
    c.v2_runner_on_ok("test")

test_CallbackModule_v2_runner_on_ok()

# Generated at 2022-06-13 11:54:42.718601
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Define function input
    result_mock = {'_result': {'failed': True, 'msg': 'MOCK TEST'}}
    result = type('result', (object,), result_mock)

    # Call method under test
    callback = CallbackModule()
    message = callback.v2_runner_on_failed(result)

    # Assert method returned expected value
    assert message == "FAILED! => {'msg': 'MOCK TEST', 'failed': True}\n"

# Generated at 2022-06-13 11:54:44.541207
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert (CallbackModule.CALLBACK_NAME == 'minimal')

# Generated at 2022-06-13 11:54:58.646688
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    CallbackModule()

# Generated at 2022-06-13 11:55:01.831299
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = None
    ignore_errors = False
    callback = CallbackModule()
    callback.v2_runner_on_failed(result,ignore_errors)


# Generated at 2022-06-13 11:55:04.569940
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    cb = CallbackModule()
    result = {'stderr': '', 'stdout': '', 'rc': 0, 'invocation': {'module_name': 'shell', 'module_args': 'echo OK'}}
    cb.v2_runner_on_ok(result)


# Generated at 2022-06-13 11:55:13.386060
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    """
    v2_runner_on_ok() returns stdout for runner on ok events
    """
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inventory  = Inventory(loader=loader, variable_manager=VariableManager(), host_list='localhost')

# Generated at 2022-06-13 11:55:25.836583
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback import CallbackModule

# Generated at 2022-06-13 11:55:31.824974
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    class Result:
        def __init__(self, result):
            self._result = result

    callbackmodule = CallbackModule()
    assert callbackmodule.v2_on_file_diff(Result({"diff": "Some diff"})) == None
    assert callbackmodule.v2_on_file_diff(Result({"diff": ""})) == None
    assert callbackmodule.v2_on_file_diff(Result({})) == None



# Generated at 2022-06-13 11:55:41.210506
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    import sys
    import os
    import unittest
    import test.support
    import tempfile
    import difflib

    output = ""

    class MockDisplay:

        def display(self, message, color=None, stderr=False, screen_only=False, log_only=False):
            global output
            output += message

    class MockCallbackModule(CallbackModule):

        def __init__(self):
            super(MockCallbackModule, self).__init__()
            self._display = MockDisplay()

    class TestAnsibleModule(unittest.TestCase):

        def test_file_diff(self):
            global output
            output = ""

            test_path = os.path.dirname(os.path.realpath(__file__))

# Generated at 2022-06-13 11:55:44.827535
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    obj = CallbackModule()
    assert 'CallbackModule' == obj.__class__.__name__
    assert obj.CALLBACK_VERSION == 2.0
    assert obj.CALLBACK_TYPE == 'stdout'
    assert obj.CALLBACK_NAME == 'minimal'


# Generated at 2022-06-13 11:55:47.266113
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    '''Check that callback module gets evaluated to class successfully'''
    expected = CallbackModule
    actual = CallbackModule
    assert actual == expected, "CallbackModule didn't evaluate to CallbackModule class"


# Generated at 2022-06-13 11:55:49.088354
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    test = CallbackModule()
    result = {"diff":'Test diff'}
    assert test.v2_on_file_diff(result) == None

# Generated at 2022-06-13 11:56:23.209823
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    from ansible.executor import task_result
    import tempfile
    with tempfile.NamedTemporaryFile() as temp:
        temp.file.write("""- hosts: localhost
  connection: local
  tasks:
    - name: "Test v2_on_file_diff"
      file:
        state: touch
        path: /etc/tmpfile
      register: result
    - name: "Test v2_on_file_diff"
      file:
        state: touch
        path: /etc/tmpfile
      register: result
""".encode('utf-8'))
        temp.file.flush()
        obj = CallbackModule()
        result = task_result.TaskResult(host=None, task=None, return_data=None)
        obj._display.display = lambda msg: msg
        obj

# Generated at 2022-06-13 11:56:32.365215
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    result = {'changed':'changed', 'ansible_job_id':'ansible_job_id', 'stderr_lines':'stderr_lines', 'end':'end'}
    result_out = {'result_items':'result_items', 'end':'end', '_files_changed':'_files_changed', '_files_deleted':'_files_deleted', '_files_failed':'_files_failed', '_files_modified':'_files_modified', '_files_replaced':'_files_replaced', '_files_skipped':'_files_skipped', '_files_unreachable':'_files_unreachable', '_play':'_play'}
    runner_on_ok = CallbackModule()

    runner_on_ok.v2_runner_on

# Generated at 2022-06-13 11:56:32.999669
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pass

# Generated at 2022-06-13 11:56:43.243312
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Set up the CallbackModule's attributes
    _display = 'test_display'
    _dump_results = 'test_dump_results'
    _clean_results = 'test_clean_results'
    _handle_warnings = 'test_handle_warnings'

    # Create a mock object to represent the actual Ansible Result object
    result = 'test_result'

    result.action = 'test_action'
    result.changed = 'test_changed'

    result._host = 'test_host'
    result._host.get_name = 'test_host_name'
    result._result = 'test_result'

    # Create a mock object to represent the actual Ansible Task object
    task = 'test_task'
    task.action = 'test_task_action'

    result._task = task

    # Create mock objects

# Generated at 2022-06-13 11:56:53.272122
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    test_class = CallbackModule()

# Generated at 2022-06-13 11:56:54.516737
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert issubclass(CallbackModule, CallbackBase)
    x = CallbackModule()

# Generated at 2022-06-13 11:56:58.486486
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # create class instance
    obj = CallbackModule()
    # create mock object for result
    result = Mock()
    filename = "mock_test"
    file_body_before = "mock file body before"
    file_body_after = "mock file body after"
    result._result = {'diff': {filename: [file_body_before,file_body_after]}}
    # execute method v2_on_file_diff
    obj.v2_on_file_diff(result)


# Generated at 2022-06-13 11:57:06.710028
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    callback = CallbackModule()

    # Test that there is no diff if the result['diff'] is empty
    result = {'diff': []}
    output = callback.v2_on_file_diff(result)
    assert output == None

    # Test that the diff is printed if the diff is not empty
    result = {'diff': [('/etc/passwd', {}, {'changed': True, 'diff': 'CHANGED\n'})]}
    output = callback.v2_on_file_diff(result)
    assert output == 'CHANGED\n'

# Generated at 2022-06-13 11:57:09.246948
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    print("\ntest_CallbackModule_v2_on_file_diff")
    cm = CallbackModule()
    result = {}
    cm.v2_on_file_diff(result)

test_CallbackModule_v2_on_file_diff()

# Generated at 2022-06-13 11:57:14.729792
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import sys
    import os

    # Local imports
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    
    cb = CallbackModule()
    result = {'stdout': 'test', 'stderr': 'test'}
    assert cb._command_generic_msg('localhost', result, "SUCCESS") == 'localhost | SUCCESS | rc=-1 >>\ntest\ntest\n\n'


# Generated at 2022-06-13 11:58:34.979319
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Testing CallbackModule.v2_runner_on_failed
    instance = CallbackModule()
    result = result()
    result.action = 'file'
    result.exception = 'unreachable'
    result.host = 'localhost'
    result.msg = 'test'
    result.stdout = 'test'
    result.task = 'testing'
    result._result = {'changed': False, 'msg': 'test', 'unreachable': '127.0.0.1'}
    task = task()
    task.action = 'file'
    task.name = 'testing'
    result._task = task
    result._host = '127.0.0.1'

# Generated at 2022-06-13 11:58:42.127281
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.module_utils._text import to_bytes

# Generated at 2022-06-13 11:58:46.640894
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import sys
    def _display(*args):
        sys.stdout.write(args[0])
    mock_display = MagicMock(_display)
    CallbackModule.__bases__ = (MagicMock(),)
    CallbackModule._display = mock_display
    callback = CallbackModule()
    callback.v2_runner_on_failed('Hello, World!')
    assert mock_display.call_count == 1

if __name__ == '__main__':
    result = 'Hello, World!'
    import pytest
    pytest.main('-s {0}'.format(__file__))

# Generated at 2022-06-13 11:58:47.773832
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    module = CallbackModule()
    assert module

# Generated at 2022-06-13 11:58:50.439378
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    testOb = CallbackModule()
    assert isinstance(testOb, CallbackBase)
    assert isinstance(testOb, CallbackModule)

# Generated at 2022-06-13 11:59:01.079116
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # Instantiate a CallbackModule object
    module = CallbackModule()
    # Instantiate a result object with file diff
    # result.get('_ansible_diff', None) returns the diff

# Generated at 2022-06-13 11:59:01.656235
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    pass

# Generated at 2022-06-13 11:59:02.966827
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    CallbackModule()


# Generated at 2022-06-13 11:59:18.115538
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Testcase 1:
    test_result = {
        'msg': 'Test message'
    }
    
    test_host = {
        'hostname' : 'testhost'
    }

    test_task = {
        'action' : 'test'
    }

    test_case = {
        '_result' : test_result,
        '_task' : test_task,
        '_host' : test_host
    }

    # Create instance of CallbackModule
    cb = CallbackModule()
    # Call method v2_runner_on_ok()
    cb.v2_runner_on_ok(test_case)

    # Testcase 2:
    test_result = {
        'msg': 'Test message'
    }
    

# Generated at 2022-06-13 11:59:24.310603
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    import ansible.inventory.host
    import ansible.playbook.play
    import ansible.playbook.task

    host = ansible.inventory.host.Host(name="localhost")
    host.set_variable('ansible_python_interpreter', '/usr/bin/python3')
    play = ansible.playbook.play.Play().load({'name': 'test_play'}, variable_manager={}, loader=None)
    task = ansible.playbook.task.Task().load({"action": {"module": "file", "args": "path=/usr/bin mode=0777"}}, play=play)

    # v2_runner_on_ok
    #
    # v2_runner_on_failed is called from v2_runner_on_ok and only references 
    # elements in result, so no need to