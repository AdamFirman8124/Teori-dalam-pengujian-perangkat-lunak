

# Generated at 2022-06-13 10:42:19.788404
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert isinstance(am._VALID_ARGS, frozenset)
    assert am.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:42:26.326163
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act_mod = ActionModule()
    # created object should be instance of ActionModule class
    assert isinstance(act_mod, ActionModule)
    assert isinstance(act_mod._VALID_ARGS, frozenset)
    assert 'aggregate' in act_mod._VALID_ARGS
    assert 'data' in act_mod._VALID_ARGS
    assert 'per_host' in act_mod._VALID_ARGS

# Generated at 2022-06-13 10:42:33.095603
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = '/tmp/ansible-tmp-1475386370.92-42104026327881'
    task_vars = dict()

    # set up example tasks and args, then call run method
    results = dict()
    t = dict(
        action=dict(
            module='set_stats',
            args=dict(
                data=dict(
                    foo='value for foo',
                    bar='value for bar'
                ),
                per_host=True
            )
        )
    )
    a = dict()
    # after calling run method, look for ansible_stats in results
    results.update(ActionModule.run(t, a, tmp, task_vars))
    assert results['ansible_stats']['data'] == dict(foo='value for foo', bar='value for bar')

# Generated at 2022-06-13 10:42:44.426354
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for class ActionModule
    :return:
    '''
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import merge_hash

    # Set up data loader
    loader = DataLoader()

    # Create Hosts, Groups, Inventory and Variable manager
    host = Host('host')
    group = Group('group')


# Generated at 2022-06-13 10:42:46.038417
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    We have enough tests for Ansible modules, so we do not need
    to test constructor of this class.
    """
    pass

# Generated at 2022-06-13 10:42:55.124867
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    import ansible.module_utils.parsing.convert_bool
    import ansible.plugins.action

    # describe the mock object (set_stats.py)
    # when the 'run()' method is called, it returns a dictionary containing the 'ansible_stats' element
    # which contains a dictionary containing the given 'data'
    class mock_object():
        def __init__(self):
            self.args = {}
        def run(self):
            return {'ansible_stats': {'data': self.args['data']} }

    # create a mock ActionModule object
    action_module_obj = ansible.plugins.action.ActionModule(mock_object(), {})

    # test the 'run()' method with a dictionary (the returned dictionary contains the input dictionary)
    action_module_obj

# Generated at 2022-06-13 10:42:56.426307
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: implement test
    assert True

# Generated at 2022-06-13 10:43:00.130879
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #Test __init__ call
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None) is not None
    # TODO: Add more tests
    pass

# Generated at 2022-06-13 10:43:00.767954
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a=ActionModule()

# Generated at 2022-06-13 10:43:09.157184
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup the test environment and test object
    import sys
    sys.path.append('test/units/module_utils')

    from AnsibleModuleTester import AnsibleModuleTester
    tester = AnsibleModuleTester(ActionModule)

    # test case #1 - data option should be a dict
    tester.run_module(dict(data='foo'), failed=True, msg='The \'data\' option needs to be a dictionary/hash')

    # test case #2 - invalid variable names in data option
    tester.run_module(dict(data={'foo bar': 42}), failed=True, msg="The variable name 'foo bar' is not valid")

    # test case #3 - valid data option, invalid per_host option

# Generated at 2022-06-13 10:43:22.158036
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule

    def run_module():
        module_args = dict(
            data=dict(
                changed=True,
                hello='world',
            ),
            per_host=True,
            aggregate=False,
        )
        module = AnsibleModule(
            argument_spec=dict(
                data=dict(type='dict', required=False),
                per_host=dict(type='bool', required=False),
                aggregate=dict(type='bool', required=False),
            ),
            supports_check_mode=True,
        )
        module.run_command = lambda _cmd, check_rc=True: (0, "", "")
        return module.run_command('/usr/bin/sleep 0')

    m_run_command, m_fail_json,

# Generated at 2022-06-13 10:43:23.770378
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(None, None, None)
    assert mod


# Generated at 2022-06-13 10:43:31.207292
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_host = 'testhost'

    myargs = dict()
    myargs['data'] = dict(a=1, b=2)
    myargs['per_host'] = True
    myargs['aggregate'] = True
    mytmp = '/tmp'
    mytask_vars = dict()

    am = ActionModule(mytask_vars, mytmp)
    am.task_vars['inventory_hostname'] = test_host
    am.connection = 'local'

    r = am.run(myargs, mytask_vars)

    assert(r['ansible_stats'] == {'data': {'a': 1, 'b': 2}, 'per_host': True, 'aggregate': True})

# Generated at 2022-06-13 10:43:36.662982
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins
    from ansible.plugins.loader import module_loader
    from ansible.plugins.action.set_stats import ActionModule

    # Create instance of class ActionModule
    actmod = ActionModule()

    # test without 'data' specified
    result = actmod.run(task_vars=None)
    assert(result['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True})

    # test with 'data' specified as dictionary
    test_data = {'test1': 1, 'test2': 'foo', 'test3': False}
    result = actmod.run(task_vars=None, args={'data': test_data})

# Generated at 2022-06-13 10:43:49.631367
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import numpy as np
    from mock import *
    from ansible.module_utils.six import iteritems, string_types
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.action import ActionBase
    from ansible.utils.vars import isidentifier
    from ansible.module_utils.set_stats import *

    # Define the string False
    str_False = 'False'

    # Define the string True
    str_True = 'True'
    
    # Define the data to be used in run
    data = {'foo': 'value1',
            'bar': 'value2'}

    # Define the data to be used in run

# Generated at 2022-06-13 10:43:54.485537
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

    assert module.run() == {u'changed': False, u'ansible_stats': {u'aggregate': True, u'per_host': False, u'data': {}}}

    assert module.run(task_vars={'ANSIBLE_VARS': {'x': 4}}) == \
           {u'changed': False, u'ansible_stats': {u'aggregate': True, u'per_host': False, u'data': {}}}

    assert module.run(task_vars={'ANSIBLE_VARS': {'x': 4}}, tmp='/tmp/tmp') == \
           {u'changed': False, u'ansible_stats': {u'aggregate': True, u'per_host': False, u'data': {}}}


# Generated at 2022-06-13 10:43:58.018598
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None)
    if not isinstance(action, ActionModule):
        raise AssertionError("Not an instance of ActionModule")


# Generated at 2022-06-13 10:44:00.487201
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 0
test_ActionModule_run.__test__ = False  # pylint: disable=invalid-name

# Generated at 2022-06-13 10:44:11.381586
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test that both `data` and `aggregate` options can be used in the same task.
    action_module = ActionModule(dict())
    action_module._task.action = "set_stats"
    action_module._task.args = dict(data = dict(foo = 1, bar = 2), aggregate = False)
    action_module.run()

    # Test that `data` and `aggregate` can be templated.
    action_module = ActionModule(dict())
    action_module._task.action = "set_stats"
    action_module._task.args = dict(data = dict(foo = "{{ foo_var }}", bar = "{{ bar_var }}"),
                                    aggregate = "{{ is_aggregate }}")

# Generated at 2022-06-13 10:44:22.216989
# Unit test for constructor of class ActionModule
def test_ActionModule():
    TempModuleNode = collections.namedtuple('TempModuleNode', ['args', 'name'])
    TempTaskNode = collections.namedtuple('TempTaskNode', ['args', 'name'])

    # empty dict for task_vars
    task_vars = dict()

    # test no args
    task_args = dict()
    task_args['data'] = dict()
    task_args['per_host'] = dict()

    task_node = TempTaskNode(args=task_args, name='set_facts')
    module_node = TempModuleNode(args=task_args, name='set_facts')
    result = dict()

# Generated at 2022-06-13 10:44:41.746261
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def test_ActionModule_run_helper(param, expect):
        action_module = ActionModule()

        action_module._task.args = param
        ansible_stats = action_module.run()

        assert ansible_stats['ansible_stats'] == expect

    param = {}
    expect = {
        'data': {},
        'per_host': False,
        'aggregate': True
    }

    test_ActionModule_run_helper(param, expect)

    param = {
        'per_host': True,
        'aggregate': True,
        'data': {'foo': 'bar'}
    }
    expect = {
        'data': {'foo': 'bar'},
        'per_host': True,
        'aggregate': True
    }

    test_ActionModule_run

# Generated at 2022-06-13 10:44:54.775336
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import sys
    import types

    class AnsibleModuleStub:
        class Task:
            args = {'data': {}}
        class Runner:
            class TaskQueueManager:
                pass

    class AnsibleModuleStub_withTaskRunner:
        class Task:
            args = {'data': {}}
        class Runner:
            task_queue_manager = AnsibleModuleStub.Runner.TaskQueueManager()
            class CallbackQueue:
                def __init__(self, *args):
                    pass
                def _init_callback(self, *args):
                    pass
                def _process_pending_results(self, *args):
                    pass    
        class ActionBase:
            @staticmethod
            def _get_tmp_path(self, *args):
                return '/tmp/'

# Generated at 2022-06-13 10:44:58.051417
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_mod = ActionModule(
        task=dict(action=dict(module_name='set_stats', module_args=dict(data=[1,2,3])))
    )
    assert action_mod



# Generated at 2022-06-13 10:45:05.700362
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class TaskMock(object):
        def __init__(self, args):
            self.args = args

    task = TaskMock(args = {'per_host': True, 'data': {'os': 'CentOS', 'version': 7}})
    tester = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert tester._task.args == {'per_host': True, 'data': {'os': 'CentOS', 'version': 7}}

# Generated at 2022-06-13 10:45:07.799346
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am.TRANSFERS_FILES == False
    assert am._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:45:14.704846
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:45:16.289309
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(None, None, None)
    assert mod is not None

# Generated at 2022-06-13 10:45:17.611695
# Unit test for constructor of class ActionModule
def test_ActionModule():
    S = ActionModule({},{})
    assert S is not None

# Generated at 2022-06-13 10:45:21.032681
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a new object of class ActionModule
    actionmodule = ActionModule()

    # assert isinstance(actionmodule, ActionBase)

    # If the assert statement above succeeds (does not throw an AssertionError exception), then the assertion is true.
    assert True

# Generated at 2022-06-13 10:45:22.986549
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()

    assert action._task.args is not None
    assert action._loader is not None
    assert action._templar is not None
    assert action._shared_loader_obj is not None



# Generated at 2022-06-13 10:45:43.674464
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None, {})
    assert module._VALID_ARGS == frozenset(['aggregate', 'data', 'per_host'])
    assert module.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:45:53.989937
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def c(**kwargs):
        isinstance(ActionModule(None, kwargs), ActionModule)

    c(task={'args': {'data': {
        'blah': '{{ansible_processor_cores}}',
        'foobar': '{{ansible_processor_threads}}',
    }}},
      task_vars={
          'ansible_processor_cores': 1,
          'ansible_processor_threads': 4,
      })

    c(task={'args': {'aggregate': True, 'data': {'blah': 'foobar'}}},
      task_vars={})

    c(task={'args': {'per_host': True, 'data': {'blah': 'foobar'}}},
      task_vars={})


# Generated at 2022-06-13 10:45:57.064804
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None,
                        shared_loader_obj=None)

# Generated at 2022-06-13 10:46:02.985612
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert_equals = None
    new_action_module = ActionModule()
    try:
        assert_equals(new_action_module._VALID_ARGS, frozenset(('aggregate', 'data', 'per_host')))
    except NameError:
        print("ActionModule does not contain _VALID_ARGS")
    try:
        assert_equals(new_action_module.TRANSFERS_FILES, False)
    except NameError:
        print("ActionModule does not contain TRANSFERS_FILES")

# Generated at 2022-06-13 10:46:12.068618
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    task_vars = {
        'ansible_stats': {
            'data': {},
            'per_host': False,
            'aggregate': True
        }
    }

    test_class = ActionModule(None, None)

    # Case 1. Only data is provided.
    # Expected result: No failure.
    args = {
        'data': {
            'a': '1',
            'b': {
                'c': '2',
                'd': '3'
            }
        }
    }

    result = test_class.run(None, task_vars)

    assert not result.get('failed', False), 'Result failed unexpectedly'
    assert result['changed'] is False, 'Result is not changed but it should'
    assert result['ansible_stats']['aggregate'] is True

# Generated at 2022-06-13 10:46:19.430129
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule.'''
    # task_vars is a dict with key-value pairs as follows:
    # {'ansible_check_mode': False,
    #  'ansible_facts': {'hardwaremodel': 'x86_64',
    #                    'hostname': 'hostname',
    #                    'interfaces': ['lo', 'eth0'],
    #                    'kernel': 'Linux',
    #                    'kernelmajversion': '3',
    #                    'kernelrelease': '3.10.0-123.13.2.el7.x86_64',
    #                    'kernelversion': '3.10.0',
    #                    'os_family': 'RedHat',
    #                    'os_name': 'CentOS',
    #                    'os_version': '

# Generated at 2022-06-13 10:46:27.962466
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    c = ActionModule()
    d = {'status': 200, 'json': {'foo': 'bar'}, 'url': 'http://localhost:8080/'}
    e = {'changed': False, 'failed': False, 'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}}
    a = c.run(d, e)
    # assert a['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True, 'foo': 'bar'}
    # assert a['ansible_stats'] == {'data': {'status': 200, 'json': {'foo': 'bar'}, 'url': 'http://localhost:8080/'}, 'per_host': False, 'aggregate': True}
    # assert a['ansible_stats

# Generated at 2022-06-13 10:46:28.991052
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:46:34.979768
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a task for testing
    task = dict(name='test_action_module')

    # Create an ActionModule instance from the task
    action_module = ActionModule(task, [], tmp=None, connection=None)

    # Assert that the arguments of the task are valid
    assert isinstance(action_module._valid_args, frozenset)
    assert action_module._VALID_ARGS == action_module._valid_args

# Generated at 2022-06-13 10:46:45.485502
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.utils.vars import combine_vars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    action_module = ActionModule(
        task=dict(action=dict(module_name='set_stats', module_args=dict(data=dict(item=dict(key='value')), aggregate=False))),
        connection=None,
        play_context=dict(become=False),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    result = action_module.run(task_vars={})


# Generated at 2022-06-13 10:47:34.890388
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # pylint: disable=unused-variable, unused-argument
    def load_fixture(self, val):
        return load_fixture_config(val)

    def load_fixture_config(self, val):
        return {
            "status": 200,
            "content": "{}"
        }

    setattr(ActionModule, "load_fixture", load_fixture)
    module = ActionModule()
    output = {}
    test_args = {
            'data': {'foo': 'bar', 'baz': 42, 'bat': {'dog': 'cat'}},
            'per_host': True,
            'aggregate': True,
    }
    data = {'foo': 'bar', 'baz': '42', 'bat': '{dog:cat}'}
    # Test with no arguments

# Generated at 2022-06-13 10:47:41.118427
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module_args = {'data': {'foo': 'bar'}}
    module_returned = {'ansible_stats': {'data': {'foo': 'bar'}, 'per_host': False, 'aggregate': True}, 'changed': False}

    am = ActionModule(None, module_args)
    assert am.run() == module_returned

# Generated at 2022-06-13 10:47:45.325427
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module._VALID_ARGS == frozenset(['aggregate', 'data', 'per_host'])
    assert not module.TRANSFERS_FILES

# Generated at 2022-06-13 10:47:46.090156
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:47:54.219325
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #
    # ActionModule.run
    #
    # Mock task, host and task_executor objects to simulate Ansible internal
    # state
    #
    # Update various values in the fake objects and invoque the
    # ActionModule.run method. Catch and verify the output of the method.
    #
    class MockTemplar:
        def __init__(self):
            pass
        def template(self, v, convert_bare=False, fail_on_undefined=True):
            return v
    class MockTaskExecutor:
        def __init__(self, host):
            self._host = host
        def run(self, task_vars=dict()):
            return {'result': 'some_result'}

# Generated at 2022-06-13 10:47:57.707179
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()

    assert am.TRANSFERS_FILES == False
    assert am._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))


# Generated at 2022-06-13 10:47:58.392797
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:48:01.015441
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 10:48:12.482469
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from collections import namedtuple
    from ansible.playbook.task import Task
    from ansible.utils.vars import merge_hash
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    ActionModule._VALID_ARGS = frozenset()
    mock_templar = lambda x: x
    mock_task = namedtuple('mock_task', ['args'])
    args = dict(
        per_host=True,
        aggregate=False,
        data=dict(
            foo='bar',
            baz=['c', 'd', 'e'],
            f=dict(
                g=dict(
                    h=True
                )
            )
        )
    )
    result = dict(
        failed=False
    )


# Generated at 2022-06-13 10:48:22.939079
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock _execute_module
    class ActionModuleMock(_ActionModule):
        def __init__(self, *args, **kwargs):
            super(ActionModuleMock, self).__init__(*args, **kwargs)

    conn = object()
    tmp = object()
    task_vars = dict()
    del tmp  # tmp no longer has any effect

    result = _ActionModule.run(tmp, task_vars=task_vars)

    assert result['ansible_facts'] == {'ansible_stats': {'aggregate': True, 'per_host': False}}
    assert result['ansible_facts']['ansible_stats'] == {'aggregate': True, 'per_host': False}

    assert not result['failed']
    assert not result['changed']

# Generated at 2022-06-13 10:50:18.153539
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''unit test for the module run method'''

    # local import to avoid issues with module not being importable
    from ansible.module_utils.parsing.convert_bool import boolean

    test_action = ActionModule()

    # test no options specify
    result = test_action.run({}, {})

    assert result is not None
    assert result['ansible_stats']['aggregate'] is True
    assert result['ansible_stats']['data'] == {}
    assert result['ansible_stats']['per_host'] is False
    assert result['msg'] == 'OK'


    # test data option with invalid value
    result = test_action.run({}, {}, module_args={'data': 'someinvalidvalue'})

    assert result is not None
    assert result['failed'] is True
   

# Generated at 2022-06-13 10:50:21.621171
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Must be called with valid set of args.
    try:
        action = ActionModule(None, None, None, None)
    except Exception as e:
        assert False, "ActionModule must be called with valid set of args."

    assert isinstance(action._VALID_ARGS, frozenset)
    assert action.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:50:29.610803
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test ModuleTemplate constructor
    global_vars = {}
    module_name = 'test_ansible_test_module_template'
    task_vars = {'test_key': 'test_value'}
    module_args = ''
    injected_vars = {'injected_key': 'injected_value'}
    action_args = ''
    action_kwargs = {
        'task': {
            'args': {
                'per_host': True,
                'data': {'test_result': '{{ hostvars[inventory_hostname] }}'}
            }
        }
    }

    action_module = ActionModule(global_vars, module_name, task_vars, module_args, injected_vars, action_args, action_kwargs)
    action_module.run_once

# Generated at 2022-06-13 10:50:30.910045
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert isinstance(m, ActionModule)

# Generated at 2022-06-13 10:50:39.553256
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Define unit test data
    parameters = {'data': {'a': 'abc', 'b': 'def'}}
    # Define results
    results = {'changed': False, 'ansible_stats': {'per_host': False, 'data': {'a': 'abc', 'b': 'def'}, 'aggregate': True}}

    # Define mocks
    class MockTemplar(object):

        # Mock class method.

        def template(self, v, **kwargs):
            return v

    class MockActionBase(object):

        # Mock class method.

        def __init__(self, *args, **kwargs):
            return

    class MockPluginLoader(object):

        # Mock class constructor

        def __init__(self, *args, **kwargs):
            return

        # Mock class method.

# Generated at 2022-06-13 10:50:44.732015
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = dict(name = '127.0.0.1')
    connection = dict(host=host)
    module_name = 'set_stats'
    task = dict(action=dict(module=module_name, args={'data': {'sum': 32}}))
    play_context = dict(remote_addr=None)
    templar = dict()

    action_plugin = ActionModule(task, connection, play_context, templar)
    result = action_plugin.run(tmp=None, task_vars=None)
    assert result['ansible_stats'] == {'data': {'sum': 32}, 'per_host': False, 'aggregate': True}
    assert result['changed'] == False


# Generated at 2022-06-13 10:50:59.164337
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    action_module = ActionModule(task=object(), connection=None, play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None)
    assert action_module.run() == dict(changed=False, ansible_stats=dict(data=dict(), per_host=False, aggregate=True))

    # Covered: data.yml
    assert action_module.run(task_vars=dict(data='"test"')) == dict(changed=False, ansible_stats=dict(data=dict(), per_host=False, aggregate=True))

    # Covered: data.yml, per_host.yml, aggregate.yml
    assert action_module

# Generated at 2022-06-13 10:51:00.615777
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	task_vars = dict()
	assert True

# Generated at 2022-06-13 10:51:11.225534
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule, object)
    assert issubclass(ActionModule, object)
    assert issubclass(ActionModule, ActionBase)
    action_module = ActionModule(None, {}, None, None, None)
    assert action_module is not None
    assert action_module.TRANSFERS_FILES is False
    assert isinstance(action_module._VALID_ARGS, frozenset)
    assert len(action_module._VALID_ARGS) == 3
    assert 'aggregate' in action_module._VALID_ARGS
    assert 'data' in action_module._VALID_ARGS
    assert 'per_host' in action_module._VALID_ARGS


# Generated at 2022-06-13 10:51:19.547870
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    task = Task()
    task._role = None
    play_context = PlayContext()
    play_context.prompt = None
    play_context.remote_addr = None
    play_context.remote_user = None
    play_context.password = None
    play_context.port = None
    play_context.become = False
    play_context.become_method = None
    play_context.become_user = None
    play_context.verbosity = 0
    play_context.connection = "ssh"
    play_context.timeout = 10
    play_context.shell = '/bin/sh -c'