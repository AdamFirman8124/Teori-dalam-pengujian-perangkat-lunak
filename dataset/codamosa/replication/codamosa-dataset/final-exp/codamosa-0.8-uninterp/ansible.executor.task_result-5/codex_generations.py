

# Generated at 2022-06-12 21:54:47.309702
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task

    test_task_fields = {'name': 'test_name',
                        }
    test_task = Task()
    test_task._ds = test_task_fields

    test_return_data = {'failed': True, 'skipped': True, 'invocation': {'module_name': 'test_module_name'}, '_ansible_no_log': True}

    test_result = TaskResult('test_host', test_task, test_return_data)
    result = test_result.clean_copy()
    assert result._task._ds == test_task_fields
    assert result._result == {'censored': 'the output has been hidden due to the fact that \'no_log: true\' was specified for this result'}

# Generated at 2022-06-12 21:54:58.058616
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    task_result_class = TaskResult('host1',None, 'result')
    task_result_class._result = {"_ansible_item_label": "item1", "results": [{"_ansible_item_label": "item2"}]}
    task_result_class._result['results'][0]['invocation'] = {'module_name': 'test', 'module_args': "test arguments"}
    task_result_class._task_fields = {'name': 'test_task'}
    result = task_result_class.clean_copy()
    assert task_result_class._task_fields == result._task_fields
   # The result was transferred without changes.
    assert task_result_class._result == result._result
    # This is a list. It will be removed.
    assert 'results' not in result._result

# Generated at 2022-06-12 21:55:03.982879
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task

    # check that we're actually getting a TaskResult instance back
    assert isinstance(TaskResult(None, None, {}).clean_copy(), TaskResult)

    # check that the method works with empty results
    assert TaskResult(None, Task(), {}).clean_copy()._result == {}

    # check that the method works with a dict
    assert TaskResult(None, Task(), {'failed': False}).clean_copy()._result == {}

    # check that the method works with a list of dicts
    assert TaskResult(None, Task(), [{'failed': False}]).clean_copy()._result == {'results': [{}]}

# Generated at 2022-06-12 21:55:14.024655
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():

    # check if debugger is enabled by configuration
    task_vars = dict(
        ansible_debugger_enabled=True
    )

# Generated at 2022-06-12 21:55:22.542776
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    task_fields = dict()
    task_fields['name'] = 'test'
    from ansible.plugins.loader import action_loader
    task = action_loader.get('debug', class_only=True)()
    task.action = 'debug'
    return_data = dict()
    return_data['skipped'] = True
    return_data['results'] = list()
    return_data['results'].append(dict())
    return_data['results'].append(dict())
    return_data['results'][0]['skipped'] = True
    return_data['results'][1]['skipped'] = True
    host = dict()
    taskResult = TaskResult(host, task, return_data, task_fields)
    assert taskResult.is_skipped() == True

# Generated at 2022-06-12 21:55:33.792715
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():

    from ansible.playbook.task import Task

    task_fields={}
    task = Task.load(task_fields)
    task._role = None

    # test_on_failed: Task with debugger enabled should need debugger
    task_fields={'name':'task 1', 'debugger': 'on_failed'}
    task = Task.load(task_fields)
    task._role = None
    task_result = TaskResult(None, task, {'failed_when_result': False, 'failed': True})
    assert task_result.needs_debugger(False)

    # test_on_failed_not_failed: Task with debugger enabled and task failed should not need debugger
    task_fields={'name':'task 2', 'debugger': 'on_failed'}
    task = Task.load(task_fields)
    task

# Generated at 2022-06-12 21:55:42.560137
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    failed_result = {'msg': 'the message', 'failed': False, 'changed': True, 'invocation': {'module_args': {'test': 'test'}}, 'results': [{'item': 'test 1', 'failed': False, 'changed': True, 'invocation': {'module_args': {'test': 'test'}}}, {'item': 'test 2', 'failed': False, 'changed': True, 'invocation': {'module_args': {'test': 'test'}}}]}
    module_result = {'msg': 'the message', 'failed': False, 'changed': True, 'invocation': {'module_args': {'test': 'test'}}}
    t = TaskResult('', '', failed_result)
    assert not t.is_skipped()


# Generated at 2022-06-12 21:55:45.058724
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # implement this when you need to debug or test this function
    pass


# Generated at 2022-06-12 21:55:55.108243
# Unit test for method clean_copy of class TaskResult

# Generated at 2022-06-12 21:56:01.600167
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():

    # When is_failed return True
    task = {'failed': True}
    result = TaskResult(None, None, task)
    assert result.is_failed()

    # When is_failed return False
    task = {'failed': False}
    result = TaskResult(None, None, task)
    assert not result.is_failed()

    # When is_failed return True and there is no failed
    task = {'unreachable': True}
    result = TaskResult(None, None, task)
    assert result.is_failed()

    # When is_failed return False and there is no failed
    task = {'unreachable': False}
    result = TaskResult(None, None, task)
    assert not result.is_failed()

    # When is_failed return False and there is no failed, with subresult
   

# Generated at 2022-06-12 21:56:18.595113
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # create a TaskResult
    class FakeTask:
        def __init__(self):
            self.action = 'action'
            self.no_log = True
    class FakeHost:
        def __init__(self):
            self.name = 'hostname'
    return_data = {'censored': 'censored', 'failed': True, 'changed': True, 'invocation': {'module_args': 'module_args', 'module_name': 'module_name'}, '_ansible_no_log': True, 'foo': 'bar'}
    task = FakeTask()
    host = FakeHost()
    result = TaskResult(host, task, return_data)
    # clean the result
    result_copy = result.clean_copy()
    # check that output is as expected

# Generated at 2022-06-12 21:56:26.250038
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    host = '127.0.0.1'
    task = {
        'name': 'test',
        'action': 'test',
        'no_log': True,
    }
    return_data = {
        'cowsay': 'hello world',
        'failed': False,
        'changed': False,
        'invocation': 'foo',
        '_ansible_parsed': False,
        '_ansible_no_log': False,
        '_ansible_item_label': 'bar',
    }
    task_fields = {
        'name': 'test',
        'action': 'test',
        'no_log': True,
        'ignore_errors': True,
    }
    task_result = TaskResult(host, task, return_data, task_fields)
    assert task_

# Generated at 2022-06-12 21:56:30.168690
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    result = TaskResult(None, None, None)

    # If debugger is set to 'always', return True
    assert result.needs_debugger(True) == True

    # If debugger is set to 'never', return False
    assert result.needs_debugger(False) == False

# Generated at 2022-06-12 21:56:37.417070
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    print('Start testing TaskResult is_skipped')
   
    task = {
        'name': 'test'
    }
    host = 'localhost'
    # 1.1
    # Case that there is no result
    return_data = None 
    task_fields = None
    tr = TaskResult(host, task, return_data, task_fields)
    print('Case 1')
    if tr.is_changed() == False:
        print('Pass')
    else:
        print('Fail')
    
    print('Case 2')
    if tr.is_skipped() == False:
        print('Pass')
    else:
        print('Fail')
    
    print('Case 3')
    if tr.is_failed() == False:
        print('Pass')
    else:
        print('Fail')
    


# Generated at 2022-06-12 21:56:46.811793
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    def assert_result(expected_result, task_fields, result_keys):
        '''
        Assert that the result of TaskResult.needs_debugger is equal to expected_result, given the provided
        task_fields and the keys of the result.
        '''
        task = Mock()
        task.all_vars.side_effect = lambda: task_fields
        result = {k: None for k in result_keys}
        assert TaskResult(None, task, result).needs_debugger() == expected_result

    def assert_failed_unreachable(task_fields, result_keys):
        '''
        Assert that the result of TaskResult.needs_debugger is True, given the provided task_fields and
        the keys of the result.
        '''
        assert_result(True, task_fields, result_keys)

# Generated at 2022-06-12 21:56:56.761899
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    '''
    Test cases:
    1. Need debugger
        1.1 Force enable
        1.2 Failed
        1.3 Unreachable
        1.4 Skipped
        1.5 Failed on ignore-errors enabled
        1.6 Failed on ignore-errors disabled
    2. Not need debugger
        2.1 Disable globally
        2.2 Specific disable
        2.3 Success
    '''

    # Debugger configured as 'always' (case 1.1)
    task_fields = dict(debugger='always')
    task = object()
    obj = TaskResult("Hostname", task, dict())
    assert True == obj.needs_debugger(True)

    # Debugger enabled globally (case 1.2 - 1.5)
    obj = TaskResult("Hostname", task, dict(failed=True, unreachable=False))


# Generated at 2022-06-12 21:57:05.276426
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    # Test 1
    return_data = {
        'failed_when_result': True
    }
    host = None
    task = ''
    task_fields = None
    result = TaskResult(host, task, return_data, task_fields)
    assert result.is_failed()

    # Test 2
    return_data = {
        'failed_when_result': False
    }
    host = None
    task = ''
    task_fields = None
    result = TaskResult(host, task, return_data, task_fields)
    assert not result.is_failed()

    # Test 3
    return_data = {
        'results': [
            {
                'failed_when_result': True
            },
            {
                'failed_when_result': True
            }
        ]
    }
    host

# Generated at 2022-06-12 21:57:14.739305
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    host = '127.0.0.1'
    task = 'test_taskname'

# Generated at 2022-06-12 21:57:22.997873
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.role_include import RoleInclude

    # Create a RoleInclude to be used by a Block
    ri = RoleInclude()
    ri._role_name = 'role_name_1'

    # Create a Block to be used by a Task
    b = Block()
    b._role = ri

    # Create a Task to be used by TaskResult
    task = Task()
    task._role = b
    task._ds = {'ignore_errors': False, 'debugger': None}

    # Create a TaskResult
    tr = TaskResult('test_host', task, {'failed': False, 'skipped': False}, task._ds)

   

# Generated at 2022-06-12 21:57:34.124171
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    from ansible.playbook.task import Task

    # 1) Test failed task
    host = 'host'
    task_fields = {'name': 'task name'}
    task = Task()
    return_data = {'failed': True}
    task_result = TaskResult(host, task, return_data, task_fields)

    expected_result = {'failed': True}

    assert(task_result.clean_copy()._result == expected_result)

    # 2) Test skipped task
    return_data = {'skipped': True}
    task_result = TaskResult(host, task, return_data, task_fields)

    expected_result = {'skipped': True}

    assert(task_result.clean_copy()._result == expected_result)

    # 3) Test skipped task with loop results (item is

# Generated at 2022-06-12 21:57:54.186393
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    # 1) does not need debugger on successful task and when globally disabled
    global_disable_debugger = False
    task_fields = dict(debugger='on_failed', ignore_errors=False)
    result = dict(failed=False)
    t = TaskResult('host', 'task', result, task_fields)
    assert not t.needs_debugger(global_disable_debugger)

    # 2) globally enabled and ignore_errors wipes out task-specific debugger setting
    # and needs_debugger with ignore_errors on failed task returns False
    global_disable_debugger = False
    task_fields = dict(debugger='on_failed', ignore_errors=True)
    result = dict(failed=True)
    t = TaskResult('host', 'task', result, task_fields)

# Generated at 2022-06-12 21:58:01.624732
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude

    task = Task()
    block = Block()
    task_include = TaskInclude()

    class TestClass:
        @property
        def ignore_errors(self):
            return False

    obj = TestClass()

    result = TaskResult(obj, task, {}, {'debugger': 'always', 'ignore_errors': False})
   # When globally_enabled equals True
    assert result.needs_debugger(True) == True

    result = TaskResult(obj, task, {}, {'debugger': 'never', 'ignore_errors': False})
    # When globally_enabled equals True
    assert result.needs_debugger(True) == False

    # Case1:

# Generated at 2022-06-12 21:58:11.179395
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    # GIVEN
    host = None
    task = None
    return_data = {
        'failed': False,
        'failed_when_result': False,
        'results': [
            {'failed': False, 'failed_when_result': False}
        ]
    }
    task_fields = None

    # WHEN
    task_result = TaskResult(host, task, return_data, task_fields)

    # THEN
    assert task_result.is_failed() == False

    # GIVEN
    return_data = {'failed': False, 'failed_when_result': False,
                   'results': [{'failed': True, 'failed_when_result': False}]}

    # WHEN
    task_result = TaskResult(host, task, return_data, task_fields)

    # THEN

# Generated at 2022-06-12 21:58:17.212120
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    import unittest
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task

    class TestTaskResult(unittest.TestCase):
        def test_needs_debugger(self):
            task1 = Task()
            task1._role = Role()
            task1._role._role_path = 'fake_role_path'
            task1._role._role_name = 'fake_role_name'
            task1._task_include = TaskInclude()
            task1._task_include._parent_role = task1._role
            task1._role._task_include = task1._task_include
            task1._task_include._include_role = Include

# Generated at 2022-06-12 21:58:25.800402
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():

    # TaskResult instance
    task = {'action': 'setup',
            'module_name': 'setup'}

    task_fields = {'action': 'setup',
                   'module_name': 'setup'}

    return_data = {'ansible_facts':
                       {'ansible_kernel_version':
                            '3.10.0-229.el7.x86_64',
                        'ansible_processor_vcpus':
                            1,
                        'ansible_processor_cores':
                            1,
                        'ansible_architecture':
                            'x86_64'}}


# Generated at 2022-06-12 21:58:35.849492
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    """
    Method needs_debugger of class TaskResult returns True when
        - globally_enabled is True and task has failed and ignore_errors is False
        - globally_enabled is True and task is unreachable
        - task has debugger set to 'always'
        - task has debugger set to 'on_failed' and has failed and ignore_errors is False
        - task has debugger set to 'on_skipped' and is skipped
        - task has debugger set to 'on_unreachable' and is unreachable
    """


# Generated at 2022-06-12 21:58:44.194802
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    import ansible.playbook.task_include as task_include
    import ansible.playbook.task as task
    host = 'localhost'
    task_name = "Test task name"
    task_data = dict(name=task_name)
    task_ds = task.Task.load(task_data, task_include.TaskInclude._loader)
    task_result_data = dict(failed=False)
    task_result_data_failed = dict(failed=True)

    # check needs_debugger is set to True when failed is True and debugger is set to never
    task_fields = dict(debugger="never")
    task_result = TaskResult(host, task_ds, task_result_data_failed, task_fields=task_fields)

# Generated at 2022-06-12 21:58:55.260316
# Unit test for method clean_copy of class TaskResult

# Generated at 2022-06-12 21:59:00.460406
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():

    input = '{"results": [{"failed_when_result": false, "failed": false}, {"failed_when_result": true, "failed": false}, {"failed_when_result": false, "failed": true}]}'
    result = DataLoader().load(input)

    task = TaskResult('', None, result)
    assert task.is_failed()

    input = '{"results": [{"failed": false}, {"failed": false}]}'
    result = DataLoader().load(input)
    task = TaskResult('', None, result)
    assert not task.is_failed()

    input = '{"results": [], "failed": true}'
    result = DataLoader().load(input)
    task = TaskResult('', None, result)
    assert task.is_failed()


# Generated at 2022-06-12 21:59:11.684291
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    host = None
    task = None
    return_data = {}
    task_fields = {}

    # Test case 1.
    print("Test case 1. ")
    return_data = {"results": [{"item": "1", "skipped": True}, {"item": "2", "skipped": True}, {"item": "3", "skipped": True}]}
    taskresult = TaskResult(host, task, return_data, task_fields)
    assert taskresult.is_skipped()

    # Test case 2.
    print("Test case 2. ")
    return_data = {"results": [{"item": "1", "skipped": False}, {"item": "2", "skipped": True}, {"item": "3", "skipped": True}]}

# Generated at 2022-06-12 21:59:29.090891
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    host = None
    task = None

    assert TaskResult(host, task, {'results': [{'skipped': True}]}).is_skipped()
    assert TaskResult(host, task, {'results': [{'skipped': False}]}).is_skipped()
    assert not TaskResult(host, task, {'results': [{'skipped': False}, {'skipped': True}]}).is_skipped()
    assert TaskResult(host, task, {'results': [{'skipped': True}, {'skipped': True}]}).is_skipped()

    assert TaskResult(host, task, {'skipped': True}).is_skipped()
    assert not TaskResult(host, task, {'skipped': False}).is_skipped()

# Generated at 2022-06-12 21:59:41.084098
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    d = DataLoader()

# Generated at 2022-06-12 21:59:52.738813
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    task_fields = dict(name='debug_task', action='debug')
    task_fields_failed = dict(name='debug_task_failed', action='debug', debugger='on_failed')
    task_fields_unreachable = dict(name='debug_task_unreachable', action='debug', debugger='on_unreachable')
    task_fields_skipped = dict(name='debug_task_skipped', action='debug', debugger='on_skipped')
    task_fields_always = dict(name='debug_task_always', action='debug', debugger='always')

# Generated at 2022-06-12 22:00:02.537539
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    # pylint: disable=protected-access
    # pylint: disable=no-value-for-parameter

    from ansible.playbook.task import Task

    task_fields = {'name': 'test_task'}

    # setup a dummy result for the task
    result = {
        'changed': False,
        'rc': 0,
        'stderr': '',
        'stderr_lines': [],
        'stdout': '',
        'stdout_lines': [],
    }

    # validate that tasks are skipped properly
    result['skipped'] = True
    tr = TaskResult('dummy_host', Task(), result, task_fields)
    assert tr.is_skipped() is True
    assert tr.is_failed() is False

# Generated at 2022-06-12 22:00:14.142608
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # remove exceptions that are only used in the callback module
    task1_result = loader.load({'changed': True, 'invocation': {'module_args': {'a': 'b'}}, 'meta': {'vars':{'a': 'b'}}, 'ansible_facts': {'a': 'b'}})
    task2_result = loader.load({'changed': True, 'invocation': {'module_args': {'a': 'b'}}, 'meta': {'vars':{'a': 'b'}}, 'ansible_facts': {'a': 'b'}, '_ansible_no_log': True})

# Generated at 2022-06-12 22:00:22.534882
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    import sys
    import os
    if not os.path.exists("./test/units/module_utils"):
        os.makedirs("./test/units/module_utils")

    sys.path.insert(0, "./test/units/module_utils")

    import unittest

    class TestTaskResult(unittest.TestCase):

        def setUp(self):
            from ansible.module_utils import basic

# Generated at 2022-06-12 22:00:32.136923
# Unit test for method clean_copy of class TaskResult

# Generated at 2022-06-12 22:00:44.087229
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    '''test TaskResult.clean_copy'''

    # Test clean_copy on dict
    result = {'failed': False, 'changed': True, 'attempts': 1, 'retries': 0, '_ansible_no_log': False, 'invocation': {'module_name': 'c', 'module_args': ''}, '_ansible_item_result': True, '_ansible_diff': '', '_ansible_verbose_always': True}
    task_fields = {'name': 'a'}

    taskresult = TaskResult('127.0.0.1', 'b', result, task_fields)
    clean_result = taskresult.clean_copy()
    assert clean_result._result == {'changed': True, 'attempts': 1, 'retries': 0}

    # Test clean_copy

# Generated at 2022-06-12 22:00:51.837454
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext

    host = '127.0.0.1'
    task = Task()
    block = Block()
    play_context = PlayContext()
    return_data = {
        'failed': True,
        '_ansible_no_log': False,
        'invocation': {
            'module_args': {
                'name': 'foo',
                'state': 'bar'
            }
        }
    }

    task_fields = {
        'action': 'debug',
        'ignore_errors': False
    }

    task_result = TaskResult(host, task, return_data, task_fields)

    # case 1: globally_enabled = True, task

# Generated at 2022-06-12 22:01:03.224351
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    return_data = {
        "_ansible_version": {"full": "1.6.0", "major": 1, "minor": 6, "revision": 0, "string": "1.6.0"},
        "ahost": "127.0.0.1",
        "alive": True,
        "ansible_facts_changed": True,
        "ansible_facts": {
            "my_fact": "my_fact_value"
        },
        "ansible_version": {"full": "1.6.0", "major": 1, "minor": 6, "revision": 0, "string": "1.6.0"},
        "changed": True,
        "discovered_interpreter_python": "/usr/bin/python"
    }

    module_name = 'ping'

# Generated at 2022-06-12 22:01:50.399935
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import ansible.playbook.play  # cannot be imported directly, see #10648
    from ansible.executor.task_result import TaskResult
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar

    host = AnsibleUnsafeText('localhost')
    play = ansible.playbook.play.Play()
    variable_manager = VariableManager(loader=DataLoader())
    variable_manager.set_host_variable(host, HostVars(vars=dict(ansible_host=host, ansible_connection='local')))

# Generated at 2022-06-12 22:02:01.184671
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    host = 'h1'
    task = None
    return_data = '{"test": "1"}'
    task_fields = None
    tc = TaskResult(host, task, return_data, task_fields)
    assert tc.clean_copy()._result == {'test': '1'}

    return_data = '{"test": "1", "_ansible_ignore_errors": true}'
    tc = TaskResult(host, task, return_data, task_fields)
    assert tc.clean_copy()._result == {'test': '1', '_ansible_ignore_errors': True}

    return_data = '{"test": "1", "_ansible_verbose_override": true}'
    tc = TaskResult(host, task, return_data, task_fields)

# Generated at 2022-06-12 22:02:13.046007
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import ansible.playbook.task_include as task_include
    from ansible.playbook.task import Task
    from ansible.vars.hostvars import HostVars

    # Test single-task results
    task = Task.load(dict(action=dict(module='test', args=dict(test='test'))))
    result = TaskResult('localhost', task, {'skipped': True})
    assert result.clean_copy()._result == {}

    task = Task.load(dict(action=dict(module='test')))
    result = TaskResult('localhost', task, {'skipped': True})
    assert result.clean_copy()._result == {}

    task = Task.load(dict(action=dict(module='test')))

# Generated at 2022-06-12 22:02:20.406247
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)
    variable_manager.set_inventory(loader.load_inventory('localhost,'))

    # task 1
    variable_manager.extra_vars = dict()
    variable_manager.extra_vars['debugger_enabled'] = True
    variable_manager.extra_vars['debugger_ignore_errors'] = False
    t = Task()

# Generated at 2022-06-12 22:02:30.958644
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task

    class HostMock:
        def __init__(self):
            self.no_log = False
            self.no_log_passwords = False
            self.name = 'test_host'

    class TaskMock(Task):
        def __init__(self):
            self.name = 'test_task'
            self.action = 'test_action'
            self.args = {'test': 'test'}
            self.module_vars = {'test': 'test'}
            self.tags = []
            self.when = None
            self.register = None
            self.ignore_errors = False
            self.no_log = False

    class Result:
        def __init__(self, stdout_lines, stderr_lines, rc):
            self

# Generated at 2022-06-12 22:02:41.106425
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    task_fields = dict(
        no_log=False
        )

    returned_data = dict(
        failed=False,
        msg="OK",
        _ansible_no_log=False,
        _ansible_verbose_always=True,
        _ansible_item_label='localhost',
        _ansible_no_log=False,
        _ansible_verbose_override=True,
        _ansible_delegated_vars={'ansible_host': 'localhost', 'ansible_port': 22, 'ansible_user': 'root', 'ansible_connection': 'ssh'},
        )

    task_result = TaskResult(None, None, returned_data, task_fields)
    clean_result = task_result.clean_copy()

    assert not clean_result._result.has_

# Generated at 2022-06-12 22:02:47.089672
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.vars.hostvars import HostVars
    task = Task()
    host = HostVars()
    task_result = TaskResult(host, task, dict(foo="bar"))
    assert task_result.clean_copy()._result.get("foo") == "bar"
    # assert task_result.clean_copy()._result.get("invocation") is None


if __name__ == "__main__":
    import pytest
    pytest.main(args=['test_result.py'])

# Generated at 2022-06-12 22:02:57.263911
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task

    # Test default behavior (global debugger enabled)
    # no debugger field should be ignored
    task_fields = {}
    task = Task()
    result = TaskResult(None, task, {}, task_fields)
    result._result['changed'] = False
    result._result['failed'] = False
    result._result['skipped'] = False
    result._result['unreachable'] = False
    result._result['failed_when_result'] = False

    assert not result.needs_debugger(globally_enabled=True)
    result._result['unreachable'] = True
    assert result.needs_debugger(globally_enabled=True)
    result._result['failed'] = True
    assert result.needs_debugger(globally_enabled=True)
    result._

# Generated at 2022-06-12 22:03:07.634304
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    '''
    Test TaskResult.clean_copy() by mocking the inner
    variable (_result) with a list of different types
    of messages and then checking every item of the
    returned dictionary.
    '''
    class Host:
        pass

    class Task:
        pass

    host = Host()
    task = Task()
    result = TaskResult(host, task, "")

    # _result = []
    result._result = []
    assert result.clean_copy()._result == []

    # _result = [] of dict
    result._result = [{'msg': 'message1'}, {'msg': 'message2'}]
    assert result.clean_copy()._result == [{'msg': 'message1'}, {'msg': 'message2'}]

    # _result = dict

# Generated at 2022-06-12 22:03:13.023140
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    # TODO add zsh completion to this
    task_fields = {
        'debugger': None,
        'ignore_errors': False,
    }

    # a very simple task that 'fails' if the unreachable bit is true
    failing_task = {'unreachable': True}
    failing_result = TaskResult(None, None, failing_task, task_fields)
    assert failing_result.needs_debugger(False) == False
    assert failing_result.needs_debugger(True) == True

    # a very simple task that 'fails' if the failed bit is true
    failing_task = {'failed': True}
    failing_result = TaskResult(None, None, failing_task, task_fields)
    assert failing_result.needs_debugger(False) == False
    assert failing_result.needs_

# Generated at 2022-06-12 22:03:40.054045
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import mock
    import sys
    if sys.version_info >= (3, 0):
        import builtins
    else:
        import __builtin__ as builtins
    class MockTaskResult:
        def __init__(self, result):
            self.result = result
    import ansible.plugins.loader as plugin_loader
    plugin_loader.add_directory('./')

# Generated at 2022-06-12 22:03:50.320235
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task

    task_fields = {
            "debugger": "on_failed",
            "ignore_errors": True,
            "no_log": True,
        }


# Generated at 2022-06-12 22:04:01.890006
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.utils import module_docs
    from ansible.modules.command import ActionModule as command_module
    return_data = {
        "stdout": "",
        "stderr": "sudo: a password is required\r\nsudo: a password is required",
        "rc": 1,
        "start": "2018-10-12 21:31:28.299828",
        "end": "2018-10-12 21:31:29.048302",
        "delta": "0:00:00.748474",
        "changed": False,
        "cmd": "ls -l /usr/local/bin",
        "invocation": {
            "module_name": "command",
        }
    }

    task = Task()
    task.action

# Generated at 2022-06-12 22:04:10.871005
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play

    # Need to construct these for TaskResult constructor
    # It is not a problem to pass fake values
    host = 'test_host'
    task = Task()

    # Create a Play
    global_vars = {'ansible_debug': True}
    play = Play().load({
        'hosts': 'all', 'tasks': [{'debug': {'msg': 'debug me'}}],
        'vars': global_vars
        }, variable_manager=None, loader=None)

# Generated at 2022-06-12 22:04:23.036989
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from copy import deepcopy
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader

    task = Task()
    task.action = 'set_fact'
    task.no_log = True

    task_fields = {}
    task_fields['name'] = "test_name"

    host = "127.0.0.1"
    return_data = DataLoader().load("{ \"changed\" : true, \"msg\" : \"All items completed\" }")
    task_result = TaskResult(host, task, return_data, task_fields)

    result = deepcopy(task_result.clean_copy())
    assert result._task_fields['name'] == "test_name"

# Generated at 2022-06-12 22:04:31.130299
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    '''
    Test if the method clean_copy of class TaskResult returns a dictionary
    with all elements of the parameter self._result, but with the keys
    failed, skipped and all the keys starting with ansible_ (except the
    key ansible_version) removed.
    '''
    r = TaskResult('', '', {'hello': 1, 'world': 2, 'ansible_version': 3, 'ansible_foo': 4, 'failed': 5, 'skipped': 6})
    result_copy = r.clean_copy()
    expected_result_copy = {'hello': 1, 'world': 2, 'ansible_version': 3}
    assert result_copy._result == expected_result_copy