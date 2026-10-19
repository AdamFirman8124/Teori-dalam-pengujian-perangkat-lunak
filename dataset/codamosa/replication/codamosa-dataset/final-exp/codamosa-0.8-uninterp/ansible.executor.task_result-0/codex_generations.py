

# Generated at 2022-06-12 21:54:47.041300
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():

    import json
    import sys
    import copy

    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    
    ##########################################################################
    # Set the Data and VariableManager

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    ##########################################################################
    # Make a test playbook

    loader = DataLoader()
    playbook_path = 'taskresult-test.yml'
   

# Generated at 2022-06-12 21:54:57.982173
# Unit test for method is_skipped of class TaskResult
def test_TaskResult_is_skipped():
    data = {}
    task_fields = {}
    task = TaskResult(data, data, data, task_fields=task_fields)
    assert task.is_skipped() == False
    assert task.is_skipped() == False

    data = {'results': [], 'skipped': True}
    task_fields = {}
    task = TaskResult(data, data, data, task_fields=task_fields)
    assert task.is_skipped() == True

    data = {'results': [{'skipped': True}]}
    task_fields = {}
    task = TaskResult(data, data, data, task_fields=task_fields)
    assert task.is_skipped() == True

    data = {'results': [{'skipped': False}]}
    task_fields = {}
    task = TaskResult

# Generated at 2022-06-12 21:55:04.738748
# Unit test for method is_skipped of class TaskResult

# Generated at 2022-06-12 21:55:14.676494
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    return_data = """
{
    "changed": false, 
    "msg": "All items completed", 
    "results": [
        {
            "_ansible_no_log": false, 
            "_ansible_parsed": true, 
            "changed": false, 
            "item": "sample", 
            "rc": 0, 
            "invocation": {
                "module_args": {
                    "name": "sample", 
                    "foo": "bar"
                }
            }
        }
    ]
}
    """

    result = TaskResult(None, None, return_data)
    result.clean_copy()
    assert result._result['results'][0]['invocation']['module_args']['name'] is not None

# Generated at 2022-06-12 21:55:22.741467
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    import pytest
    from ansible.playbook.task import Task

    hostname = 'testhost'
    task = Task()
    task_fields = {}

    def check_need_debugger(result, expect):
        tr = TaskResult(hostname, task, result, task_fields=task_fields)
        assert tr.needs_debugger() == expect

    # 1. failed_when_result (always failed)
    failed_when_result = dict(failed_when_result=True)
    check_need_debugger(failed_when_result, True)

    # 2. failed (can be recoverable)
    failed = dict(failed=False)
    check_need_debugger(failed, False)
    failed = dict(failed=True)
    check_need_debugger(failed, True)

    # 3. unre

# Generated at 2022-06-12 21:55:33.895360
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.module_utils._text import to_bytes as b

    class FakeTask(object):
        def __init__(self, no_log):
            self.no_log = no_log
            self.action = "command"

    class FakeHost(object):
        def __init__(self, name):
            self.name = name

    def check_result_fields(result, dict_or_list, ignored_fields, preserved_fields, subset_fields):
        if isinstance(dict_or_list, dict):
            for field in dict_or_list:
                if field in ignored_fields:
                    assert field not in result
                elif field in preserved_fields:
                    assert result[field] == dict_or_list[field]
                elif field in subset_fields:
                    assert result[field] == dict_

# Generated at 2022-06-12 21:55:42.611241
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.included_file import IncludedFile


# Generated at 2022-06-12 21:55:53.980150
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
  from yaml import load
  from ansible.parsing.yaml.objects import AnsibleUnicode


# Generated at 2022-06-12 21:55:56.293229
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    returned_data = {
        'failed': True,
        'failed_when_result': True,
        'results': [
            {
                'failed_when_result': True
            },
            {
                'failed_when_result': False
            }
        ]
    }

    task_result = TaskResult('', '', returned_data)
    assert task_result.is_failed()

# Generated at 2022-06-12 21:56:07.833705
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    class FakeTask:
        def __init__(self, action=None, no_log=None, ignore_errors=None):
            self.action = action
            self.no_log = no_log
            self.ignore_errors = ignore_errors

    C._TASK_DEBUGGER_IGNORE_ERRORS = False

    # no_log as boolean
    r = TaskResult('localhost', FakeTask(no_log=True), {'failed': True})
    assert not r.is_failed()

    # no_log as dict
    r = TaskResult('localhost', FakeTask(no_log={'msg': 'failed'}), {'failed': True, 'msg': 'failed'})
    assert not r.is_failed()

    # no_log as dict and result has no_log as dict

# Generated at 2022-06-12 21:56:24.733862
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():

    from ansible.playbook.task import Task


# Generated at 2022-06-12 21:56:33.691116
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    import unittest

    class task:
        def __init__(self, action):
            self.action = action

    # test 1
    ansible_action = 'debug'
    ansible_ignore_errors = False
    ansible_debugger = None
    task1 = task(ansible_action)
    task_fields = dict()
    task_fields['ignore_errors'] = ansible_ignore_errors
    task_fields['debugger'] = ansible_debugger
    task_result = TaskResult(None, task1, {}, task_fields)
    assert task_result.needs_debugger() == True

    # test 2
    ansible_action = 'debug'
    ansible_ignore_errors = False
    ansible_debugger = 'on_failed'
    task2 = task(ansible_action)


# Generated at 2022-06-12 21:56:43.156208
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import pytest

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task

    inventory = DataLoader().load("""
    localhost ansible_connection=local
    """)

    def _get_host(name):
        return Host(name, variables=inventory.get_host(name).get_vars())


# Generated at 2022-06-12 21:56:53.772663
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    import json
    from ansible.playbook.task import Task
    class Check:
        def __init__(self, verbosity, module_name='shell', module_args='true'):
            self.verbosity = verbosity
            self.module_name = module_name
            self.module_args = module_args
            self.check_mode = False

    def get_task(verbosity=3, action='shell', module_name='shell', args='true'):
        return Task.load(dict(action=action, module_name=module_name, module_args=args), Task(), loader=None)

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager


# Generated at 2022-06-12 21:57:00.764464
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    task = { 'debugger': 'never', 'ignore_errors': False }
    debugger_on = TaskResult('host', task, {'failed': False, 'unreachable': False})
    debugger_off = TaskResult('host', task, {'failed': True, 'unreachable': False})
    debugger_off2 = TaskResult('host', task, {'failed': False, 'unreachable': True})

    assert(debugger_on.needs_debugger() is False)
    assert(debugger_off.needs_debugger() is False)
    assert(debugger_off2.needs_debugger() is False)

    task = { 'debugger': 'always', 'ignore_errors': False }
    debugger_on = TaskResult('host', task, {'failed': False, 'unreachable': False})
    debugger_on

# Generated at 2022-06-12 21:57:10.578837
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # Arrange
    host = 'host is not needed for this test'
    task = 'task is not needed for this test'
    task_fields = dict()
    # return_data is the data that the _task.run method returns

# Generated at 2022-06-12 21:57:18.612407
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible import constants as C

    class Host:
        def __init__(self, name):
            self.name = name

    class Task:
        def __init__(self, verbose=False, no_log=False, debug=False, action="", ignore_errors=False):
            self.verbose = verbose
            self.no_log = no_log
            self.action  = action
            self.ignore_errors = ignore_errors


    class Payload:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)


# Generated at 2022-06-12 21:57:30.170430
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    """
    This test is to make sure that internal keys are removed from the TaskResult.
    """
    from ansible.playbook import task_include
    from ansible.playbook.task import Task

    host = '127.0.0.1'
    data = { "changed": False, "failed": False, "invocation": {"module_args": {"name": "test", "state": "latest"}}, "item": "", "msg": "All packages were up to date", "rc": 0, "results": [{"item": "", "msg": "All packages were up to date", "res": {"changed": False, "db": "", "invocation": {"module_args": {"name": "test", "state": "latest"}}, "item": "", "rc": 0}, "skipped": False}], "skipped": False }

    task

# Generated at 2022-06-12 21:57:41.148634
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    import ansible_runner

# Generated at 2022-06-12 21:57:52.624551
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    host = 'test_host'
    task = None
    return_data = {'failed': False,
                   'changed': False}
    task_fields = {'name': 'test',
                   'debugger': 'always'}
    result = TaskResult(host, task, return_data, task_fields)
    assert result.needs_debugger(True) == True

    task_fields = {'name': 'test',
                   'debugger': 'never'}
    result = TaskResult(host, task, return_data, task_fields)
    assert result.needs_debugger(True) == False

    task_fields = {'name': 'test',
                   'debugger': 'on_failed'}
    result = TaskResult(host, task, return_data, task_fields)

# Generated at 2022-06-12 21:58:09.105783
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.plugins.loader import action_loader

    task = action_loader.get('debug', class_only=True)()
    result = TaskResult(host='127.0.0.1', task=task, return_data={'msg': 'Kaboom!'})
    assert result.clean_copy()._result == {'msg': 'Kaboom!'}

    task = action_loader.get('setup', class_only=True)()
    result = TaskResult(host='127.0.0.1', task=task, return_data={'msg': 'Kaboom!'})
    assert result.clean_copy()._result == {'censored': "the output has been hidden due to the fact that 'no_log: true' was specified for this result"}

    task = action_loader.get('shell', class_only=True)

# Generated at 2022-06-12 21:58:20.717939
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    import unittest
    import ansible.plugins.task.debugger as debugger

    # create result object for failed task
    task_result = TaskResult(
        host="localhost",
        task=None,
        return_data={
            "failed": True
        }
    )

    class TestTaskResult(unittest.TestCase):

        def test_no_debugger(self):
            debugger._enable_task_debugger = False
            self.assertEqual(False, task_result.needs_debugger(False))

        def test_debugger_enabled_task_failed_TASK_DEBUGGER_IGNORE_ERRORS_unset(self):
            debugger._enable_task_debugger = True
            self.assertEqual(True, task_result.needs_debugger(True))


# Generated at 2022-06-12 21:58:31.777474
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    result = {
        '_ansible_parsed': True,
        '_ansible_no_log': True,
        '_ansible_item_result': True,
        '_ansible_ignore_errors': False,
        '_ansible_verbose_always': True,
        '_ansible_no_log': True,
        '_ansible_verbose_override': True,
        '_ansible_item_label': 'item0'
    }
    taskresult = TaskResult('host', 'task', result)
    copied_result = taskresult.clean_copy()

    # test whether copy is returned (not same id)
    assert copied_result._result is not result
    assert copied_result._result['_ansible_parsed'] is result['_ansible_parsed']

# Generated at 2022-06-12 21:58:39.940373
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    task = get_task_object("show_args.yaml")
    task_result = TaskResult("test", task, "fake_results")
    assert task_result.needs_debugger() == False, "Always ans always debugger does not match"
    task_result._task_fields['debugger'] = "on_unreachable"
    task_result._result['unreachable'] = True
    assert task_result.needs_debugger() == True, "On unrecheable matching failed"
    task_result._result['unreachable'] = False
    task_result._result['failed'] = True
    assert task_result.needs_debugger() == False, "On unrecheable matching failed"
    task_result._task_fields['debugger'] = "on_failed"

# Generated at 2022-06-12 21:58:47.243199
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    host = Host(name="example.org")
    variable_manager = VariableManager(loader=None, inventories=None)
    task_queue_manager = TaskQueueManager(inventory=None, variable_manager=variable_manager, loader=None,
                                          options=None, passwords=None, stdout_callback=None, run_additional_callbacks=None,
                                          run_tree=False, task_result_callback=None)
    task_queue_manager.hostvars[host] = {}
    task = Task()
    task.action = 'shell'

# Generated at 2022-06-12 21:58:56.276257
# Unit test for method clean_copy of class TaskResult

# Generated at 2022-06-12 21:59:01.588385
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    import os
    import sys
    import unittest

    from ansible.parsing.dataloader import DataLoader

    try:
        from units.compat.mock import MagicMock, patch
    except ImportError:
        from unittest.mock import MagicMock, patch

    class TestTaskResult(unittest.TestCase):

        def setUp(self):

            # patching calls to the dataloader..

            def dataLoader_load(data, show_content=False):
                return DataLoader().load(data, show_content)

            # patching calls to the dataloader..

            self.mock_data_loader = MagicMock()
            self.mock_data_loader.load = dataLoader_load


# Generated at 2022-06-12 21:59:12.185604
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    # setup
    class Task:
        def __init__(self):
            self.action = 'test'

    task = Task()

    # Test whether the debugger is called when only globally and on_failed are set, with a failed task
    C.TASK_DEBUGGER_ON = True
    on_failed = True
    always = False
    ignored_errors = False
    failed = True
    unreachable = False
    skipped = False
    task.debugger = 'on_failed'
    task.ignore_errors = ignored_errors
    result = TaskResult('localhost', task, {'failed': failed, 'unreachable': unreachable, 'skipped': skipped}, {})
    assert result.needs_debugger(globally_enabled=on_failed)

    # Test whether the debugger is called when only globally and on_failed are set,

# Generated at 2022-06-12 21:59:23.205209
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.plugins.callback.default import CallbackModule
    import json

    result = {"changed": True, "foo": "bar", "failed": False, "invocation": {"module_args": {"one": "two"}},
              "results": [{"changed": True, "foo1": "bar1"}, {"changed": False, "foo2": "bar2"}],
              "_ansible_verbose_always": True, "_ansible_verbose_override": True,
              "_ansible_parsed": True, "_ansible_item_label": "item1", "item": "item1",
              "_ansible_delegated_vars": {"ansible_host": "host1", "ansible_port": "port1"}}

    task_fields = {"ignore_errors": False, "debugger": "on_failed"}

# Generated at 2022-06-12 21:59:31.707666
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    task = None
    task_fields = None

    globally_enabled = True

    # initialize return_data
    return_data = {
        'failed': False,
        'skipped': False,
        'unreachable': False
    }

    # test for debugger: always
    task_fields = {'debugger': 'always'}
    task_result = TaskResult(None, task, return_data, task_fields)
    assert task_result.needs_debugger(globally_enabled)

    # test for debugger: never
    task_fields = {'debugger': 'never'}
    task_result = TaskResult(None, task, return_data, task_fields)
    assert not task_result.needs_debugger(globally_enabled)

    # test for debugger: on_failed

# Generated at 2022-06-12 21:59:49.704412
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import copy
    import unittest
    import unit_test.test_utils as test_utils
    from ansible.playbook.task import Task

    class TestTaskResult(unittest.TestCase):
        def test_clean_copy(self):
            # Test TaskResult._result with a dict
            test_host = 'test_host'
            test_task = Task()
            test_task_fields = dict()
            test_return_data = dict(invocation=dict(module_args=dict(a=1, b=2)),
                                    ansible_facts=dict(some=dict(deep=dict(fact='value')), another='no deep fact'),
                                    changed=True,
                                    failed=False,
                                    skipped=False,
                                    unreachable=False)

# Generated at 2022-06-12 22:00:00.580040
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    task_fields = {"name": "test"}
    host = "fakehost"
    task = Task()
    task.no_log = True
    json = """{
  "failed": true,
  "invocation": {
    "module_args": "",
    "module_name": "test"
  },
  "_ansible_parsed": true
}"""
    return_data = DataLoader().load(json)

    original_task_result = TaskResult(host, task, return_data, task_fields)
    clean_task_result = original_task_result.clean_copy()

    assert clean_task_result._result == {'censored': 'the output has been hidden due to the fact that \'no_log: true\' was specified for this result'}
   

# Generated at 2022-06-12 22:00:11.614437
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    import ansible.playbook.task
    task = ansible.playbook.task.Task()

    tr = TaskResult(None, task, {'foo': 1, 'bar': 2, 'changed': True})
    tr_copied = tr.clean_copy()

    assert tr._result.get('changed')
    assert tr_copied._result.get('changed')
    assert tr._result.get('foo') == tr_copied._result.get('foo')
    assert tr._result.get('bar') == tr_copied._result.get('bar')

    tr = TaskResult(None, task, {'foo': 1, 'bar': 2, 'no_log': True})
    tr_copied = tr.clean_copy()

    assert not tr._result.get('no_log')
    assert not tr_copied._

# Generated at 2022-06-12 22:00:21.120974
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    task = Task()
    host = Host(name='myhost')
    task_fields = dict()
    return_data = None

    task_result = TaskResult(host, task, return_data, task_fields)
    assert task_result.clean_copy() is not None
    assert task_result.clean_copy()._result == None

    # return_data is string

# Generated at 2022-06-12 22:00:25.546681
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    '''

    :return:
    '''
    task_fields = {}
    task = TaskResult({}, {}, {}, task_fields)
    res_clean_copy = task.clean_copy()
    assert res_clean_copy



# Generated at 2022-06-12 22:00:33.623065
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    result = dict(failed=True)
    task = dict(no_log=True)
    host = dict()
    task_result = TaskResult(host, task, result)
    assert task_result.clean_copy() == dict(censored="the output has been hidden due to the fact that 'no_log: true' was specified for this result")
    # the method does not change the original object
    assert task_result._result == dict(failed=True)
    assert task_result.task_name == None
    assert not task_result.is_changed()
    assert not task_result.is_failed()
    assert not task_result.is_skipped()
    assert not task_result.is_unreachable()
    assert not task_result.needs_debugger()


if __name__ == '__main__':
    test

# Generated at 2022-06-12 22:00:45.084490
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # Test object creation
    task_result = TaskResult('host.example.org', None, {'excluded_key': 'removed', 'censored': 'removed too', '_ansible_no_log': True, '_ansible_item_label': 'filtered'})
    assert isinstance(task_result, TaskResult)

    # Test clean_copy
    assert isinstance(task_result.clean_copy(), TaskResult)

    # Test censoring
    clean = task_result.clean_copy()
    assert 'censored' in task_result._result
    assert 'censored' in clean._result
    assert 'the output has been hidden due to the fact that \'no_log: true\' was specified for this result' in clean._result['censored']

    # Test cleaning

# Generated at 2022-06-12 22:00:49.175248
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    d = dict(
        name="mike",
        ignore_errors=True,
        debugger="never",
    )
    task = Task.load(d, ds=None, role=Role())
    block = Block.load(d, ds=None, task_include=task, role=Role())
    task._parent = block

    # is_failed=False, is_unreachable=False, is_skipped=False
    result = TaskResult(None, task, dict(
        changed=False,
        failed=False,
        failed_when_result=False,
        unreachable=False,
        skipped=False,
    ))
    assert not result.needs_debug

# Generated at 2022-06-12 22:00:57.560469
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    host_mock = None
    task_mock = None
    return_data = {
        'invocation': {
            'module_name': 'setup',
        },
        'skipped': True,
    }
    task_fields = dict()

    result = TaskResult(host_mock, task_mock, return_data, task_fields)
    clean_result = result.clean_copy()

    # Check if the task was skipped
    assert clean_result.is_skipped() == return_data.get('skipped', False)

    # Check that the invocation field has been removed
    assert 'invocation' not in clean_result._result

# Generated at 2022-06-12 22:01:06.772294
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    task = type('FakeTask',(object,),{"get_name":lambda x: "name"})()
    task_fields = {'name':'name'}

    # Test is_failed when return_data is dict
    return_data = {'failed':True}
    result = TaskResult(None,task,return_data,task_fields)
    assert result.is_failed() == True

    # Test is_failed when return_data is string
    return_data = "{'failed':True}"
    result = TaskResult(None,task,return_data,task_fields)
    assert result.is_failed() == True

    # Test is_failed when the key failed doesn't exist in the return_data
    return_data = "{'fail':True}"
    result = TaskResult(None,task,return_data,task_fields)

# Generated at 2022-06-12 22:01:20.342666
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from collections import namedtuple
    from ansible import constants

    # create required objects for creating a TaskResult instance
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-12 22:01:27.563385
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    # Test a regular task
    task = TaskResult('localhost', 'dummy_task', {
        'task': 'dummy_task',
        '_ansible_parsed': True,
        'module_name': 'concat',
        'msg': 'Hello',
        'failed': False,
        'changed': True,
        'stderr': 'Error',
        'stdout': 'Output',
        'rc': 0,
    })

    task_copy = task.clean_copy()

    assert task_copy._host == 'localhost'
    assert task_copy._task == 'dummy_task'
    assert task_copy._result['failed'] is False
    assert '_ansible_parsed' not in task_copy._result
    assert 'msg' in task_copy._result
    assert 'stderr'

# Generated at 2022-06-12 22:01:38.044445
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    result = dict(
        ansible_facts=dict(
            a=1
        ),
        key1='value1',
        key2='value2',
        failed=True,
        _ansible_no_log=True,
        item='myitem',
        ansible_env=C.HOST_VARS_EXTRAS,
        _ansible_item_label=1,
        _ansible_verbose_always=True,
        _ansible_ignore_errors=True,
        _ansible_delegated_vars={
            'ansible_host': 'localhost',
            'ansible_port': 2222,
            'ansible_user': 'newuser',
            'ansible_connection': 'local'
        }
    )

# Generated at 2022-06-12 22:01:48.302110
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from collections import namedtuple

    Host = namedtuple('Host', ['name'])
    host = Host(name="testhost")
    task = Task()

    loader = DataLoader()
    inventory = InventoryManager(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    return_data = {
        "failed": False,
            "invocation": {
                "module_args": "echo hello",
            },
            "item": "hello",
            "changed": False
        }

# Generated at 2022-06-12 22:01:59.579393
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    import pytest

    class FakeHost(object):
        pass

    class FakeTask(object):
        name = 'fake_task'
        action = 'fake_action'
        ignore_errors = False

        @property
        def no_log(self):
            return False

    # _debugger is None, ignore_errors is False
    task = FakeTask()
    result_when_failed = TaskResult(FakeHost(), task, {'failed': True}, task_fields={})
    result_when_unreachable = TaskResult(FakeHost(), task, {'unreachable': True}, task_fields={})
    result_when_failed_with_globally_enabled = TaskResult(FakeHost(), task, {'failed': True}, task_fields={})
    result_when_unreachable_with_globally_enabled = TaskResult

# Generated at 2022-06-12 22:02:05.628050
# Unit test for method is_failed of class TaskResult

# Generated at 2022-06-12 22:02:16.517955
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    class FakeHost:
        def __init__(self):
            self.name = 'fake_host'

    class FakeTask:
        def __init__(self):
            self.action = 'fake_action'
            self.no_log = True

    from ansible.utils.display import Display

    dummy_display = Display()
    d = dict(changed=True, result="this is a test",
             _ansible_no_log=True,
             invocation=dict(module_name='fake_module',
                             module_args="fake_args",
                             module_complex_args=dict(a_complex_arg="complex_value")))

    taskresult = TaskResult(FakeHost(), FakeTask(), d)
    d_copy = taskresult.clean_copy()


# Generated at 2022-06-12 22:02:27.849878
# Unit test for method clean_copy of class TaskResult

# Generated at 2022-06-12 22:02:34.587926
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    results = [
        # [ is_failed_when_result, expected is_failed, expected is_skipped ]
        [ True, True, False ],
        [ False, False, False ],
        [ None, False, False ],
        [ '', False, False ],
        [ 1, True, False ],
        [ 0, False, False ]
    ]

    for result in results:
        is_failed_when_result, expected_is_failed, expected_is_skipped = result

        task_result = TaskResult(None, None, create_test_dict('failed', 'failed_when_result', is_failed_when_result))
        assert expected_is_failed == task_result.is_failed()
        assert expected_is_skipped != task_result.is_skipped()


# Generated at 2022-06-12 22:02:43.538864
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task

    class Host:
        def __init__(self, name):
            self.name = name

    host = Host('localhost')

    task = Task()
    task.name = 'test_TaskResult_clean_copy'
    task.action = 'debug'

    # basic test

# Generated at 2022-06-12 22:03:03.557656
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    import unittest
    import ansible.executor.task_result

    class TestTaskResultDebugger(unittest.TestCase):

        def test_needs_debugger_tag_failure(self):
            t = ansible.executor.task_result.TaskResult(host=None, task=None, return_data={"failed": True}, task_fields={"name":"test","debugger":"always"})
            self.assertTrue(t.needs_debugger())

        def test_needs_debugger_tag_unreachable(self):
            t = ansible.executor.task_result.TaskResult(host=None, task=None, return_data={"unreachable": True}, task_fields={"name":"test","debugger":"always"})
            self.assertTrue(t.needs_debugger())


# Generated at 2022-06-12 22:03:12.262229
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    DataLoader().set_basedir('/tmp/')

    # 1. Result has failed key
    assert TaskResult(None, None, {'failed': True}).is_failed()
    assert TaskResult(None, None, {'failed': False}).is_failed()

    # 2. Result has failed_when_result key
    assert TaskResult(None, None, {'failed_when_result': True}).is_failed()
    assert TaskResult(None, None, {'failed_when_result': False}).is_failed()

    # 3. Result has results key.
    #    True case: all 'result' has failed key and value is True.
    assert TaskResult(None, None, {'results': [{'failed': True}]}).is_failed()

# Generated at 2022-06-12 22:03:19.622831
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    # set up task and result for testing
    task_fields = dict()
    task_fields['action'] = 'debug'
    task_fields['name'] = 'mock task'
    task_fields['ignore_errors'] = False
    task_fields['debugger'] = None
    task = mock_task(task_fields=task_fields)
    result = mock_task_result(task)

    # add some random keys to result
    result['_ansible_ignore_errors'] = False
    result['_ansible_no_log'] = False
    result['changed'] = True
    result['failed'] = True
    result._ansible_delegated_vars = dict()
    result._ansible_delegated_vars['ansible_host'] = 'localhost'
    result._ansible_delegated_vars

# Generated at 2022-06-12 22:03:27.487457
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():

    from ansible.playbook.task import Task

    task1 = Task()
    task2 = Task()
    task3 = Task()

    task_fields1 = {'debugger': 'always'}
    task_fields2 = {'ignore_errors': True, 'debugger': 'on_failed'}
    task_fields3 = {'ignore_errors': True, 'debugger': 'on_skipped'}

    task1._parent = {'_task_fields': task_fields1}
    task2._parent = {'_task_fields': task_fields2}
    task3._parent = {'_task_fields': task_fields3}

    # test case 1:  debugger = always
    result1 = TaskResult('a', task1, {'failed': True})

# Generated at 2022-06-12 22:03:32.927596
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    from ansible.playbook.task import Task

    host = 'localhost'
    task = Task()

    return_data_1 = {"failed_when_result": True}
    task_fields_1 = None
    result_1 = TaskResult(host, task, return_data_1, task_fields_1)
    assert result_1.is_failed() == True

    return_data_2 = {"results": [{"failed_when_result": True}]}
    task_fields_2 = None
    result_2 = TaskResult(host, task, return_data_2, task_fields_2)
    assert result_2.is_failed() == True

    return_data_3 = {"results": [{"failed_when_result": False}]}
    task_fields_3 = None

# Generated at 2022-06-12 22:03:38.170024
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    from ansible.plugins.action.debug import ActionModule as debug_action
    from ansible.playbook.task import Task

    loader = DataLoader()
    task_fields = dict()

    def get_name():
        return task_name

    def debug_var_ret(results):
        # just put what we were asked to in the result
        try:
            msg = results[0]
            result = results[1]
        except KeyError:
            result = {}
        result['debug_var'] = {msg: result.pop('var')}
        return result

    debug_action.ActionModule.return_values = debug_var_ret

    import json

# Generated at 2022-06-12 22:03:43.442626
# Unit test for method needs_debugger of class TaskResult
def test_TaskResult_needs_debugger():
    task_fields = dict(ignore_errors=True)
    task_fields['debugger'] = 'always'
    success_result = TaskResult('localhost', 'fake task', {
        'changed': False,
        'invocation': {'module_name': 'ping', 'module_args': ''}
    }, task_fields)
    assert success_result.needs_debugger(True)
    task_fields['debugger'] = 'on_failed'
    assert not success_result.needs_debugger(True)
    failure_result = TaskResult('localhost', 'fake task', {
        'failed': True,
        'invocation': {'module_name': 'ping', 'module_args': ''}
    }, task_fields)
    assert failure_result.needs_debugger(True)

# Generated at 2022-06-12 22:03:56.379561
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():

    host = 'localhost'
    task = None
    return_data = {}
    task_fields = {'name': 'test'}

    task_result = TaskResult(host, task, return_data, task_fields)


# Generated at 2022-06-12 22:04:05.772492
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.vars.manager import VariableManager
    from ansible.inventory import Inventory
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.plugins.loader import callback_loader
    import json
    import yaml


# Generated at 2022-06-12 22:04:07.623183
# Unit test for method is_failed of class TaskResult
def test_TaskResult_is_failed():
    u1 = TaskResult(None, None, {'failed': True})
    assert u1.is_failed() == True


# Generated at 2022-06-12 22:04:28.503461
# Unit test for method clean_copy of class TaskResult
def test_TaskResult_clean_copy():
    from ansible.playbook.task import Task

    task_fields = dict(action=dict(module='setup', args={'filter': 'ansible_distribution'}))
    task = Task()
    task._ds = task_fields
