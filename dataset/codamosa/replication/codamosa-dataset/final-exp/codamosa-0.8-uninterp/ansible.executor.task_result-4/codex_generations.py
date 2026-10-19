

# Generated at 2022-06-12 21:54:50.150855
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    host = "127.0.0.1"
    task_fields = dict()
    class TaskResultTest(TaskResult):
        def __init__(self, host, task_fields):
            task = True
            return_data = True
            TaskResult.__init__(self, host, task, return_data, task_fields)

    # Test1: empty result
    task_result = TaskResultTest(host, task_fields)
    task_result._result = {}
    assert task_result.is_skipped() is False

    # Test2: test for loop results
    task_result._result = dict(results=[dict(skipped=True)])
    assert task_result.is_skipped() is True

    task_result._result = dict(results=[dict(skipped=True), dict(skipped=True)])


# Generated at 2022-06-12 21:54:54.533069
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():

    host = 'dummy-host'
    task = 'dummy-task'
    return_data = {'failed': True}
    task_fields = {'name': 'dummy-result'}
    result = TaskResult(host, task, return_data, task_fields)

    assert result.is_failed() == True

# Generated at 2022-06-12 21:55:02.775536
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    hostname = 'localhost'
    task_data = dict()
    task_data['module_name'] = 'hostname'
    task_data['module_args'] = 'name=localhost'
    task_data['name'] = 'hostname'
    task_data['action'] = 'hostname'
    task_data['no_log'] = True

    task_fields = dict()
    task_fields['module_name'] = 'hostname'
    task_fields['module_args'] = 'name=localhost'
    task_fields['name'] = 'hostname'
    task_fields['action'] = 'hostname'
    task_fields['no_log'] = True

    return_data = dict()
    return_data['cmd'] = 'hostname'
    return_data['rc'] = 0

# Generated at 2022-06-12 21:55:13.507603
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    return_data = {'changed': False, 'results': [{'changed': True, 'invocation': {'module_name': 'setup'}}]}
    task = TaskResult('dummy_host', {}, return_data)
    assert task.is_skipped() == False


# Generated at 2022-06-12 21:55:21.766068
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # TaskResult.clean_copy() removes keys from result
    original = {"failed": False, "output": "Blackbird singing in the dead of night"}
    task_result = TaskResult(None, None, original)
    result = task_result.clean_copy()._result
    assert 'output' in original
    assert 'output' not in result

    # TaskResult.clean_copy() can preserve status if no_log is set
    original = {"failed": False, "output": "Blackbird singing in the dead of night", "_ansible_no_log": True}
    task_result = TaskResult(None, None, original)
    result = task_result.clean_copy()._result
    assert 'output' in original
    assert 'output' not in result
    assert 'failed' not in result
    assert 'failed' in original

    # Task

# Generated at 2022-06-12 21:55:32.786756
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.vars.clean import module_response_deepcopy, strip_internal_keys
    
    input_dict = DataLoader().load("""{"failed": false, "msg": "All items completed", "results": [{"failed": false, "item": {"name": "foo"}, "msg": "All items completed"}, {"failed": false, "item": {"name": "bar"}, "msg": "All items completed"}], "changed": false}""")
    task_fields = {'name': 'example task'}
    host = {'name': 'test-host'}
    task = Task()
    
    result = TaskResult(host, task, input_dict, task_fields)
    assert result.is_failed()

# Generated at 2022-06-12 21:55:42.052824
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    task_fields = {
        'debugger': 'on_failed'
    }
    assert TaskResult('host', 'task', {'failed': True}, task_fields).needs_debugger() == True

    task_fields = {
        'debugger': 'on_unreachable'
    }
    assert TaskResult('host', 'task', {'unreachable': True}, task_fields).needs_debugger() == True

    task_fields = {
        'debugger': 'on_skipped'
    }
    assert TaskResult('host', 'task', {'skipped': True}, task_fields).needs_debugger() == True

    task_fields = {
        'debugger': 'always'
    }
    assert TaskResult('host', 'task', {'changed': False}, task_fields).needs_debugger() == True

# Generated at 2022-06-12 21:55:53.361688
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    '''Unit test for method clean_copy of class TaskResult'''
    from ansible.playbook.task import Task
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    mock_host = AnsibleUnicode(u'localhost')
    mock_task = Task()
    result = AnsibleSequence()
    item = AnsibleMapping()
    item.update(dict(failed=1, changed=1, skipped=0, unreachable=0))
    result.append(item)
    item = AnsibleMapping()
    item.update(dict(failed=1, changed=1, skipped=0, unreachable=0))

# Generated at 2022-06-12 21:55:59.731633
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    task = {'ignore_errors': False, 'action': 'debug', 'no_log': False, '_ansible_no_log': True}
    result = {'failed': True, 'ansible_job_id': '2979.977', 'stdout_lines': ['Hello, world!'], '_ansible_verbose_always': True, '_ansible_verbose_override': True, '_ansible_no_log': True, 'changed': False}

    cleaned_result = TaskResult('my_host', task, result).clean_copy()._result

    assert cleaned_result == {'censored': 'the output has been hidden due to the fact that \'no_log: true\' was specified for this result', '_ansible_verbose_override': True, 'changed': False}

# Generated at 2022-06-12 21:56:10.918942
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    import unittest

    class Test_TaskResult(unittest.TestCase):
        def setUp(self):
            self.loader = DataLoader()
            self.task = dict(action='debug', name='test')

        # Test 'skipped' method in class TaskResult
        def test_skipped_true(self):
            result = dict(skipped=True)
            task_result = TaskResult('127.0.0.1', self.task, result)
            self.assertTrue(task_result.is_skipped())

        def test_skipped_false(self):
            result = dict()
            task_result = TaskResult('127.0.0.1', self.task, result)
            self.assertFalse(task_result.is_skipped())


# Generated at 2022-06-12 21:56:26.200048
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    result = True
    meta = {'results': True}
    taskresult = TaskResult(None, None, meta)

    assert taskresult.is_skipped() == result


# Generated at 2022-06-12 21:56:35.015118
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    import json

    # Create a task
    block = Block()
    var_manager = VariableManager()
    task = Task()
    task._role = None
    task.action = 'debug'
    task.args = {'msg': 'hello'}
    task._parent = block
    task._role = None
    task.no_log = True
    task.notify = []
    task._block = block
    task._role_name = "common"
    task.loop = None
    task.when = None
    task.changed_when = False
    task.failed_when = False
    task.tags = []
    task.until = None

# Generated at 2022-06-12 21:56:44.728226
# Unit test for method clean_copy of class TaskResult

# Generated at 2022-06-12 21:56:55.136408
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # A fake task object
    task = type('task', (object,), {
        'action':''
    })()
    task.action = C._GET_URL_ACTION
    # A fake host object
    host = type('host', (object,), {
        'name':''
    })()
    host.name = "192.168.1.1"
    # A fake task_fields object
    task_fields = {}
    # A fake return_data, I skip the indentation due to the limitation of this forum.
    # You can refer to the class TaskResult in the source code code

# Generated at 2022-06-12 21:57:03.565731
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    loader = DataLoader()
    task = AnsibleTask()
    # Test for success
    return_data = '{"changed": false, "invocation": {"module_args": {"service_name": "nfs-server", "enabled": true, "state": "started", "force": false}}, "rc": 0, "stderr": "", "stderr_lines": [], "stdout": "", "stdout_lines": []}'
    task_result = TaskResult('host', task, loader.load(return_data))
    assert not task_result.is_failed()

    # Test for failure

# Generated at 2022-06-12 21:57:04.109685
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    assert True

# Generated at 2022-06-12 21:57:13.634031
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    import pytest

    from ansible.errors import AnsibleActionFail

    class Task:
        def __init__(self, action, ignore_errors=False):
            self.action = action
            self.ignore_errors = ignore_errors

        def get_name(self):
            return "not important"

    class Host:
        pass

    @pytest.fixture
    def tr():
        class TaskResult:
            def __init__(self, host, task, return_data=None):
                self._host = host
                self._task = task

                if isinstance(return_data, dict):
                    self._result = return_data.copy()
                else:
                    self._result = DataLoader().load(return_data) if return_data else None


# Generated at 2022-06-12 21:57:20.613474
# Unit test for method needs_debugger of class TaskResult

# Generated at 2022-06-12 21:57:32.610072
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    # import not done here
    # to enable test to be run
    # with --cov
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    test_host = '127.0.0.1'
    test_task_name = 'test task'
    test_task_action = 'setup'
    test_task_args = None

    # Create a play
    test_play = Play().load({
        'name': 'test play',
        'hosts': test_host,
        'gather_facts': 'no'
    }, variable_manager=VariableManager(), loader=None)

    # Create a task

# Generated at 2022-06-12 21:57:44.012538
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible import constants as C
    from ansible.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    class FakeTask:
        def __init__(self, name, no_log, ignore_errors, action):
            self.name = name
            self.no_log = no_log
            self.ignore_errors = ignore_errors
            self.action = action

        def get_name(self):
            return self.name


# Generated at 2022-06-12 21:57:58.309320
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    task_result = TaskResult(None, None, {'changed': False, 'invocation': {'module_name': 'debug'}, 'censored': 'the output has been hidden due to the fact that \'no_log: true\' was specified for this result', '_ansible_item_label': '/etc/ansible/roles/common/tasks/main.yml:18'})
    x = task_result.clean_copy()
    print(x._result)
    print(x.is_changed())
    print(x.is_failed())
    print(x.is_skipped())
    print(x.is_unreachable())

# Generated at 2022-06-12 21:58:09.597872
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    result1 = {
        "failed": False,
        "ansible_facts": {
            "os_family": "RedHat",
            "distribution": "CentOS",
            "distribution_major_version": "7"
        }
    }
    
    result2 = {
        "failed": "True",
        "ansible_facts": {
            "os_family": "RedHat",
            "distribution": "CentOS",
            "distribution_major_version": "7"
        }
    }
    
    result3 = {
        "failed": False,
        "ansible_facts": {
            "os_family": "RedHat",
            "distribution": "CentOS",
            "distribution_major_version": "7"
        }
    }
    

# Generated at 2022-06-12 21:58:21.416161
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    # Setup test variables
    host = ['192.168.33.10']
    task = 'task'
    return_data = dict()

    # Create TaskResult object
    result = TaskResult(host, task, return_data)

    # Test is_failed with no key in return_data
    assert not result.is_failed()

    # Test is_failed with key failed and value False in return_data
    return_data['failed'] = False
    result = TaskResult(host, task, return_data)
    assert not result.is_failed()

    # Test is_failed with key failed and value True in return_data
    return_data['failed'] = True
    result = TaskResult(host, task, return_data)
    assert result.is_failed()

    # Test is_failed with key failed_when_result and value False

# Generated at 2022-06-12 21:58:32.140183
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import json
    import unittest

    class TestTaskResult(unittest.TestCase):

        def setUp(self):
            self.data = {}

# Generated at 2022-06-12 21:58:40.175118
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult

    # Create a task that skipped
    block_1 = Block()
    task_1 = Task()
    task_1._parent = block_1
    task_1._role = None
    task_1._block = block_1
    task_1._play = None
    task_1._ds = {'name': "task_1", 'ignore_errors': None}
    task_1._loop = None
    task_1._context = PlayContext()

# Generated at 2022-06-12 21:58:46.249356
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    host = '127.0.0.1'
    task = 'test_task'
    task_fields = {'name': 'test task fields'}
    return_data = {'a': 'b', 'c': ['d', 'e'], 'f': 5, 'g': ['h']}
    result = TaskResult(host, task, return_data, task_fields)
    clean_result_task_fields = result.clean_copy()
    assert clean_result_task_fields._result is not return_data
    assert clean_result_task_fields._result is not result._result
    assert clean_result_task_fields._result == return_data

# Generated at 2022-06-12 21:58:55.857114
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    from ansible.playbook.task import Task

    task_fields = dict()
    host = 'dummy_host'
    res = dict()
    res['failed'] = False
    res['failed_when_result'] = False
    res['unreachable'] = False

    actual = TaskResult(host, Task(), res, task_fields).is_failed()
    assert actual == False

    res['failed'] = True
    actual = TaskResult(host, Task(), res, task_fields).is_failed()
    assert actual == True

    res['failed'] = False
    res['failed_when_result'] = True
    actual = TaskResult(host, Task(), res, task_fields).is_failed()
    assert actual == True

    res['failed_when_result'] = False
    res['unreachable'] = True
    actual

# Generated at 2022-06-12 21:59:01.335917
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    from ansible.playbook.task import Task
    task1 = Task()
    result1 = {'failed': True}
    task_result1 = TaskResult('localhost', task1, result1)
    assert task_result1.is_failed()

    task2 = Task()
    result2 = {'failed': False}
    task_result2 = TaskResult('localhost', task2, result2)
    assert not task_result2.is_failed()

    task3 = Task()
    result3 = {'failed_when_result': True}
    task_result3 = TaskResult('localhost', task3, result3)
    assert task_result3.is_failed()

    task4 = Task()
    result4 = {'results': [{'failed_when_result': True}, {'failed_when_result': True}]}


# Generated at 2022-06-12 21:59:08.304917
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    import unittest

    class TestTaskResult(unittest.TestCase):
        def setUp(self):
            self.task = {'ignore_errors': False, 'debugger': None}

        def test_with_default_args(self):
            t = TaskResult(None, self.task, {"failed": True})
            self.assertFalse(t.needs_debugger())


    # run tests
    unittest.main()

# Generated at 2022-06-12 21:59:19.770355
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    t = TaskResult('localhost', {}, {'failed': True, 'invocation': {'module_name': 'ping'}})
    t._result['_ansible_ignore_errors'] = True
    assert 'failed' not in t.clean_copy()._result
    assert 'invocation' not in t.clean_copy()._result
    assert 'changed' not in t.clean_copy()._result
    assert '_ansible_ignore_errors' not in t.clean_copy()._result

    t = TaskResult('localhost', {}, {'failed': True, 'invocation': {'module_name': 'ping'}})
    t.needs_debugger(True)
    assert 'failed' not in t.clean_copy()._result
    assert 'invocation' not in t.clean_copy()._result

# Generated at 2022-06-12 21:59:31.528634
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    task_fields = dict(name='fake task')

    task = Task()
    task._role = None
    task.action = 'setup'
    task.args = dict()
    task._parent = PlayContext()
    task._parent.become = False
    task._parent.become_method = 'sudo'
    task._parent.become_user = None

    # test that "debugger" field is not copied
    # test that "debugger" field can be handled by is_failed

# Generated at 2022-06-12 21:59:41.429196
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    # Check that is_failed returns False
    # when failed key not in the result
    assert TaskResult('hostname', 'task', {}).is_failed() == False

    # Check that is_failed returns False
    # when failed key is False in the result
    assert TaskResult('hostname', 'task', {'failed': False}).is_failed() == False

    # Check that is_failed returns False
    # when failed key is True in the result
    assert TaskResult('hostname', 'task', {'failed': True}).is_failed() == True

# Generated at 2022-06-12 21:59:53.081936
# Unit test for method clean_copy of class TaskResult

# Generated at 2022-06-12 22:00:02.754821
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task

    task = Task()
    task_fields = dict()

    # When an action is debugger and we are in a failed state, we should
    # need a debugger, even if it is not enabled globally
    task.action = 'debugger'
    task_fields = {'failed': True}

    assert TaskResult(None, task, task_fields).needs_debugger(globally_enabled=False) == True

    # If a debugger is disabled globally, we should not need it
    assert TaskResult(None, task, task_fields).needs_debugger(globally_enabled=False) == False

    # If a debugger is enabled globally and the task has failed, we should
    # need to run the debugger

# Generated at 2022-06-12 22:00:14.390397
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import json
    from ansible.vars.clean import module_response_deepcopy, strip_internal_keys
    import sys

    class Task:
        def __init__(self, no_log=False, action="run"):
            self.no_log = no_log
            self.action = action


# Generated at 2022-06-12 22:00:22.704913
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    fake_host = "fakehost1"
    mock_task = None
    mock_fields = None

    test_case_failed_key = dict(failed=True,
                                results=None)
    result_test_case_failed_key = TaskResult(fake_host,
                                             mock_task,
                                             test_case_failed_key,
                                             mock_fields)
    assert result_test_case_failed_key.is_failed() is True

    test_case_failed_when_result_key = dict(failed_when_result=True,
                                            results=None)

# Generated at 2022-06-12 22:00:30.218344
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task, TaskResult
    from ansible.plugins.callback.default import CallbackModule
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from copy import deepcopy

    hosts_data = {
        'host1': {
            'vars': {
                'ansible_user': 'root',
                'ansible_password': 'secret'
            }
        },
        'host2': {
            'vars': {
                'ansible_user': 'root',
                'ansible_password': 'letmein'
            }
        }
    }

    # Create a Task
    task_fields = {
        'ignore_errors': False,
        'action': 'debug'
    }
    task = Task(task_fields=task_fields)
   

# Generated at 2022-06-12 22:00:35.804209
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    t_result = TaskResult(None, None, {
        "foo": 1,
        "bar": "baz",
        "unreachable": True,
        "message": "msg",
        "invocation": {
            "module_name": "setup",
            "module_args": ""
        },
        "_ansible_verbose_always": True,
        "changed": False
    })
    clean_copy = t_result.clean_copy()
    assert len(clean_copy._result) == 3
    assert "foo" in clean_copy._result
    assert clean_copy._result["foo"] == 1
    assert "bar" in clean_copy._result
    assert clean_copy._result["bar"] == "baz"
    assert "unreachable" in clean_copy._result

# Generated at 2022-06-12 22:00:46.261879
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host

    fake_task = Task()
    fake_task.action = 'aFakeAction'
    fake_task._role = None
    fake_host = Host(name='fakehost')
    fake_result = {'a': '1', '_ansible_verbose_always': '2', 'b': '3'}
    fake_task_fields = {'aFakeField': 'aFakeValue'}
    obj = TaskResult(fake_host, fake_task, fake_result, fake_task_fields)

    # obj.clean_copy() is called with empty variables
    obj._result = {}
    obj_clean = obj.clean_copy()
    assert obj_clean._result == {}

    # obj.clean_copy() is called with _

# Generated at 2022-06-12 22:00:54.993875
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    return_data = {
        "changed": False,
        "msg": "All items completed",
        "results": [
            {
                "changed": False,
                "item": "foo",
                "msg": ""
            },
            {
                "changed": False,
                "item": "bar",
                "msg": ""
            }
        ]
    }

    for ignore_change in [False, True]:
        for ignore_errors in [False, True]:
            task = type('',(object,), {'action': 'debug', 'no_log': not ignore_change, 'ignore_errors': ignore_errors})()
            for error in [False, 'failed', 'unreachable', 'failed_when_result']:
                if error:
                    return_data[error] = True
                else:
                    return_data

# Generated at 2022-06-12 22:01:15.441703
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # create host instance
    # create task instance
    # create TaskResult instance
    task_fields = {'name': 'test_task'}
    task_result_data = {'stdout': 'test_result_stdout', 'cmd': 'test_result_command', 'rc': 0}
    t_r = TaskResult('test_host', 'test_task', task_result_data, task_fields)
    # create expected results
    expected_results = {'stdout': 'test_result_stdout', 'cmd': 'test_result_command', 'rc': 0, '_ansible_item_label': 'test_task'}
    # get actual result
    actual_result = t_r.clean_copy()
    # test if actual result equals expected result
    assert expected_results == actual_result._result

# Generated at 2022-06-12 22:01:23.930358
# Unit test for method is_skipped of class TaskResult

# Generated at 2022-06-12 22:01:27.544808
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    """
    task_result = TaskResult(host, task, return_data, task_fields=None)
    task_result.is_failed()
    """

    task_result = TaskResult('hostname', 'task', {'failed': False}, 'task_fields')
    assert not task_result.is_failed()

# Generated at 2022-06-12 22:01:32.336435
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():

    task_result = TaskResult(host=None, task=None, return_data={
        'results': [
            {'skipped': True},
            {'skipped': True},
            {'skipped': True}
        ]
    })

    assert task_result.is_skipped(), "Task should be cunsidered skipped"



# Generated at 2022-06-12 22:01:43.210450
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    """
    Method clean_copy of class TaskResult should return a 'clean' taskresult object
    """
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader

    h = 'example.com'
    t = Task()

# Generated at 2022-06-12 22:01:51.223900
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    class MyTask:
        def __init__(self):
            self.action = 'copy'
            self.no_log = False

    # test failed_when_result
    task = MyTask()
    host_result = {'changed': True, 'failed_when_result': True}
    task_result = TaskResult(None, task, host_result)
    assert(task_result.is_failed())

    # test failed
    host_result = {'changed': True, 'failed': True}
    task_result = TaskResult(None, task, host_result)
    assert(task_result.is_failed())

    # test results
    host_result = {'changed': True, 'results': [{'changed': True, 'failed_when_result': True}]}

# Generated at 2022-06-12 22:02:01.873592
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    task_result = TaskResult(None, None, '{"failed": true}')
    assert(task_result.is_failed())

    task_result = TaskResult(None, None, '{"notfailed": true}')
    assert(not task_result.is_failed())

    task_result = TaskResult(None, None, '{"failed": false}')
    assert(not task_result.is_failed())

    task_result = TaskResult(None, None, '{"results": [{"failed": "si", "changed": "si"}, {"failed": false, "changed": "si"}]}')
    assert(task_result.is_failed())

    task_result = TaskResult(None, None, '{"results": [{"failed": false, "changed": "si"}, {"failed": "si", "changed": "si"}]}')

# Generated at 2022-06-12 22:02:14.262614
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import unittest


# Generated at 2022-06-12 22:02:20.442309
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    task_result = TaskResult("host", "task", {"failed": True})

    # assert failed returns True
    assert task_result.is_failed()

    result = dict(
        failed=False,
        results=[
            dict(
                failed=True
            )
        ]
    )
    task_result = TaskResult("host", "task", result)

    # assert failed returns True
    assert task_result.is_failed()


# Generated at 2022-06-12 22:02:30.994677
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    task = MockTask()

    result_ok = { 'failed': False, 'msg': 'hello' }
    taskresult = TaskResult('host', task, result_ok)
    taskresult_copy = taskresult.clean_copy()
    assert taskresult_copy._result == result_ok
    assert taskresult_copy._result is not result_ok
    assert taskresult_copy._host == 'host'
    assert taskresult_copy._task is task
    assert taskresult_copy._task_fields == {}

    result_fail = { 'failed': True, 'msg': 'hello', '_ansible_no_log': False, 'failed_when_result': False }
    taskresult = TaskResult('host', task, result_fail)
    taskresult_copy = taskresult.clean_copy()
    assert taskresult_copy._result == result_

# Generated at 2022-06-12 22:02:43.192131
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    task_result_1 = TaskResult('host_1', 'task_1', {'failed': True})
    task_result_2 = TaskResult('host_1', 'task_1', {'results': [{'failed': True}]})
    task_result_3 = TaskResult('host_1', 'task_1', {'results': [{'failed': False}, {'failed': True}]})

    assert(task_result_1.is_failed() == True)
    assert (task_result_2.is_failed() == True)
    assert (task_result_3.is_failed() == True)


# Generated at 2022-06-12 22:02:50.395210
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    class MockTask:
        def __init__(self, action, ignore_errors):
            self.action = action
            self.ignore_errors = ignore_errors

    class MockHost:
        def __init__(self, hostname):
            self.name = hostname

    def test_case(action, ignore_errors, globally_debugged, failed, unreachable, skipped, expected_result):
        """Generates a parametrized unit test case"""

        task = MockTask(action, ignore_errors)
        host = MockHost('foohost')

        if failed:
            assert not unreachable
            assert not skipped

        if unreachable:
            assert not failed
            assert not skipped

        if skipped:
            assert not failed
            assert not unreachable

        result = TaskResult(host, task, {})

# Generated at 2022-06-12 22:02:58.369884
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    task = object()
    data = {'failed': True}
    result = TaskResult(None, task, data)

    assert result.is_failed() == True

    data = {'failed': False}
    result = TaskResult(None, task, data)

    assert result.is_failed() == False

    data = {}
    result = TaskResult(None, task, data)

    assert result.is_failed() == False

    data = {'failed': False, 'results': [{'failed': True}]}
    result = TaskResult(None, task, data)

    assert result.is_failed() == True


# Generated at 2022-06-12 22:03:08.635115
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    import json

    result = {
        "module_stdout": "The quick brown fox jumps over the lazy dog.",
        "module_stderr": "The quick brown fox jumps over the lazy dog.",
        "failed_when_result": True,
        "invocation": {
            "module_args": {
                "name": "foo",
                "debug": True,
                "state": "absent"
            }
        },
        "warnings": [
            "Consider using service module rather than running service"
        ],
        "_ansible_no_log": True,
        "changed": True,
        "_ansible_module_name": "yum",
        "_ansible_parsed": True,
        "msg": "foo removed"
    }

    task = None
    host = None

    task_result = Task

# Generated at 2022-06-12 22:03:15.495183
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.vars.unsafe_proxy import UnsafeProxy

    fake_loader = DataLoader()
    host = UnsafeProxy({'name': 'localhost', 'vars': {}})
    task = Task()
    task.action = 'debug'

    # host variable is set to True
    host.vars['ansible_debugger'] = True
    result = TaskResult(host, task, {}, {})
    assert result.needs_debugger(globally_enabled=False) is True
    assert result.needs_debugger(globally_enabled=True) is True

    # task variable is set to True
    result._task_fields['debugger'] = True
    assert result.needs_debugger(globally_enabled=False) is True

# Generated at 2022-06-12 22:03:23.273715
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # test with a verbose_always debug task
    verbose_debug_task = {
        'name': 'my_verbose_debug_task',
        'action': 'debug',
        'args': {
            'msg': 'This is a message including %HOSTNAME%',
            'verbosity': 4
        },
        '_ansible_verbose_always': True
    }
    verbose_debug_result = {
        'changed': False,
        'msg': 'This is a message including myhostname',
        '_ansible_verbose_override': True,
        '_ansible_item_label': 'my_item',
        '_ansible_no_log': False,
        '_ansible_verbose_always': True,
        'failed': False
    }

# Generated at 2022-06-12 22:03:30.318375
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from collections import namedtuple

    MockHost = namedtuple('Host', 'get_name get_vars')
    host = MockHost('127.0.0.1', get_vars=lambda:dict())
    task = namedtuple('Task', 'get_name action')
    task = task('TASK', 'debug')
    copy = dict(failed=True,
                stdout='stdout',
                stderr='stderr',
                invocation=dict(module_name='debug',
                                module_args=dict(),
                                module_vars=dict()),
                _ansible_no_log=True,
                _ansible_item_label='item')
    tr = TaskResult(host, task, copy)
    clean_copy = tr.clean_copy()


# Generated at 2022-06-12 22:03:42.248842
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    task = MagicMock()
    task.action = 'debug'
    task.no_log = False

    _task_fields = {}
    _task_fields['name'] = 'Dummy-Test'
    _task_fields['ignore_errors'] = False

    return_data = {}
    return_data['failed'] = False
    return_data['skipped'] = False
    return_data['changed'] = False
    return_data['ansible_module_results'] = {'invocation':{'module_args':{'name':'ansible'}}}
    return_data['ansible_module_results']['msg'] = 'Dummy message'
    return_data['ansible_module_results']['changed'] = False

# Generated at 2022-06-12 22:03:54.201882
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import json
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader

    task_fields = dict(
        action='debug',
        name='Test TaskResult.clean_copy',
        ignore_errors=True,
        register='somevar',
        debugger='on_failed',
    )

    task = Task()
    task.action = 'debug'
    task.ignore_errors = True
    task.register = 'somevar'
    task._parent_block = None
    task._role = None
    task._task_fields = task_fields
    task.set_loader(action_loader)

    # TaskResult.clean_copy should not censor debug output when the result
    # indicates the task failed, unless ignore_errors is set

# Generated at 2022-06-12 22:04:04.407671
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    result = TaskResult(None, None, return_data={'foo': 'bar'})
    assert False == result.is_failed()

    result = TaskResult(None, None, return_data={'foo': 'bar', 'failed': True})
    assert True == result.is_failed()

    result = TaskResult(None, None, return_data={'foo': 'bar', 'results': []})
    assert False == result.is_failed()

    result = TaskResult(None, None, return_data={'foo': 'bar', 'results': [{'failed': True}]})
    assert True == result.is_failed()

    result = TaskResult(None, None, return_data={'foo': 'bar', 'results': [{'failed': False}, {'failed': True}]})
    assert True == result.is_failed

# Generated at 2022-06-12 22:04:27.166615
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    class Task:
        def __init__(self):
            self.name = 'test_task'
            self.action = 'test_action'
            self.debugger = 'on_failed'

    class Host:
        def __init__(self, hostname):
            self.name = hostname
            self.hostname = hostname

    task = Task()
    host = Host('host')


# Generated at 2022-06-12 22:04:33.805427
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    import os
    import json
    from ansible.module_utils._text import to_bytes

    # load test data
    module_data = None
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'module_result.json')) as f:
        module_data = f.read()

    # convert it to byte string
    module_data = to_bytes(module_data, errors='strict')
    # convert it to json
    module_data = json.loads(module_data)

    # create a TaskResult object
    tr = TaskResult(host='localhost', task=None, return_data=module_data)

    # convert it to byte string
    module_data = to_bytes(json.dumps(module_data), errors='strict')
    #