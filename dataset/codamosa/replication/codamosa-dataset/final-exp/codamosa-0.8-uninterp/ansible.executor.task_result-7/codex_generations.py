

# Generated at 2022-06-12 21:54:50.370608
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    assert TaskResult('host', 'task', {'skipped': True}).is_skipped()
    assert TaskResult('host', 'task', {'results': [{'skipped': True}]}).is_skipped()
    assert TaskResult('host', 'task', {'results': [{'skipped': True}, {'skipped': True}]}).is_skipped()
    assert not TaskResult('host', 'task', {'results': [{'skipped': False}]}).is_skipped()
    assert not TaskResult('host', 'task', {}).is_skipped()

# Generated at 2022-06-12 21:54:57.006597
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    from ansible.playbook.task import Task

    # Test for bug 1447619
    task = Task()
    task.when = True
    task.action = 'foobar'
    task.name = 'Test task'
    task.deprecated_when_value = True

    result = TaskResult('fake_host', task, {
        'changed': False,
        'failed': True,
        'failed_when_result': True,
        'rc': 100
    })

    assert(result == True)

# Generated at 2022-06-12 21:55:04.135419
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    result = {
        '_ansible_parsed': True,
        '_ansible_ignore_errors': True,
        '_ansible_item_result': False,
        '_ansible_no_log': False,
        '_ansible_notify': [],
        '_ansible_item_label': 'included_tasks',
        '_ansible_delegated_vars': {
            'ansible_host': '127.0.0.1',
            'ansible_port': 22,
            'ansible_user': 'root',
            'ansible_connection': 'ssh'
        },
        'failed': False,
        'changed': False
    }

    clean_result = TaskResult('host', 'task', result).clean_copy()._result
    assert 'failed' in clean

# Generated at 2022-06-12 21:55:13.083787
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    test_cases = [{'host': 'host', 'task': 'task', 'result': True, 'msg': 'should return True if the failed key is in the result section'},
                  {'host': 'host', 'task': 'task', 'result': False, 'msg': 'should return False if the failed key is not in the result section'}]

    for test_case in test_cases:
        if test_case['result']:
            result = {'failed': True}
        else:
            result = {'failed': False}

        taskResult = TaskResult(test_case['host'], test_case['task'], result)
        assert test_case['result'] == taskResult.is_failed(), test_case['msg']

# Generated at 2022-06-12 21:55:21.498139
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.vars.manager import VariableManager
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.executor.task_queue_manager import TaskQueueManager

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(loader.load_inventory('test/unit/ansible/config/hosts'))
    play_context = PlayContext()
    play_context.network_os = 'default'
    play_context.remote_addr = ''
    play_context.port = 2222
    play

# Generated at 2022-06-12 21:55:32.475225
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    import copy
    task_result = dict(
        results=[
            dict(
                failed=False,
                skipped=True,
                _ansible_item_label='item0',
            ),
            dict(
                failed=False,
                skipped=False,
                _ansible_item_label='item1',
            ),
        ],
    )
    task_result_2 = copy.deepcopy(task_result)
    task_result_2['results'][0]['failed'] = True
    task_result_3 = copy.deepcopy(task_result)
    task_result_3['results'][-1]['failed'] = True
    task_result_4 = copy.deepcopy(task_result)
    task_result_4['failed'] = True

# Generated at 2022-06-12 21:55:36.993102
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    host = None
    task = None
    return_data = None
    task_fields = None
    taskResult = TaskResult(host, task, return_data, task_fields)

    assert taskResult.needs_debugger(True) is False
    assert taskResult.needs_debugger(False) is False

# Generated at 2022-06-12 21:55:45.400456
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    # There are two kinds of skipped tasks:
    #   1) normal tasks with a skipped flag
    #   2) loop tasks with a skipped flag in each item result
    # The following tests cover both cases.
    task_fields = {}
    task = MockTask()
    host = MockHost('hostname')
    result = TaskResult(host, task, {}, task_fields)

    # Not skipped, no result
    assert False == result.is_skipped()

    # Not skipped, some result
    result._result = {'foo': 'bar'}
    assert False == result.is_skipped()

    # Skipped
    result._result = {'foo': 'bar', 'skipped': True}
    assert True == result.is_skipped()

    # Loop with all item results skipped

# Generated at 2022-06-12 21:55:55.342398
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    # Tests True scenario when failed: true is present in result (in dictionary format)
    # This is the case when we have condition of failed_when in the task
    task = TaskResult(None, None, {'failed': True})
    assert task.is_failed() == True
    # Tests False scenario when failed: false is present in result (in dictionary format)
    task = TaskResult(None, None, {'failed': False})
    assert task.is_failed() == False
    # Tests True scenario when failed: true is present in result (in squashed format)
    task = TaskResult(None, None, [{'failed': True}])
    assert task.is_failed() == True
    # Tests False scenario when failed: false is present in result (in squashed format)

# Generated at 2022-06-12 21:55:58.666188
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    host = None
    task = None
    return_data = {'results': [{'skipped': True}, {'skipped': True, 'msg': 'msg'}]}
    task_fields = None
    taskresult = TaskResult(host, task, return_data, task_fields)

    assert taskresult.is_skipped()

# Generated at 2022-06-12 21:56:24.703400
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    # Prepare the input to the function
    mock_host = "host1"
    mock_task = {"debugger": "on_failed", "ignore_errors": True, "action": "debug"}
    mock_return_data = {"failed": True, "failed_when_result": False, "skipped": False, "unreachable": False}
    mock_task_fields = {"name": "my_task"}

    # create a TaskResult object
    task_result = TaskResult(mock_host, mock_task, mock_return_data, mock_task_fields)

    # Call the method under test
    actual_result = task_result.needs_debugger()

    # Verify the result
    assert actual_result == False

    # Change the input to the method needs_debugger

# Generated at 2022-06-12 21:56:33.653606
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    result = TaskResult(None, None, None)
    assert result.needs_debugger() == False

    condition = {
        (True,  False, False, False, False, False): False,
        (True,  False, True,  False, False, True ): False,
        (True,  False, False, True,  False, False): True,
        (True,  False, False, False, False, False): True,
        (False, True,  True,  False, False, False): False,
        (False, False, False, False, True,  False): True,
        (False, False, False, False, False, False): True,
    }

   

# Generated at 2022-06-12 21:56:39.610348
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # create a TaskResult object
    import unittest
    import ansible.playbook.task_include as task_include
    import ansible.playbook.task as task

    class TaskTest(unittest.TestCase):
        def test_TaskResult_clean_copy(self):
            task_fields = {}
            task_fields['action'] = 'copy'
            host = '127.0.0.1'
            task_ds = dict(
                when='any',
                module='copy',
                args=dict(
                    src='/etc/hosts',
                    dest='/tmp/hosts',
                ),
            )
            return_data = dict(
                changed=True,
                md5sum='False',
                msg='File copy successfull',
                src='/etc/hosts',
            )
            t

# Generated at 2022-06-12 21:56:50.133184
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    task_fields = dict()


# Generated at 2022-06-12 21:56:58.982678
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():

    return_data = dict(
        failed = True,
    )

    task_fields = dict(
        ignore_errors = False
    )

    result = TaskResult(None, None, return_data, task_fields)
    assert(result.is_failed() == True)

    return_data = dict(
        failed = True,
    )

    task_fields = dict(
        ignore_errors = True
    )

    result = TaskResult(None, None, return_data, task_fields)
    assert(result.is_failed() == False)

    return_data = dict(
        failed_when_result = True,
    )

    task_fields = dict()

    result = TaskResult(None, None, return_data, task_fields)
    assert(result.is_failed() == True)

# Generated at 2022-06-12 21:57:06.482694
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import json
    from ansible.plugins.loader import action_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)

# Generated at 2022-06-12 21:57:15.829206
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    class Task(object):
        ''' Mock task object '''
        def __init__(self, action, debugger, ignore_errors=False):
            self.action = action
            self.debugger = debugger
            self.ignore_errors = ignore_errors

    # test cases

# Generated at 2022-06-12 21:57:23.856084
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    mock_t = Task()
    mock_t._role = None
    mock_vars = VariableManager()
    tr = TaskResult('https://some.host.name.com', mock_t, {'failed': False})

    # test is_failed()
    assert tr.is_failed() == False, "Test 'tr.is_failed()' failed"

    # test global debugger with debug task
    mock_t._role = None
    mock_t.action='debug'
    tr = TaskResult('https://some.host.name.com', mock_t, {'failed': False})
    assert tr.needs_debugger(True) == True, "Test 'tr.needs_debugger(True)' failed"

    # test global

# Generated at 2022-06-12 21:57:34.343266
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    task = dict()
    task['name'] = 'dummy'
    task['action'] = 'test'
    task['register'] = 'testvar'

    # test results is None
    tr = TaskResult(dict(), task, None)
    assert tr.is_skipped() == False

    # test results is list
    results = []
    results.append(dict())
    results.append(dict())
    results.append(dict())

    results[0]['skipped'] = True
    results[1]['skipped'] = False
    tr = TaskResult(dict(), task, dict())
    tr._result['results'] = results
    assert tr.is_skipped() == False

    del results[1]['skipped']
    tr._result['results'] = results
    assert tr.is_skipped() == True

   

# Generated at 2022-06-12 21:57:46.748327
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    class Task:
        def __init__(self, action, ignore_errors=None, debugger=None):
            self.action = action
            self.ignore_errors = ignore_errors
            self.debugger = debugger
        def get_name(self):
            return self.name

    # Setup mock objects
    import types
    import ansible.vars
    def save_TASK_DEBUGGER_ENABLED(value):
        TASK_DEBUGGER_ENABLED.was_called = True
        TASK_DEBUGGER_ENABLED.value = value
    def restore_TASK_DEBUGGER_ENABLED():
        ansible.vars.TASK_DEBUGGER_ENABLED = TASK_DEBUGGER_ENABLED.saved


# Generated at 2022-06-12 21:57:59.404195
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():

    # create a TaskResult object
    t = TaskResult('localhost', 'setup', {'setup' : {'a' : 1}}, {'name' : 'setup', 'debugger' : 'on_failed'})
    assert t.needs_debugger(True) == False

    t = TaskResult('localhost', 'setup', {'setup' : {'failed' : True, 'changed' : False}}, {'name' : 'setup', 'debugger' : 'on_failed'})
    assert t.needs_debugger(True) == True

    t = TaskResult('localhost', 'setup', {'setup' : {'failed' : True, 'changed' : False}}, {'name' : 'setup', 'debugger' : 'on_failed', 'ignore_errors' : True})

# Generated at 2022-06-12 21:58:10.391392
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    result = {'failed': False, 'changed': True, 'msg': "No message was provided", 'invocation': {'module_name': 'setup', 'module_args': {}, 'module_complex_args': {}}, '_ansible_no_log': False, '_ansible_item_result': True, '_ansible_verbose_always': True}
    task_fields = {'name': 'setup', 'ignore_errors': False, 'debugger': 'on_failed', 'action': 'setup'}
    test_object = TaskResult('myhost', 'mytask', result, task_fields)
    clean_result = test_object.clean_copy()
    assert clean_result._result == {'msg': 'No message was provided', '_ansible_verbose_always': True}


# Generated at 2022-06-12 21:58:11.966935
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    pass

# Generated at 2022-06-12 21:58:22.523809
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    host = "localhost"
    task = {
        "name": "task",
        "action": "task"
    }
    return_data = {
        "failed": True,
        "failed_when_result": False,
        "results": [{
            "failed": True,
            "failed_when_result": False
        }, {
            "failed": True,
            "failed_when_result": False
        }]
    }
    result = TaskResult(host, task, return_data)

    # Test with failed
    assert result.is_failed()

    # Test with failed in results
    return_data["failed"] = False
    result = TaskResult(host, task, return_data)
    assert result.is_failed()

    # Test with no failed
    return_data["failed"] = False
    return

# Generated at 2022-06-12 21:58:33.027975
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import ansible.playbook.task
    task = ansible.playbook.task.Task()
    host = '127.0.0.1'
    task_fields = None

# Generated at 2022-06-12 21:58:41.742884
# Unit test for method clean_copy of class TaskResult

# Generated at 2022-06-12 21:58:53.107967
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():

    class MockTask:
        def __init__(self, action, ignore_errors, debugger):
            self.action = action
            self.ignore_errors = ignore_errors
            self.debugger = debugger
    class MockHost:
        def __init__(self):
            pass

    def debugger_host_set(t):
        return {'on_unreachable': True, 'on_failed': True}

    #
    # failed, globally_enabled=False
    #
    _mock_task = MockTask('some action', False, 'on_failed')
    _mock_result = {'failed': True, 'unreachable': False}
    _mock_host = MockHost()
    _mock_task_fields = {'debugger': 'on_failed'}

# Generated at 2022-06-12 21:59:02.767341
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    from ansible import module_utils
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    class TestTask(Task):
        def __init__(self, name, task_executor):
            self.name = name
            self._task_executor = task_executor

        def get_name(self):
            return self.name

        def get_action(self):
            return self.action

        def set_loader(self, loader):
            pass

        def set_inventory(self, inventory):
            pass

        def set_variable_manager(self, variable_manager):
            pass

        def load_tags(self):
            self.tags = []

        def has_tags(self):
            return False


# Generated at 2022-06-12 21:59:12.617297
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    """Test the correct evaluation of is_failed()
    """
    # bad = True
    # bad = False
    # failed = True
    # failed = False
    # failed_when_result = True
    # failed_when_result = False
    # results = not present
    # results = []

    # results = [{}]

    # task = dict
    # task = object

    # task_fields = dict
    # task_fields = object

    # will always fail
    bad = False
    failed = False
    failed_when_result = True
    results = []
    results.append({})
    task = dict()
    task_fields = dict()
    test_obj = TaskResult('host', task, {'failed': failed, 'failed_when_result': failed_when_result, 'results': results})

# Generated at 2022-06-12 21:59:23.718449
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    class DummyHost: pass
    class DummyTask: pass

    # Setup
    t = DummyTask()
    h = DummyHost()

# Generated at 2022-06-12 21:59:50.148186
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    task_fields = {'name':'test_task',
                   'ignore_errors': True}
    result = {'invocation':{'module_name':'debug'},
              'ansible_facts':{'a':'b'},
              'changed': True,
              'failed_when_result': True,
              '_ansible_verbose_always': True,
              '_ansible_item_label': {'b':'c'},
              '_ansible_no_log': True,
              '_ansible_verbose_override': True,
              'results':[{'failed':True,
                          'skipped': False,
                          'unreachable': False}],
              }
    r = TaskResult(None, None, result, task_fields=task_fields)
    r2 = r

# Generated at 2022-06-12 22:00:00.919818
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    ld = DataLoader()
    task = Task()
    task.no_log = True
    task.action = 'debug'
    data = {'censored': 'the output has been hidden due to the fact that \'no_log: true\' was specified for this result'}
    t = TaskResult(None, task, ld.load(data))
    assert t.clean_copy()._result == data
    t = TaskResult(None, task, ld.load(data), dict(name='test'))
    assert t.clean_copy()._result == data
    t = TaskResult(None, task, ld.load(data), dict(name='test', debugger="on_failed"))
    assert t.clean_copy()._result == data
    # Notice that '_ansible_no_log' is skipped

# Generated at 2022-06-12 22:00:12.072903
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    task = MockTask(name='mock_task', ignore_errors=False)
    host = MockHost('mock_host')
    task_fields = dict(name='task_fields', ignore_errors=True)
    data = dict(failed=False, changed=False, skipped=False, unreachable=False, msg='ok', _ansible_no_log=False)

    # Testing instance with _result as dict
    result = TaskResult(host, task, data, task_fields)

    copy = result.clean_copy()

    # Testing Result instance
    assert copy._host == host
    assert copy._task == task
    assert copy._task_fields == task_fields
    assert copy._result == data

    # Testing instance with _result as list of dicts

# Generated at 2022-06-12 22:00:21.401311
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    import unittest
    import ansible.playbook.task_include

    class FakeTaskResult(TaskResult):
        def __init__(self, result, task_fields, task=None, host=None):
            super(FakeTaskResult, self).__init__(host, task, result, task_fields)

    TASK_FIELDS = {
        'debugger': 'never',
        'ignore_errors': False,
        'name': 'do something',
    }

    RESULT = {
        'failed': False,
        'unreachable': False,
    }


# Generated at 2022-06-12 22:00:31.446676
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    task_fields = dict(debugger="always", ignore_errors=True)
    task = dict()
    task["action"] = "pause"

    # Test 1: test when globally_enabled is False
    task_result = TaskResult(None, task, None, task_fields=task_fields)
    assert not task_result.needs_debugger(False)

    # Test 2: test when globally_enabled is True
    task_result = TaskResult(None, task, None, task_fields=task_fields)
    assert task_result.needs_debugger(True)

    # Test 3: test when globally_enabled is True and an action that does not support debugging
    task_result = TaskResult(None, {"action" : "shell"}, None, task_fields=task_fields)
    assert not task_result.needs_debugger(True)

# Generated at 2022-06-12 22:00:43.167989
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    class Task:
        def __init__(self, no_log=False, action='', ignore_errors=False):
            self.no_log = no_log
            self.action = action
            self.ignore_errors = ignore_errors

    class Host:
        name = "test_host"

    task_fields = {'name': 'test_task', 'debugger': 'always'}

    # case 1: no_log = False, action = 'setup', ignore_errors = False
    task = Task(no_log=False, action='setup', ignore_errors=False)
    host = Host()

# Generated at 2022-06-12 22:00:51.226903
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()

    # Test case #1

# Generated at 2022-06-12 22:01:02.806260
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():

    class TestHost(object):
        def __init__(self, name):
            self.name = name

    class TestTask(object):
        def __init__(self, name, action, debugger, ignore_errors):
            self.name = name
            self.action = action
            self.debugger = debugger
            self.ignore_errors = ignore_errors

    # No debugger option set on task => always returns False unles debugger is enabled globally
    task = TestTask('test_task', 'apt', None, False)
    result = TaskResult(TestHost('host'), task, {'failed': True})
    assert result.needs_debugger(True) == True
    assert result.needs_debugger(False) == False

    # debugger option set to always => always returns True

# Generated at 2022-06-12 22:01:09.006218
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.vars.hostvars import HostVars

    loader = DataLoader()

    # create sample host
    host_vars = HostVars(loader=loader, changed_when=None, task_vars={'colors': ['red', 'blue'], 'hostvars': {'myhost': {'nested': 'var'}, 'otherhost': {'nested': 'var'}}})
    host = {
        'name': 'localhost',
        'vars': host_vars,
    }

    # create sample task fields
    task_fields = {
        'action': 'debug',
        'debugger': 'on_unreachable',
        'ignore_errors': False,
    }

    # create sample task
    task = Task()
    task

# Generated at 2022-06-12 22:01:19.216359
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    jdata = """
    {
        "failed_when_result": false,
        "msg": "the output has been hidden due to the fact that 'no_log: true' was specified for this result",
        "changed": false,
        "invocation": {
            "module_name": "debug",
            "module_args": {
                "msg": "Hello, world!",
                "_ansible_verbose_always": true
            },
            "module_complex_args": {
                "msg": "Hello, world!",
                "_ansible_verbose_always": true
            }
        },
        "stdout": "Hello, world!",
        "stderr": "",
        "_ansible_verbose_always": true,
        "_ansible_no_log": true
    }
    """
    task = TaskResult

# Generated at 2022-06-12 22:01:31.389274
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    # Setup
    host = "host"
    task = "task"
    return_data = {'item': 'foo'}

    # Test
    result = TaskResult(host, task, return_data)

    # Assert
    assert result.is_skipped() == False

# Generated at 2022-06-12 22:01:42.180008
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    class FakeTask:
        def __init__(self, action, ignore_errors, debugger):
            self.action = action
            self.ignore_errors = ignore_errors
            self.debugger = debugger

    class FakeHost:
        def __init__(self, name):
            self.name = name

    result = {'failed': True}
    task_fields = {}
    for action in ('shell', 'command', 'win_shell', 'raw'):
        for ignore_errors in (False, True):
            for debugger in ('always', 'never', 'on_failed', 'on_skipped', 'on_unreachable'):
                for globally_enabled in (True, False):
                    task = FakeTask(action, ignore_errors, debugger)
                    host = FakeHost('host')

# Generated at 2022-06-12 22:01:50.654647
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    task_fields = dict()
    task_fields['debugger'] = 'never'
    task_fields['ignore_errors'] = False
    task = dict()
    host = dict()
    return_data = dict()
    return_data['failed'] = False
    return_data['changed'] = True
    test_case = TaskResult(host, task, return_data, task_fields)
    assert test_case.needs_debugger() == False
    task_fields['debugger'] = 'always'
    test_case = TaskResult(host, task, return_data, task_fields)
    assert test_case.needs_debugger() == True
    task_fields['debugger'] = 'on_failed'
    return_data['failed'] = True

# Generated at 2022-06-12 22:02:01.408225
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    host_name = 'localhost'
    task_name = 'dummy_task'
    task_args = {'msg': 'Dummy message'}
    task_action = 'debug'
    task_no_log = True
    task_ignore_errors = False
    task_debugger = 'on_failed'

    task_fields = {
        'name': task_name,
        'action': task_action,
        'no_log': task_no_log,
        'ignore_errors': task_ignore_errors,
        'debugger': task_debugger
    }


# Generated at 2022-06-12 22:02:13.314580
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    host = 'foo'
    result = dict(changed=False, failed=False)
    task = dict(name='The name of the task', ignore_errors=False, debugger=None)
    task_fields = dict(name='the name of the task_fields')

    task_result = TaskResult(host, task, result, task_fields)

    ret = task_result.needs_debugger()
    assert ret is False

    task = dict(name='The name of the task', ignore_errors=True, debugger='always')
    task_fields = dict(name='the name of the task_fields')
    task_result = TaskResult(host, task, result, task_fields)
    ret = task_result.needs_debugger()
    assert ret is True


# Generated at 2022-06-12 22:02:20.528842
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():

    task_fields = {'name': 'fake task to test TaskResult class',
                   'debugger': 'on_failed',
                   'ignore_errors': True}
    task = TaskResult(None, None, {}, task_fields)

    # test with result having failed_when_result
    result = {'failed': True,
              'failed_when_result': True,
              'results':[{'failed': True,
                          'failed_when_result': True,
                          'foo': 1},
                         {'failed': False,
                          'failed_when_result': False,
                          'bar': 2}]
    }
    result_obj = TaskResult(None, None, result, task_fields)
    assert result_obj.is_failed()

    # test with result having failed_when_result = False
    result

# Generated at 2022-06-12 22:02:29.424794
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    result = TaskResult(None, None, {
        'failed': True,
        'changed': True,
        'ansible_facts': {'test': 'true'},
        '_ansible_fact_cleaned': True,
        '_ansible_no_log': True,
        '_ansible_item_result': False,
    })

    result_clean = result.clean_copy()
    assert result_clean._result == {'censored': 'the output has been hidden due to the fact that '
                                                '\'no_log: true\' was specified for this result',
                                    'changed': True}



# Generated at 2022-06-12 22:02:40.651765
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    task_fields = dict(
        action='file',
        module_arguments='path=/path/to/file state=absent',
        name='file absent',
        ignore_errors=False,
        debugger='always'
    )
    task = dict(
        ignore_errors=False
    )
    host = dict(
        name='host1'
    )

    # Test when there is no failed key in results
    return_data = {'changed': True, 'invocation': {'module_args': 'path=/path/to/file state=absent'}}
    test = TaskResult(host, task, return_data, task_fields)
    assert not test.is_failed()

    # Test when there is a failed key set to True in results

# Generated at 2022-06-12 22:02:48.473615
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    import ansible
    import ansible.plugins.action
    import ansible.module_utils
    import ansible.plugins.loader
    import ansible.plugins.module_utils

    class FakeHost(object):
        pass

    class FakeTask(object):
        def get_name(self):
            return "fake_task_name"

    class FakeModule(object):
        pass

    class FakeTaskResult(object):
        def __init__(self, result):
            self.result = result

    class FakeActionBase(object):
        _config = dict()
        _task_vars = dict()

        def run(self, tmp=None, task_vars=None):
            return FakeTaskResult(result)


# Generated at 2022-06-12 22:02:56.680102
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    # TODO: this test should be moved to the testsuites once the new
    # testsuites are merged with devel.
    task = object()
    task_fields = dict()

    results = (
        (True, True),
        (True, False),
        (False, False),
        (False, True),
    )

    for (debugger_value, globally_enabled) in results:
        task_fields['debugger'] = debugger_value
        r = TaskResult('example', task, dict(), task_fields)
        assert r.needs_debugger(globally_enabled) == (globally_enabled or debugger_value)

# Generated at 2022-06-12 22:03:12.560106
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    # If you modify this unit test method then consider modifying
    # the method playbook.play_context.load_debugger_vars in
    # the same way.
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    play = Play()
    play.hosts = ['host1']
    play.tasks = []
    play_context = PlayContext(play=play)

    task = Task()
    task.action = 'debug'
    task.args = {'msg': 'msg'}

    task_result = TaskResult('host1', task, {'msg': 'msg'})
    task_result.needs_debugger(globally_enabled=True)

# Generated at 2022-06-12 22:03:20.115504
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():

    # Create an object of class TaskResult
    task_result = TaskResult(None, None, None)

    # CASE 1: if the value of _task_fields.get('debugger') == 'always'
    _task_fields = { 'name': 'test task', 'debugger': 'always' }
    task_result._task_fields = _task_fields
    assert task_result.needs_debugger() == True

    # CASE 2: if the value of _task_fields.get('debugger') == 'on_unreachable'
    task_result._result = { 'unreachable': True }
    _task_fields = { 'name': 'test task', 'debugger': 'on_unreachable' }
    task_result._task_fields = _task_fields
    assert task_result.needs_debugger() == True



# Generated at 2022-06-12 22:03:27.879673
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    test_cases = [
        ('always', True, True, True, True, True, True, True, True),
        ('never', False, False, False, False, False, False, False, False),
        ('on_failed', False, False, False, False, False, False, False, False),
        ('on_unreachable', False, False, False, False, False, False, False, False),
        ('on_skipped', False, False, False, False, False, False, False, False),
    ]

    # build test cases from combinations of (globally_enabled, task_result_is_failed, task_result_is_unreachable, task_result_is_skipped, task_field_ignore_errors, task_field_debugger)

    # first generate all combinations of (globally_enabled, task_result

# Generated at 2022-06-12 22:03:41.226653
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.vars.clean import module_response_deepcopy
    host_name = 'localhost'
    task = Task()
    task.action = 'setup'
    task.ignore_errors = False
    task.no_log = False
    task.deprecated = False
    task.debugger = None
    task_fields = {}

# Generated at 2022-06-12 22:03:48.937551
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    tqm = TaskQueueManager(
        inventory=InventoryManager(loader=DataLoader(), sources=C.DEFAULT_HOST_LIST),
        variable_manager=VariableManager())

    task1 = Task()
    task1.action = 'set_fact'

    taskresult = TaskResult(None, task1, None)
    taskresult.clean_copy()

# Generated at 2022-06-12 22:04:00.673135
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    test_data = []

    result1 = dict(failed=True)
    test_data.append((result1, True))
    result2 = dict(results=[dict(failed=True), dict(failed=True)])
    test_data.append((result2, True))
    result3 = dict(results=[dict(failed=True), dict(failed=False)])
    test_data.append((result3, True))
    result4 = dict(results=[dict(failed=False), dict(failed=True)])
    test_data.append((result4, True))
    result5 = dict(results=[dict(failed=False), dict(failed=False)])
    test_data.append((result5, False))
    result6 = dict(results=[dict(failed=False), result2])

# Generated at 2022-06-12 22:04:09.803935
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    from ansible.task import Task
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    h = Host(name="host")
    t = Task()
    t.name = "test"
    t.action = "shell"
    t.no_log = True
    data_loader = DataLoader()

    r = {"changed": False, "_ansible_ignore_errors": False, "item": "test", "failed": False, "changed_when": "changed", "rc": 0, "_ansible_no_log": False, "invocation": {"module_name": "shell", "module_args": "echo 'test'"}, "stdout": "test"}
    result = TaskResult(h, t, r)
    result_clean_copy = result.clean_copy()


# Generated at 2022-06-12 22:04:22.322603
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    class MockTask:
        pass

# Generated at 2022-06-12 22:04:31.499011
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import pytest