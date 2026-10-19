

# Generated at 2022-06-12 21:55:00.430724
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    host = None
    task = None
    return_data = {'skipped': True}
    task_result = TaskResult(host, task, return_data)
    assert task_result.is_skipped()
    return_data = {'skipped': False}
    task_result = TaskResult(host, task, return_data)
    assert not task_result.is_skipped()
    return_data = {'results': [{'skipped': True}, {'skipped': True}]}
    task_result = TaskResult(host, task, return_data)
    assert task_result.is_skipped()
    return_data = {'results': [{'skipped': False}, {'skipped': True}]}
    task_result = TaskResult(host, task, return_data)
    assert not task_result

# Generated at 2022-06-12 21:55:11.009444
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    # test needs_debugger for both action and task keyword
    # for each combination of task_debugger and ignore_errors config
    # for each combination of task result and globally_enabled
    orig_debugger_settings = (C.TASK_DEBUGGER_ENABLED, C.TASK_DEBUGGER_IGNORE_ERRORS)
    for task_debugger_setting in (True, False):
        for ignore_errors_setting in (True, False):
            for task_result in (True, False):
                for globally_enabled in (True, False):
                    C.TASK_DEBUGGER_ENABLED = task_debugger_setting
                    C.TASK_DEBUGGER_IGNORE_ERRORS = ignore_errors_setting


# Generated at 2022-06-12 21:55:20.290264
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():

    def assert_is_skipped(item, result_dict, ret):
        task = type('Task', (object,), {'no_log': False})
        task_result = TaskResult(result_dict.get('host'), task, result_dict)
        assert isinstance(task_result.is_skipped(), bool)
        assert task_result.is_skipped() == ret, str(item) + ": " + str(result_dict)


# Generated at 2022-06-12 21:55:30.973865
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    results = []
    results.append({'foo': 'bar', '_ansible_verbose_always': True, '_ansible_no_log': False})
    results.append({'foo': 'bar', '_ansible_verbose_always': True, '_ansible_no_log': True})
    results.append({'foo': 'bar', '_ansible_verbose_always': False, '_ansible_no_log': False})
    results.append({'_ansible_verbose_always': False, '_ansible_no_log': True})
    results.append({'_ansible_verbose_always': True, '_ansible_no_log': False})
    results.append({'_ansible_verbose_always': True, '_ansible_no_log': True})
    results

# Generated at 2022-06-12 21:55:40.771077
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    task_fields = {}
    task_fields['debugger'] = 'on_failed'
    task_fields['ignore_errors'] = True
    task = MockTask('test_task_name')
    host = MockHost('test_hostname')
    ret = TaskResult(host, task, {'failed' : True}, task_fields=task_fields)
    assert ret.needs_debugger() == False

    ret = TaskResult(host, task, {'failed' : True}, task_fields=task_fields)
    assert ret.needs_debugger(globally_enabled=True) == True

    task_fields['debugger'] = 'on_failed'
    task_fields['ignore_errors'] = False
    ret = TaskResult(host, task, {'failed' : True}, task_fields=task_fields)
    assert ret

# Generated at 2022-06-12 21:55:46.534324
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # load the test data, which has been written to a file with no_log=True set
    from ansible.parsing.dataloader import DataLoader
    results = DataLoader().load(filename='test/units/callback_plugins/results/clean_copy.json')

    task = DummyTask()
    host = DummyHost()

    # create TaskResult object from the results
    taskresult = TaskResult(host, task, results)

    # call TaskResult's clean_copy method to generate the "clean" results
    clean_results = taskresult.clean_copy()

    assert clean_results._result['verbose_override'] == "true"
    assert clean_results._result['censored'] == "the output has been hidden due to the fact that 'no_log: true' was specified for this result"
    assert clean_results._

# Generated at 2022-06-12 21:55:53.211407
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    class FakeTask:

        def __init__(self, name, action, no_log=False):
            self.name = name
            self.action = action
            self.no_log = no_log

        def get_name(self):
            return self.name

    class FakeHost:
        pass

    # Test without no_log set
    # Test without any internal key present
    task = FakeTask(
        name='test_task',
        action='setup'
    )
    host = FakeHost()
    internal_data = {
        'changed': False,
        'failed': True,
        'test_key': 'test_val'
    }
    task_fields = {
        'debugger': 'on_failed'
    }

# Generated at 2022-06-12 21:56:01.789468
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    yaml_data = """
- name: task_result
  block:
  - debug:
      msg: '{{var}}'
      verbosity: 4
    when: not var
    loop: [ 1, 2, 3 ]
    loop_control:
      loop_var: var
      index_var: idx
      label: '{{idx}} {{var}}'
    failed_when: False
    changed_when: False
    register: task_result
"""
    loader = AnsibleLoader(yaml_data, '<string>')
    block = next(loader.get_single_data())
    assert isinstance(block, Block)

    tasks

# Generated at 2022-06-12 21:56:09.219911
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    # Set up environment
    task_fields = dict(
        name='name',
    )
    return_data = dict(
        results=list(),
        failed_when_result=False,
        failed=False,
        unreachable=False
    )
    task_result = TaskResult(host='host', task='task', return_data=return_data, task_fields=task_fields)

    # Unit test
    assert not task_result.is_failed()

    # Tear down environment

# Generated at 2022-06-12 21:56:19.637701
# Unit test for method is_failed of class TaskResult

# Generated at 2022-06-12 21:56:39.586663
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult

    task = Task()
    task.action = 'mymodule'
    task_fields = dict()
    return_data = dict(invocation=dict(module_args="a"))
    host = "localhost"
    task_result = TaskResult(host, task, return_data, task_fields)
    clean_task_result = task_result.clean_copy()
    assert len(clean_task_result._result) == 0

# Generated at 2022-06-12 21:56:50.089153
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    # No failed_when_result
    host = None
    task = None
    return_data = {'failed': True, 'failed_when_result': False}
    task_fields = None
    tr = TaskResult(host, task, return_data, task_fields)
    assert(tr.is_failed() == True)

    # Failed_when_result is False
    host = None
    task = None
    return_data = {'failed': False, 'failed_when_result': False}
    task_fields = None
    tr = TaskResult(host, task, return_data, task_fields)
    assert(tr.is_failed() == False)

    # Failed_when_result is True
    host = None
    task = None
    return_data = {'failed': True, 'failed_when_result': True}

# Generated at 2022-06-12 21:56:58.941733
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    # Test for debugger on task with failed_when and not ignore_errors (needs_debugger should be True)
    task_fields_failed_when = {'failed_when': '{{ true }}', 'debugger': 'on_failed', 'ignore_errors': False}
    result_failed_when = {'failed': True, 'failed_when_result': True}
    task_failed_when = TaskResult(None, None, result_failed_when, task_fields_failed_when)
    assert task_failed_when.needs_debugger(globally_enabled=True)

    # Test for debugger on task with failed_when and ignore_errors (needs_debugger should be False)

# Generated at 2022-06-12 21:57:08.023737
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    # Setup
    import os
    import tempfile
    import shutil
    import json
    import jinja2
    host = '127.0.0.1'
    task_fields = {}
    task = MockTask(task_fields)
    mock_result = {'failed': False, 'failed_when_result': False, 'unreachable': False}

    expected_result = {'task_name': host, 'task_path': 'tasks/mock.yml', 'host': host, 'task': task_fields, 'result': mock_result} # Expected task result.

    # Execute test
    task_result = TaskResult(host, task, mock_result, task_fields)
    # Test the value returned for a debugger which isn't present in the playbook

# Generated at 2022-06-12 21:57:16.861020
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    # GIVEN
    task_vars = dict(no_log=False)
    task = AnsibleTask(action='include_role')
    result = TaskResult(host='localhost', task=task, return_data={})
    result._task_fields = task_vars
    # WHEN
    ret = result.needs_debugger()
    # THEN
    assert not ret, 'Default value should be False'


# Generated at 2022-06-12 21:57:23.093703
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host


# Generated at 2022-06-12 21:57:25.894046
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    assert False, "No tests for this module"

# Generated at 2022-06-12 21:57:31.401383
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    import json
    import pickle

    DataLoader_dump = DataLoader().dump
    module_response_deepcopy_org = module_response_deepcopy
    module_response_deepcopy_mock = lambda x: {'_ansible_no_log': True}

    try:
        import _frozen_importlib
    except ImportError:
        # Python >= 3.4
        from unittest import mock
        import sys

        @mock.patch.object(sys, 'modules')
        def test_TaskResult_clean_copy_inner(modules):
            import ansible.playbook.task_include
            from ansible.utils.vars import combine_vars

            DataLoader.dump = lambda self, data: json.dumps(data)

            modules['ansible.vars.clean'] = mock.Mock()
           

# Generated at 2022-06-12 21:57:42.586034
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    class DummyTask(object):
        pass

    dummy_task = DummyTask()
    dummy_task.action = 'test_test'

    task_fields = dict()
    task_fields.update(debugger='never')
    task_result = TaskResult(None, dummy_task, {}, task_fields)
    assert not task_result.needs_debugger()

    task_fields = dict()
    task_fields.update(ignore_errors=True)
    task_result = TaskResult(None, dummy_task, {}, task_fields)
    assert not task_result.needs_debugger()

    task_fields = dict()
    task_fields.update(ignore_errors=True, debugger='on_failed')
    task_result = TaskResult(None, dummy_task, {}, task_fields)
    assert not task

# Generated at 2022-06-12 21:57:54.318452
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    from ansible.playbook.task import Task as T
    from ansible.playbook.play_context import PlayContext
    import ansible.playbook.role
    from ansible.plugins.loader import action_loader

    # TODO: replace with mock-objects
    t = T()
    t._role = None
    t._play_context = PlayContext()

    t.action = 'shell'
    t.args = {'chdir': None, 'creates': None, 'executable': None, '_raw_params': 'echo 1', 'removes': None, 'warn': True}
    t._role = ansible.playbook.role.Role()
    t._role._role_name = "test_result"
    t._role._role_path = "/tmp/test_result"


# Generated at 2022-06-12 21:58:04.678068
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    def check(return_data, expected):
        task = FakeTask()
        result = TaskResult(FakeHost('example.com'), task, return_data)
        assert result.is_failed() == expected


# Generated at 2022-06-12 21:58:13.040287
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():

    class FakeTask:
        def get_name(self):
            return 'foo'

    def check_result(result, expected):
        task_result = TaskResult('localhost', FakeTask(), result)
        assert task_result.is_failed() == expected

    check_result({'unreachable': True}, True)
    check_result({'unreachable': False}, False)

    check_result({'failed': True}, True)
    check_result({'failed': False}, False)

    check_result({'failed': False, 'results': [{'failed': False}, {'failed': False}]}, False)
    check_result({'failed': False, 'results': [{'failed': False}, {'failed': True}]}, True)


# Generated at 2022-06-12 21:58:23.224939
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task

    host_name = 'test_host'
    task_name = 'test_task'
    loader = DataLoader()
    variable_manager = None
    loader.set_basedir('.')
    task_data = dict(action=dict(module='ping', args=dict()))
    task = Task.load(task_data, variable_manager=variable_manager, loader=loader)
    task.set_loader(loader)
    task.name = task_name
    return_data = dict(changed=True, _ansible_parsed=True,
                       invocation=dict(module_args='',))

    task_result = TaskResult(host_name, task, return_data)
    task_result._task

# Generated at 2022-06-12 21:58:33.633306
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task_include import TaskInclude

    host = 'test_host'
    task1 = TaskInclude('test_task')
    task2 = TaskInclude('test_task2')
    task1_fields = {'name': 'test_task'}
    task2_fields = {'name': 'test_task2'}

# Generated at 2022-06-12 21:58:41.021923
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    class MockTask:
        def __init__(self):
            self.action = 'test'
            self.no_log = False
            self.ignore_errors = False
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    inv = InventoryManager(loader=None, sources=None)
    inventory = inv.get_inventory()
    host = inventory.get_host("localhost")
    variable_manager = VariableManager(loader=None, inventory=inventory)
    task = MockTask()
    task_fields = {}
    # Check is_failed for item when 'failed' is True
    task_result = TaskResult(host, task, {"failed": True}, task_fields)
    result = task_result.is_failed()
    assert result

    # Check is_failed for item when 'failed

# Generated at 2022-06-12 21:58:52.717654
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import json
    import ansible.playbook


# Generated at 2022-06-12 21:59:01.542847
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task

    # Prepare data for TaskResult __init__
    host = 'localhost'
    task = Task()
    return_data = {}

    # Prepare data for TaskResult.clean_copy
    return_data['failed'] = False
    return_data['changed'] = False
    return_data['skipped'] = False
    return_data['retries'] = 3
    return_data['attempts'] = 5
    return_data['invocation'] = {}
    return_data['invocation']['module_name'] = 'shell'
    return_data['invocation']['module_args'] = 'echo 1'
    return_data['invocation']['module_complex_args'] = {}
    return_data['stdout'] = 'data'

# Generated at 2022-06-12 21:59:12.181393
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    from ansible.playbook.task import Task

    class MyHost:
        pass

    host = MyHost()
    task = Task()

    # no failed key
    return_data = dict()
    result = TaskResult(host, task, return_data)
    assert result.is_failed() == False

    # failed set to False
    return_data = dict(failed=False)
    result = TaskResult(host, task, return_data)
    assert result.is_failed() == False

    # failed set to True
    return_data = dict(failed=True)
    result = TaskResult(host, task, return_data)
    assert result.is_failed() == True

    # results with failed_when_result set to False
    return_data = dict(results=[dict(failed_when_result=False)])
   

# Generated at 2022-06-12 21:59:23.205666
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    # Testing TaskResult.is_skipped with a loop result
    task = {}
    task_fields = {}
    return_data = {
        "results": [
            {
                "item": 1,
                "skipped": True
            },
            {
                "item": 2,
                "skipped": True
            }
        ]
    }
    task_result = TaskResult(None, task, return_data, task_fields)
    assert task_result.is_skipped()

    # Testing TaskResult.is_skipped with a non-loop result
    task = {}
    task_fields = {}
    return_data = {
        "skipped": True
    }
    task_result = TaskResult(None, task, return_data, task_fields)
    assert task_result.is_skipped()



# Generated at 2022-06-12 21:59:29.627253
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    return_data = dict(changed=False, failed=False, results=None, skipped=False, unreachable=False)
    task = MockTask()
    task_fields = dict()
    host = MockHost()

    task_result = TaskResult(host, task, return_data, task_fields)
    assert task_result.is_failed() is False

    return_data = dict(changed=False, failed=False, results=None, skipped=False, unreachable=False)
    task = MockTask(action='shell')
    task_fields = dict()
    host = MockHost()

    task_result = TaskResult(host, task, return_data, task_fields)
    assert task_result.is_failed() is False


# Generated at 2022-06-12 21:59:49.704825
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    host = Host(name="localhost")
    task1 = Task()
    task1._role_name = "test.role"
    task2 = Task()
    task2._role_name = "test.role"
    task3 = Task()
    task3._role_name = "test.role"
    task4 = Task()
    task4._role_name = "test.role"
    task5 = Task()
    task5._role_name = "test.role"
    task6 = Task()
    task6._role_name = "test.role"

    task1._task_fields = {'debugger': 'always'}
    task2._task_fields = {'debugger': 'never'}
    task3._

# Generated at 2022-06-12 21:59:56.935408
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    host = "localhost"
    task = "task"
    return_data = {'msg': 'some data', 'failed': True, 'failed_when_result': True, 'invocation': True, '_ansible_no_log': True}
    task_fields = {'name': 'task name'}
    result = TaskResult(host, task, return_data, task_fields)
    clean_data = result.clean_copy()
    assert clean_data is not None

# Generated at 2022-06-12 22:00:08.150111
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.plugins.test.test_module import TestModule
    import json


# Generated at 2022-06-12 22:00:18.691166
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    _host = 'temp_host'
    _task = None
    _task_fields = None
    _return_data_1 = {'unreachable': False, 'failed': True}
    _return_data_2 = {'unreachable': False, 'failed': False}
    _return_data_3 = {'unreachable': True, 'failed': False}
    _return_data_4 = {'results': [{'unreachable': False, 'failed': False}], 'failed_when_result': False}
    _return_data_5 = {'results': [{'unreachable': False, 'failed': False}], 'failed_when_result': True}

# Generated at 2022-06-12 22:00:24.443316
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    import copy
    import ansible.parsing.dataloader
    import ansible.vars.manager
    import ansible.inventory.manager
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.executor.task_result
    import ansible.executor.task_include
    import ansible.executor.action_write_locks

    # Build a task from playbook
    variable_manager = ansible.vars.manager.VariableManager()
    loader = ansible.parsing.dataloader.DataLoader()
    inventory = ansible.inventory.manager.InventoryManager(loader=loader, sources=C.DEFAULT_HOST_LIST)

# Generated at 2022-06-12 22:00:32.950927
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    foo = TaskResult(None, None, None)
    assert foo.needs_debugger() == False

    bar = TaskResult(None, None, None, {"debugger": "on_failed"})
    assert bar.needs_debugger() == False
    assert bar.needs_debugger(True) == True

    baz = TaskResult(None, None, None, {"debugger": "on_failed", "ignore_errors": True})
    assert baz.needs_debugger() == False
    assert baz.needs_debugger(True) == False

    qux = TaskResult(None, None, None, {"debugger": "on_unreachable"})
    assert qux.needs_debugger() == False
    assert qux.needs_debugger(True) == False


# Generated at 2022-06-12 22:00:45.000609
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    result = TaskResult('hostname', 'task', {'changed': 'changed', 'failed': 'failed', '_ansible_verbose_always': '_ansible_verbose_always', 'results': [{'failed': 'failed_item'}, {'failed': 'failed_item_2'}]})
    newresult = result.clean_copy()
    assert newresult._result.get('changed') == 'changed'
    assert newresult._result.get('_ansible_verbose_always') == '_ansible_verbose_always'
    assert newresult._result.get('results')[0].get('failed') == 'failed_item'
    assert newresult._result.get('results')[1].get('failed') == 'failed_item_2'
    assert not newresult._result.get('failed')

# Generated at 2022-06-12 22:00:45.552677
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    pass

# Generated at 2022-06-12 22:00:52.694982
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():

    class Task:

        def __init__(self, action, debugger, ignore_errors):
            self.action = action
            self.debugger = debugger
            self.ignore_errors = ignore_errors

    class TaskResult_test(TaskResult):

        def __init__(self, _host, _task, return_data, task_fields=None):
            if task_fields is None:
                task_fields = dict()
            TaskResult.__init__(self, _host, _task, return_data, task_fields)

        def _check_key(self, key):
            if key in self._result:
                return True
            else:
                return False

    task_fields = {'debugger': 'on_failed', 'ignore_errors': True}
    task = Task('setup', 'on_failed', True)
    return

# Generated at 2022-06-12 22:01:03.827020
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.vars.hostvars import HostVars
    from ansible.utils.vars import combine_vars

    t = Task()
    t.action = 'setup'
    t.name = 'setup'
    t.no_log = True

    h = HostVars(name='localhost', taskvars=dict())


# Generated at 2022-06-12 22:01:21.235468
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    from ansible.task import Task
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    test_task = Playbook()
    test_task.inventory = InventoryManager(loader=DataLoader())

# Generated at 2022-06-12 22:01:28.215422
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # Test that it might works with the unix 'test' module
    module_name = "test"
    task = mock_Task(module_name)
    task_result = mock_task_result(task)
    results = task_result.clean_copy()

    # Test that clean_copy method returns a TaskResult object
    assert isinstance(results, TaskResult)

    # Test that clean_copy method returns a TaskResult object with a dictionary
    # in its _result attribute
    assert isinstance(results._result, dict)

    # Test that module_name is in _result attribute
    assert module_name in results._result

    # Test that all methods of TaskResult class are in the TaskResult object
    for method in TaskResult.__dict__:
        if not "__" in method:
            assert method in results.__dict__

    #

# Generated at 2022-06-12 22:01:39.240497
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

    task = Task()
    task._role = None
    task._block = Block()
    task.action = 'shell'
    task.args = dict(free_form='/bin/false')
    task.set_loader(DataLoader())
    task.vars = {}
    task._parent = Play()
    task._role = None
    task._role_name = None

    task.no_log = True


# Generated at 2022-06-12 22:01:49.013950
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # completely empty result
    result = {'results': []}
    task_result = TaskResult(None, None, result)
    result = task_result.clean_copy()._result
    assert 'results' in result and len(result['results']) == 0
    assert 'failed' not in result and 'changed' not in result and 'retries' not in result
    assert 'skipped' not in result and '_ansible_no_log' not in result and 'invocation' not in result

    # failed
    result = {'failed': True, 'failed_when_result': True}
    task_result = TaskResult(None, None, result)
    result = task_result.clean_copy()._result
    assert result == {'failed_when_result': True}

    # not failed

# Generated at 2022-06-12 22:01:55.339534
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    host = '10.0.0.1'
    task = TaskResult(host, task, return_data, task_fields)
    tc = task.clean_copy()
    assert len(tc._result.keys()) == 3
    assert 'censored' in tc._result.keys()
    assert 'changed' in tc._result.keys()
    assert 'retries' in tc._result.keys()

# Generated at 2022-06-12 22:02:03.663509
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host

# Generated at 2022-06-12 22:02:15.583995
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.callback import CallbackBase
    from ansible.utils.color import ANSIBLE_COLOR, stringc
   

# Generated at 2022-06-12 22:02:16.591111
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    if is_failed() is False:
        return 1
    else:
        return 0

# Generated at 2022-06-12 22:02:27.930942
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    class DummyTask(object):
        def __init__(self, action, debugger, ignore_errors):
            self.action = action
            self.ignore_errors = ignore_errors
            self._debugger = debugger

    def assert_needs_debugger(action, debugger, ignore_errors, globally_enabled, expected):
        dummy_task = DummyTask(action, debugger, ignore_errors)
        task_fields = {
            'debugger': debugger,
            'ignore_errors': ignore_errors,
            'name': 'and his name is'
        }
        task_result = TaskResult(None, dummy_task, {'failed': True}, task_fields)
        result = task_result.needs_debugger(globally_enabled)

# Generated at 2022-06-12 22:02:34.760750
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import unittest
    import json

    class TestTaskResult(unittest.TestCase):
        # Method to set up a test case
        # There is no setUp() method for this class
        # which means that each of the test_ methods listed after
        # begin with a clean slate.
        def init_test(self, description, input_data, expected_data):
            task_fields = {'name': 'testTask', 'ignore_errors': True,
                           'debugger': 'on_failed', 'no_log': True}
            self.task = TaskResult(host=None, task=None, return_data=input_data, task_fields=task_fields)
            self.output = json.dumps(self.task.clean_copy()._result)
            self.expected = json.dumps(expected_data)


# Generated at 2022-06-12 22:03:01.139913
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    class Task:
        def __init__(self):
            self.action = ''
            self.no_log = False
            self.debugger = ''
            self.ignore_errors = False

    class Host:
        def __init__(self):
            self.name = ''

    host = Host()
    failedTask = Task()
    failedTask.action = 'failed_action'
    failedTask.no_log = True

    def _check_result(task, debugger, ansible_debugger, ansible_ignore_errors, ansible_failed, ansible_unreachable, ansible_skipped):
        task.debugger = debugger
        task.ignore_errors = ansible_ignore_errors

        # Initialize result

# Generated at 2022-06-12 22:03:10.779753
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    class FakeTask:
        def __init__(self):
            self.action = 'setup'
            self.tags = []
            self.ignore_errors = False
            self.no_log = False
    fail_dict = {'msg': 'fixture failed', 'failed': True}
    fail_list = [{'item': 1, 'msg': 'fixture failed', 'failed': True}, {'item': 2, 'msg': 'fixture failed', 'failed': True}]
    success_dict = {'msg': 'fixture success', 'failed': False}
    success_list = [{'item': 1, 'msg': 'fixture success', 'failed': False}, {'item': 2, 'msg': 'fixture success', 'failed': False}]
    # Test a failed task
    fake_task = FakeTask()
    fake

# Generated at 2022-06-12 22:03:16.344525
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import json
    import os
    host_dict = {
        "all": {
            "hosts": {
                "somehost": {
                    "ansible_host": "127.0.0.1"
                }
            }
        }
    }
    inventory = DataLoader().load(host_dict)
    host = inventory.get_host('somehost')
    task_fields = {
        'no_log': False,
        'ignore_errors': False,
        'debugger': 'on_failed'
    }
    task = DataLoader().load(task_fields)

    data = json.load(open(os.path.join(os.path.dirname(__file__), 'task-result.json')))
    result = TaskResult(host, task, data, task_fields)

# Generated at 2022-06-12 22:03:25.563063
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader, variable_manager, 'localhost')
    variable_manager.set_inventory(inventory)

    task = Task()
    task.action = 'debug'
    task.register = 'shell'
    task.name = 'test debug'
    task.args = 'var=test'
    task.ignore_errors = True

    result = TaskResult('host', task, {'_ansible_verbose_always': True, 'failed': True, 'changed': True})
    assert result.needs_debugger() is True
   

# Generated at 2022-06-12 22:03:37.803359
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    host = "localhost"
    task = "playbook"

    return_data = {
        'changed': False,
        'failed': True,
        'invocation': {
            'module_name': 'command',
            'module_args': {
                'creates': '/home/foobar',
                'removes': '/home/foobar',
                'warn': True
            }
        },
        'stdout': "hello world",
        'stdout_lines': ["hello", "world"],
        'warnings': ['warning'],
        '_ansible_no_log': False,
        '_ansible_item_result': False,
        '_ansible_verbose_always': False
    }

    result = TaskResult(host, task, return_data)

    clean_result = result.clean_copy()

# Generated at 2022-06-12 22:03:43.197653
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    # This test only tests TaskResult.needs_debugger and TaskResult._check_key methods.
    # Thus TaskResult.__init__ and other methods are mocked.

    # Create TaskResult object.
    task = TaskResult(
        host=None,
        task=None,
        return_data={'_ansible_no_log': False},
        task_fields={
            'name': None,
            'ignore_errors': None,
            'debugger': None,
        },
    )

    # Test TaskResult._check_key method
    assert task._check_key('anykey') is False

    task._result = {'anykey': True}
    assert task._check_key('anykey') is True

    task._result = {'changed': True}
    assert task._check_key('changed') is True

    task._

# Generated at 2022-06-12 22:03:56.105647
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    from ansible.playbook import Playbook
    from ansible.playbook.task_include import TaskInclude

    task = TaskInclude()
    task.action = 'include'
    task.no_log = True

    loader = DataLoader()

    inventory = Playbook.load([], loader=loader, variable_manager=None)
    host = inventory.hosts['']


    #Test with 'failed' key in result 
    return_data = {'failed': False, 'invocation': {'module_name': 'setup', 'module_args': {}}}
    task_result = TaskResult(host, task, return_data)
    assert(task_result)

    cleaned_result = task_result.clean_copy()
    assert('failed' in cleaned_result._result)

# Generated at 2022-06-12 22:04:05.489939
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    import unittest
    class TaskResultTest(unittest.TestCase):

        """
        Unit tests for needs_debugger method of class TaskResult
        """

        def setUp(self):
            """
            Setup test case
            """
            self.task_result = TaskResult(None, None, None)
            self.task_result._task_fields = {}

        def test_name(self):
            """
            Test that method name is correct
            """
            self.assertEqual(self.task_result.needs_debugger.__name__, "needs_debugger")

        def test_debugger_always(self):
            """
            Test debugger keyword 'always'
            """
            self.task_result._task_fields['debugger'] = 'always'

# Generated at 2022-06-12 22:04:08.023589
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    my_res = TaskResult('my host', 'my task', 'my response')
    # by default, the needs_debugger method should return False
    assert not my_res.needs_debugger()



# Generated at 2022-06-12 22:04:14.644638
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    import random

    # test cases
    # (
    #   task['debugger'], task['ignore_errors'], task_result['failed'],
    #   task_result['unreachable'], globally enabled debugger, expected result,
    # )

# Generated at 2022-06-12 22:04:32.149036
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    task = Task()
    task._role = None                         # Dummy value
    task.action = None                        # Dummy value
    task.args = None                          # Dummy value
    task.delegate_to = None                   # Dummy value
    task.deprecated = None                    # Dummy value
    task.delegate_facts = None                # Dummy value
    task.environment = None                   # Dummy value
    task.failed_when_result = None            # Dummy value
    task.ignore_errors = None                 # Dummy value
    task.loop = None                          # Dummy value
    task.loop_args = None                     # Dummy value
    task.loop_with = None                     # Dummy value
    task.name = None                          # Dummy value
    task.notify