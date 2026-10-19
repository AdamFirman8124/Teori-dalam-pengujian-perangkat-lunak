

# Generated at 2022-06-13 10:42:28.799979
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mocking attributes of class ActionModule
    class ActionModuleTest(ActionModule):
        def __init__(self):
            self._task = MockTask()
            self._templar = MockTemplar()

        def _get_action_result(self, result, tmp, task_vars):
            return super(ActionModuleTest, self).run(tmp, task_vars)

    # Mocking class Task
    class MockTask():
        def __init__(self):
            self.args = {}

    # Mocking class Templar
    class MockTemplar():
        def __init__(self):
            pass

        def template(self, data, convert_bare=False, fail_on_undefined=True):
            return data

    # Instance of class ActionModule
    action_module = ActionModuleTest()

    # Define

# Generated at 2022-06-13 10:42:37.137507
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run'), "run method"
    assert hasattr(ActionModule, 'TRANSFERS_FILES'), "TRANSFERS_FILES"
    assert isinstance(ActionModule._VALID_ARGS, frozenset), '_VALID_ARGS type'
    assert 'data' in ActionModule._VALID_ARGS, 'data valid arg'
    assert 'per_host' in ActionModule._VALID_ARGS, 'per_host valid arg'


# Generated at 2022-06-13 10:42:47.008880
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.utils import context_objects as co

    class TestActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            return super(ActionModule, self).run(tmp, task_vars)

    class TestTask():
        def __init__(self, args):
            self.args = args

    class TestTaskVars(dict):
        def __init__(self, test_data, args):
            self.test_data = test_data
            self.args = args
            for k, v in iteritems(test_data['vars']):
                self[k] = v

    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.template import Templar

# Generated at 2022-06-13 10:42:56.469979
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

    # Test case 1: normal case
    module._task = {
        'args': {'data': {'key1': 'val1'}}
    }
    result = {'_ansible_verbose_always': False}
    module._templar = 'templar'
    module.run(task_vars=None, tmp=None)
    assert result['ansible_stats'] == {'aggregate': True, 'data': {'key1': 'val1'}, 'per_host': False}
    assert not result.get('failed')

    # Test case 2: template
    module._task = {
        'args': {'data': {'key1': '{{ x }}'}}
    }

# Generated at 2022-06-13 10:43:07.549441
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest

    class FakeActionModule(ActionModule):
        """
        Fake class implementing parent class methods we don't want in our unit test
        """
        def __init__(self):
            # initialize superclass
            super(FakeActionModule, self).__init__()

            # assign class variables for easy access in test case
            self._task = FakeTask()
            self._task_vars = {}

        # TODO: test this in test_action_module_set_stats
        def _execute_module(self, *args, **kwargs):
            pass

    class FakeTask:
        """
        Fake class implementing class methods we don't want in our unit test
        """
        def __init__(self):
            # initialize superclass
            self._role = None
            self._loader = None
            self._templar = None

# Generated at 2022-06-13 10:43:12.103597
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test init of ActionModule
    actionModule = ActionModule('task', None, 1, [], dict(), dict(), dict(), None, None)
    actionModule._task = dict()
    actionModule._task.args = dict()
    actionModule._task.args['data'] = {}

    # Test run of ActionModule
    result = actionModule.run(None, None)
    assert result['changed'] == False
    #assert result['failed'] == False


# Generated at 2022-06-13 10:43:21.108762
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Setup argument values for test
    args = {'per_host': False, 'aggregate': True}
    args['data'] = '{{ inventory_hostname }}'
    loop_var = 'inventory_hostname'
    # Setup hosts keys
    host1 = 'host1'
    host2 = 'host2'
    host3 = 'host3'
    host_vars = {host1: {loop_var: host1}, host2: {loop_var: host2},host3: {loop_var: host3}}
    # Setup module
    tmp = None
    task_vars = None # Does not mater here
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    am._task = Mock()
    am

# Generated at 2022-06-13 10:43:22.301512
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = ActionModule(None, None)
    # TODO: implement unit test
    pass

# Generated at 2022-06-13 10:43:31.165466
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_class_instance = ActionModule()

    # test for method run with successful input
    def test_run_success(self):
        test_class_instance._task.args = {'data': {'test_var1': 'test_value1'}, 'per_host': True}
        test_class_instance._templar.template = lambda x,y: x
        result = test_class_instance.run()
        assert result['changed'] is False, "this test should work"
        assert result['ansible_stats']['aggregate'] is True, "this test should work"
        assert result['ansible_stats']['per_host'] is True, "this test should work"
        assert isinstance(result['ansible_stats']['data'], dict), "this test should work"

# Generated at 2022-06-13 10:43:37.422220
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = module.run(tmp = None, task_vars = None)
    assert result['ansible_stats']['aggregate'] is True
    assert result['ansible_stats']['per_host'] is False
    assert len(result['ansible_stats']['data']) == 0


# Generated at 2022-06-13 10:43:43.244150
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # dummy test
    assert 'something' == 'something'

# Generated at 2022-06-13 10:43:46.663500
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = {"action": {"__ansible_module__": "set_stats", "args": {"data": {"x": "{{ y }}"}}}}
    tmp = ""
    task_vars = {"y": 1}
    m = ActionModule(task, task_vars, tmp)
    assert m.TRANSFERS_FILES == False
    assert m.run(tmp, task_vars) == {'ansible_stats': {'data': {'x': 1}, 'per_host': False, 'aggregate': True}, 'changed': False}



# Generated at 2022-06-13 10:43:47.752942
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Check the unit test in lib/ansible/plugins/action/set_stats.py
    pass


# Generated at 2022-06-13 10:43:54.580912
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys

    def display_bool(val):
        # print a bare boolean unless the value is None
        if val is None:
            return val
        return 'yes' if val else 'no'

    # create task and action
    task = MagicMock()
    action = ActionModule()

    # set task arguments
    task.args = {}

    # set action's attributes
    action._task = task
    action._templar = MagicMock()

    # test data
    data = {
        'foo': 'value for foo',
        'bar': 'value for bar',
    }
    args = {
        'data': data,
    }
    expected_stats = {
        'data': data,
        'per_host': False,
        'aggregate': True,
    }

    # run method on action
   

# Generated at 2022-06-13 10:43:55.480226
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=dict())

    # Testing the instantiation of the class
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 10:44:09.099064
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(
        task=dict(
            args=dict(
                data=dict(
                    test1=1,
                    test2=2,
                    test3=3,
                ),
                per_host=True,
                aggregate=True,
            )
        )
    )
    results = module.run()
    assert results['ansible_stats']['data'] == dict(
        test1=1,
        test2=2,
        test3=3,
    ), results
    assert results['ansible_stats']['per_host'] == True
    assert results['ansible_stats']['aggregate'] == True

    module = ActionModule(
        task=dict(
            args=dict(
                per_host="false",
                aggregate="false",
            )
        )
    )


# Generated at 2022-06-13 10:44:16.802123
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import ansible.module_utils.parsing.convert_bool

    task = dict(
        action=dict(module='set_stats', args=dict(
            aggregate=True,
            data=dict(
                success=True,
                host_success=dict(
                    ansible_test_host=True,
                    ansible_test_2_host=True
                )
            )
        )),
        task_args=dict()
    )

    tmp = None
    task_vars = dict(
        ansible_test_host='test1',
        ansible_test_2_host='test2',
    )
    m = ActionModule(task, tmp)
    m._templar.template = lambda arg, arg1=None, arg2=None, arg3=None: arg
    m

# Generated at 2022-06-13 10:44:26.548680
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import mock
    import yaml
    from ansible.module_utils.parsing.convert_bool import boolean

    # Load test data

# Generated at 2022-06-13 10:44:35.683290
# Unit test for constructor of class ActionModule
def test_ActionModule():

    class MockModule(object):
        """Class to mock the module object"""
        def __init__(self):
            self.params = dict()
            self._args = dict()

        def _set_args(self, args):
            self._args = args

        def _set_params(self, params):
            self.params = params

    class MockPlayContext(object):
        """Class to mock the play context"""

        def __init__(self):
            self.remote_addr = '127.0.0.1'
            self.connection = 'local'
            self.port = 22
            self.remote_user = 'root'

    class MockTask(object):
        """Class to mock the task object"""
        def __init__(self):
            self.action = 'set_stats'
            self.args = dict()


# Generated at 2022-06-13 10:44:43.950193
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class TestAction(ActionModule):
        def run(self, tmp=None, task_vars=None):
            return super(TestAction, self).run(tmp, task_vars)

    class TestTask(object):
        def __init__(self, args):
            self.args = args

    task = TestTask({'data': {'testvar1': '{{ testvar2 }}', 'testvar2': '{{ foo }}', 'testvar3': '{{ bar }}'},
                     'per_host': '{{ per_host }}',
                     'aggregate': '{{ aggregate }}',
                     'foo': 'foo',
                     'bar': 'bar',
                     'per_host': True,
                     'aggregate': False})
    tmp = None

# Generated at 2022-06-13 10:44:54.962552
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert type(ActionModule(task=None)) == ActionModule

# Generated at 2022-06-13 10:44:55.583629
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:44:56.526682
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule == ActionModule

# Generated at 2022-06-13 10:45:07.139324
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:45:15.537283
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = {
        'name': 'somehost',
        'address': '127.0.0.1'
    }

    task_vars = dict(hostvars=dict(somehost=host))

    action = ActionModule(task=dict(action=dict(module='set_stats'), args={}), task_vars=task_vars)

    result = action.run(task_vars=task_vars)
    assert result == dict(
        ansible_stats=dict(
            aggregate=True,
            per_host=False,
            data={}
        ),
        changed=False
    ), 'ActionModule.run does not return the expected result'

# Generated at 2022-06-13 10:45:19.088722
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'TRANSFERS_FILES')
    assert isinstance(ActionModule._VALID_ARGS, frozenset)
    assert hasattr(ActionModule, 'run')
    assert callable(ActionModule.run)

# Generated at 2022-06-13 10:45:20.149810
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action is not None

# Generated at 2022-06-13 10:45:22.912685
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None)
    assert am.TRANSFERS_FILES == False
    assert am._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:45:25.712457
# Unit test for constructor of class ActionModule
def test_ActionModule():
    config_data = '{"data": {"test_var": 123}}'
    task_data = config_data
    action = ActionModule(task_data)

    assert action._task.args['data'] == {"test_var": 123}

# Generated at 2022-06-13 10:45:34.764751
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def _dict_to_list_of_tuples(input):
        output = []
        for key, value in input.items():
            output.append((key, value))
        return output

    def _test_run_with(data, task_vars, aggregate, per_host, expected_failure=False, expected_output=None):
        # Arrange
        class _Task:
            def __init__(self, args):
                self.args = args
        class _ActionBase:
            def __init__(self, processor, tmp, task_vars):
                self._task = _Task(args)
                self._processor = processor
                self._task_vars = task_vars
            def run(self, tmp=None, task_vars=None):
                pass

# Generated at 2022-06-13 10:45:56.143119
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''test_ActionModule_run'''
    # TODO: write unit test for method run here

# Generated at 2022-06-13 10:45:59.706254
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isidentifier('a_b')
    assert isidentifier('_a')
    assert not isidentifier('_')
    assert not isidentifier('1')
    assert not isidentifier('a-b')
    assert not isidentifier('a b')

# Generated at 2022-06-13 10:46:03.097937
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(), dict(), False, '.', '.', '.')
    assert action.TRANSFERS_FILES is False
    assert action._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:46:11.284899
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(
            action=dict(module_name='', module_args='')
        ),
        connection=dict(module_name='', module_args=''),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    assert module
    assert hasattr(module, '_task')
    assert hasattr(module, '_connection')
    assert hasattr(module, '_play_context')
    assert hasattr(module, '_loader')
    assert hasattr(module, '_templar')
    assert hasattr(module, '_shared_loader_obj')

# Generated at 2022-06-13 10:46:14.549424
# Unit test for constructor of class ActionModule
def test_ActionModule():
  # test for the correct instantiation of the class
  mod = ActionModule(dict(action=dict(module_name="x", module_args=dict(a=1))), None)
  assert mod.__doc__ == 'Ansible module for collecting and reporting statistics from a task'
  assert mod._task.args.get("a") == 1

# Generated at 2022-06-13 10:46:21.367757
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class CustomActionModule(ActionModule):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            super(CustomActionModule, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)


# Generated at 2022-06-13 10:46:24.601564
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    for key in ActionModule._VALID_ARGS:
        assert key in action.VALID_ARGS

# Generated at 2022-06-13 10:46:35.058031
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am.run() == {'changed': False, 'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}}
    assert am.run(task_vars={'one': '1', 'two': '2', 'three': '3'}) == {
        u'changed': False,
        u'ansible_stats': {
            u'data': {u'one': u'1', u'two': u'2', u'three': u'3'},
            u'per_host': False,
            u'aggregate': True,
        }
    }

# Generated at 2022-06-13 10:46:45.533786
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = Mock()
    task.args = {'data': {'fact1': '1', 'fact2': '{{outcome}}'}, 'per_host': 'True', 'aggregate': 'False'}
    task.register = 'ansible_stats'
    call = Mock()
    call.template = 'success'
    templar = Mock()
    templar.template.side_effect = [{'fact1': '1', 'fact2': 'success'},
                                    True, False, 'success']
    am = ActionModule(task, connection=None, play_context=None, loader=None, templar=templar, shared_loader_obj=None)

# Generated at 2022-06-13 10:46:55.186575
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # all the tests are done with the localhost
    module = ActionModule()

    # Test to set the stats:memory_mb:101.2
    # Test to set the stats:cpu_num:4
    task_vars = {
        "ansible_stats":{
            "data":{
                "memory_mb": 101.2,
                "cpu_num": 4
            }
        }
    }

    result = module.run(
        task_vars=task_vars
    )

    assert not result['changed']
    assert result['ansible_stats'] == {
        'data': {
            'memory_mb': 101.2,
            'cpu_num': 4
        },
        'per_host': False,
        'aggregate': True
    }

    # Test to set the stats:memory_

# Generated at 2022-06-13 10:47:48.362596
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Dummy class to mock the access to the ActionBase class
    class ActionBaseMock:
        def __init__(self):
            self.tmp = None
            self.task_vars = None

    # Dummy class to mock the access to class AnsibleModule (provided by module_utils/basic.py)
    class AnsibleModuleMock:
        def __init__(self):
            self.params = {}
            self.check_mode = False
            self.no_log = True
            self.args = {'aggregate': True, 'data': {'test_1': 'var_1', 'test_2': 'var_2'}, 'per_host': False}
            self.result = {'failed': False, 'msg': '', 'ansible_stats': {}}

    # Dummy class to mock the access to the

# Generated at 2022-06-13 10:48:00.184651
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # This method should return all the stats after converting the strings, in a boolean format
    test_action_module = ActionModule()
    args = {'data': {'a': '1', 'b': '2', 'c': '3'}, 'per_host': 'true', 'aggregate': 'false'}
    test_action_module._task.args = args
    assert test_action_module._task.args == args
    assert test_action_module._task.args.get('per_host') == 'true'
    assert test_action_module._task.args.get('aggregate') == 'false'
    assert test_action_module.run(tmp=None, task_vars=None)['ansible_stats']['data']['a'] == 1

# Generated at 2022-06-13 10:48:11.911209
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of ActionModule class
    module = ActionModule()

    # Create a mock object of ActionBase class
    class ActionBase:
        class _task:
            args = {'data': {'a': '1'}}
        
        def run(self, tmp=None, task_vars=None):
            task_vars = dict()
            stats=dict()
            stats['changed'] = False
            stats['ansible_stats'] = {'data': {'a': '1'}, 'aggregate': False, 'per_host': True}
            return stats
            
    action = ActionBase()
    
    # Create a mock function of 'boolean' function with return value as True
    def mockreturn(arg, strict=False):
        return True
    
    # Create a mock object of '_templar' class

# Generated at 2022-06-13 10:48:16.026543
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test ActionModule class constructor
    """

    assert ActionModule._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
    assert not ActionModule.TRANSFERS_FILES

# Generated at 2022-06-13 10:48:26.046109
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:48:33.271367
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    ActionModule.run() Unit Test
    """

    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.play import Play
    import collections
    import copy

    # Create an object of class Task to pass to action_plugin
    task_obj = collections.namedtuple('Task', ['action', 'loop', 'loop_args',
                                               'name', 'register', 'vars',
                                               'when', 'args', 'delegate_to'])
    action_plugin = 'set_stats'
    loop = None
    loop_args = None
    task_name = 'Test set_stats'
    register = 'set_stats_register'
    vars = dict

# Generated at 2022-06-13 10:48:35.672185
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class_ = ActionModule()
    assert class_._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:48:39.052550
# Unit test for constructor of class ActionModule
def test_ActionModule():
    _VALID_ARGS = set(['aggregate', 'data', 'per_host'])

    result = ActionModule()._VALID_ARGS
    assert isinstance(result, frozenset)
    assert set(_VALID_ARGS) == set(result)

# Generated at 2022-06-13 10:48:43.118649
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # pylint: disable=too-few-public-methods
    class MyActionModule(ActionModule):
        pass

    action = MyActionModule()

    assert action.get_action_args() == {'action': 'myactionmodule'}

# Generated at 2022-06-13 10:48:47.125697
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit testing of the ActionModule constructor.
    """
    aMod = ActionModule("Fake_Path_To_Task", "Fake_module", {"data": {"var": 1}})
    assert aMod._task.args['data']['var'] == 1

# Generated at 2022-06-13 10:50:44.360445
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.action import ActionBase
    from ansible.executor.play_iterator import PlayIterator

    adhoc_path = frozenset([b'ad-hoc', b'hosts'])

    task = dict(
        action=dict(
            module=b'set_stats',
        ),
    )


# Generated at 2022-06-13 10:50:53.539772
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_ActionModule = ActionModule(
        {'name':'test_set_stats'},
        fixed_options={'connection':'ssh', 'module_name':'set_stats', 'module_args':{'data':{'test_var':'test_value'}}},
        task_uuid='12345'
    )
    result = test_ActionModule.run({'changed':False}, {'test_var':'test_value'})
    print(result)


# Generated at 2022-06-13 10:50:57.502430
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am.task is None
    assert am.connection is None
    assert am.play_context is None
    assert am.loader is None
    assert am.templar is None
    assert am.shared_loader_obj is None


# Generated at 2022-06-13 10:51:01.300617
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(am.run(), dict)

# Generated at 2022-06-13 10:51:13.263636
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Check that run method of class ActionModule generates expected results
    """

    from ansible.module_utils.parsing.convert_bool import boolean

    # default values
    stats = {'data': {}, 'per_host': False, 'aggregate': True}

    # expected results

# Generated at 2022-06-13 10:51:18.009909
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act = ActionModule(load_name='test')
    assert isinstance(act, ActionBase)
    assert act.TRANSFERS_FILES is False
    assert isinstance(act._VALID_ARGS, frozenset)
    assert 'aggregate' in act._VALID_ARGS
    assert 'data' in act._VALID_ARGS
    assert 'per_host' in act._VALID_ARGS

# test_ActionModule()

# Generated at 2022-06-13 10:51:25.767027
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # set up test data
    task_data = {'args': {'data': {'my_boolean': '{{ true }}',
                                   'my_integer': '{{ 42 }}',
                                   'my_string': '{{ "forty two" }}',
                                   'my_list': '{{ [1,2,3,4,5] }}'},
                          'per_host': 'yes'}}
    task_vars = {'foobar': 'baz'}
    tmp = None
    module_name = 'set_stats'

    # make an instance of the AnsibleModule without the imports
    am = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
        bypass_checks=True,
    )

    # create an instance of the ActionModule

# Generated at 2022-06-13 10:51:27.182355
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        # instantiate class action module
        ActionModule()
        assert True
    except:
        assert False

# Generated at 2022-06-13 10:51:32.459133
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.utils.template
    stats_args = {
        'data': {
            'foo': '{{ foo }}',
            'bar': '{{ bar }}',
            'baz': '{{ baz }}',
        },
        'per_host': '{{ per_host }}',
        'aggregate': '{{ aggregate }}',
    }

    template_args_template_dict = {
        'foo': 'FOO',
        'bar': 'BAR',
        'baz': 'BAZ',
        'per_host': True,
        'aggregate': True,
    }

    template_result = {
        'foo': 'FOO',
        'bar': 'BAR',
        'baz': 'BAZ',
        'per_host': True,
        'aggregate': True,
    }



# Generated at 2022-06-13 10:51:43.636854
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import ansible.plugins.action.set_stats
    from ansible.playbook.task import Task

    task = Task()

    stats_action = ansible.plugins.action.set_stats.ActionModule(task, task_vars={})

    # Empty data and options set
    task.args = {}
    result = stats_action.run()
    assert result['ansible_stats']['data'] == {}
    assert result['ansible_stats']['per_host'] == False
    assert result['ansible_stats']['aggregate'] == True

    # Test dictionary without templating
    task.args = {'data': {'a': 1, 'b': 2, 'c': 5}}
    result = stats_action.run()