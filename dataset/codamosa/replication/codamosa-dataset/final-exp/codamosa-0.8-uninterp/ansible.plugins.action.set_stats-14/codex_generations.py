

# Generated at 2022-06-13 10:42:24.712901
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule({})
    am._task = mock()
    am._task.args = {'data': {'a':'b'}}
    am._templar = mock()

    # test that the template function is called
    am._templar.template.return_value = {'a':'b'}
    am.run(None, None)
    assert am._templar.template.call_count == 1

    # test that a dict is returned
    assert am.result['ansible_stats']['data'] == {'a':'b'}

    # test that changed tag is set correctly
    assert am.result['changed'] == False

    # test that a bool is returned
    am._task.args = {'data': {'a':'b'}, 'per_host': 'true'}
    am

# Generated at 2022-06-13 10:42:35.343000
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with no task argument
    module = ActionModule(None, None, {})
    assert module._task.args == {}

    # Test with task argument with no data
    task_args = {'data': None}
    task_args = {}
    module = ActionModule(None, None, task_args)
    assert module._task.args == {}

    # Test with task argument with empty data
    task_args = {'data': {}}
    module = ActionModule(None, None, task_args)
    assert module.run()['ansible_stats'] == {
        'data': {},
        'per_host': False,
        'aggregate': True,
    }

    # Test with task argument with valid data and no per_host or aggregate option value

# Generated at 2022-06-13 10:42:42.468964
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule

    try:
        obj = ActionModule(
                task=dict(),
                connection=dict(),
                play_context=dict(),
                loader=dict(),
                templar=dict(),
                shared_loader_obj=dict())
    except Exception as exception:
        assert False, 'failed to create object: %s' % exception

    assert obj, 'ActionModule object could not be created'
    assert isinstance(obj, ActionModule), 'ActionModule object is not an instance of ActionModule'
    assert isinstance(obj._VALID_ARGS, frozenset), 'ActionModule._VALID_ARGS is not a frozenset'
    assert isinstance(obj.TRANSFERS_FILES, bool), 'ActionModule.TRANSFERS_FILES is not a boolean'

# Generated at 2022-06-13 10:42:49.995546
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_name = 'testmodule'
    action_class = ActionModule
    module_args = {'data': {'a': 'b', 'c': 'd'}}
    test_instance = action_class(module_name, action_class._task, action_class._connection,
                                 action_class._play_context, module_args)

    assert test_instance.action_plugins_path == 'ansible.plugins.action', "Failed to set action_plugin_path"
    assert test_instance.module_name == module_name, "Failed to set module_name"
    assert test_instance.connection == action_class._connection, "Failed to set connection"
    assert test_instance.task == action_class._task, "Failed to set task"

# Generated at 2022-06-13 10:42:50.864596
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:42:51.427798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:43:02.304265
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # test_dict_with_per_host_and_aggregate_options_true_and_data_var_name_not_identifier
    stats = {'data': {}, 'per_host': True, 'aggregate': True}

    fake_task1 = {
        'args': {
            'data': {
                'var1': 1,
                'var2': 2,
                'var 3': 3
            },
            'aggregate': True,
            'per_host': True
        }
    }

    expected_result1 = {
        'changed': False,
        'ansible_stats': stats,
        'failed': True,
        'msg': "The variable name 'var 3' is not valid. Variables must start with a letter or underscore character, and contain only letters, numbers and underscores."
    }

    fake

# Generated at 2022-06-13 10:43:02.995877
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:43:10.994677
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("start test")
    # self._task.args
    # self._task.args.get('data', {})
    # self._task.args.get('aggregate', None)
    # self._task.args.get('per_host', None)

    actionModule = ActionModule()
    actionModule._task.args = {
        "data": {
            "value1": "{{test}}",
            "value2": 10,
            "value3": "test",
            "value4": "{{test[1]}}",
            "value5": "value5",
            }
        }
    actionModule._task.args['data']['value1'] = '{{test}}'
    actionModule._task.args['data']['value2'] = 10

# Generated at 2022-06-13 10:43:20.236010
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit testing for run method of class ActionModule """
    # Create mock ansible data
    mock_ansible = AnsibleData(method='run')

    # Create instance of class ActionModule
    action_module = ActionModule(mock_ansible.mock_self())

    # Create mock task data
    mock_task = AnsibleTask(mock_ansible.mock_self())

    # Create mock ansible options data
    mock_ansible_options = AnsibleOptions(mock_ansible.mock_self())

    # Create mock play context data
    mock_play_context = AnsiblePlayContext()

    # Create mock connection data
    mock_connection = AnsibleConnection()

    # Create mock ansible templar data
    mock_ansible_templar = AnsibleTemplar()


# Generated at 2022-06-13 10:43:32.877511
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global_vars = {'hostvars': {'host1': {'a': 1, 'b': 2}}}
    task_vars = {'a': 10}
    args = dict(data={'a': '{{a}}', 'b': '{{hostvars[inventory_hostname]["b"]}}'})
    task = dict(action=dict(module='set_stats', args=args))
    am = ActionModule(task, global_vars, task_vars)
    assert am.run(task_vars=task_vars) == {'ansible_stats': {'aggregate': True,
          'data': {'a': 10, 'b': 2}, 'per_host': False}, 'changed': False}


# Generated at 2022-06-13 10:43:34.608588
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert isinstance(am, ActionModule)

# Generated at 2022-06-13 10:43:40.082600
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Initiate object
    actionModule = ActionModule()

    # Check if object is correctly initiated
    assert actionModule
    assert actionModule._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
    assert actionModule.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:43:41.803415
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None)
    assert(module)

# Generated at 2022-06-13 10:43:52.620475
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize ProcessInventory() class object
    process_inventory = ProcessInventory()

    # Set values for class attributes of ProcessInventory() class object
    process_inventory._play_context = PlayContext()
    process_inventory.task = Task()

    # Create an object of 'ActionModule' class
    action_module = ActionModule(process_inventory)

    # Test case - 1
    # Test the run() method of 'ActionModule' class with valid args
    # Test the run() method of 'ActionModule' class with per_host argument
    # (True/False)

# Generated at 2022-06-13 10:44:03.751618
# Unit test for constructor of class ActionModule
def test_ActionModule():

    #from ansible.compat.tests.mock import patch
    from ansible.compat.tests import unittest
    from ansible.utils.vars import combine_vars

    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    from ansible.vars.manager import VariableManager

    class TestActionModule(ActionModule):
        _VALID_ARGS = frozenset(('action', 'name', 'per_host'))

    class TestTask(Task):
        name = 'test_task'
        action = 'test_action'

        def __init__(self, args, play_context=None):
            super(Task, self).__init__()
            self._task = self
            self._args = args
           

# Generated at 2022-06-13 10:44:13.713305
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:44:15.207263
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module.run(None, None)

# Generated at 2022-06-13 10:44:16.079066
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_ActionModule = ActionModule()


# Generated at 2022-06-13 10:44:25.488218
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test when the data is not passed
    options = {}
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    task_vars = {}
    action = ActionModule(task=MockTask(), connection=MockConnection(), play_context=MockPlayContext(), loader=MockLoader(), templar=MockTemplar(), shared_loader_obj=MockSharedLoaderObject())
    result = action.run(task_vars=task_vars)
    assert result['changed'] == False
    assert result['ansible_stats']['aggregate'] == True
    assert result['ansible_stats']['per_host'] == False
    assert result['ansible_stats']['data'] == {}

    # Test when the data is passed
    options = {}
    module = Ansible

# Generated at 2022-06-13 10:44:36.053758
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not ActionModule().run()['failed']

# Generated at 2022-06-13 10:44:37.483463
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Add your unit test for method run of class ActionModule here
    pass


# Generated at 2022-06-13 10:44:40.022886
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am is not None
    assert am._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
    assert not am.TRANSFERS_FILES


# Generated at 2022-06-13 10:44:53.860971
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import unittest
    from ansible.module_utils.ansible_modlib.parsing.convert_bool import BOOLEANS_TRUE, BOOLEANS_FALSE, boolean

    # Return a dict of the args that are expected to be passed to the
    # modules constructor and the expected value for passed args.
    def get_args():
        module_args = dict()
        for arg in ActionModule.run.__code__.co_varnames:
            if arg == 'self':
                continue
            module_args[arg] = arg
        return module_args

    class TestModule(unittest.TestCase):

        def setUp(self):
            # super() was not used in constructor of ActionModule
            self.action_module = ActionModule(get_args())


# Generated at 2022-06-13 10:44:54.971665
# Unit test for method run of class ActionModule
def test_ActionModule_run():
   # The class is for testing only, the method is available for run time use.
   return

# Generated at 2022-06-13 10:45:05.656787
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Test ActionModule.run")
    action_module = ActionModule()

    class MyTask:
        vars = {}

        def __init__(self):
            self.args = {}

    def run(tmp, task_vars):
        return {
            'changed': False,
            'ansible_stats': {
                'aggregate': True,
                'per_host': False,
                'data': {}
            }
        }

    class MyTemplar:
        def __init__(self):
            pass

        def template(self, thing, convert_bare=True, fail_on_undefined=False):
            if isinstance(thing, string_types):
                thing = "test_%s" % thing.replace(" ", "_")
                return thing
            else:
                return thing


# Generated at 2022-06-13 10:45:06.617376
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule()
    assert("ActionModule" in obj.__str__())

# Generated at 2022-06-13 10:45:16.544559
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.set_stats import ActionModule
    import sys
    import pytest

    tmpdir = pytest.ensuretemp('test_ActionModule_run')
    assert tmpdir.check(dir=1)

    task_vars = {}
    self = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    result = self.run(tmp=tmpdir.strpath, task_vars=task_vars)

    # Check result['ansible_stats'] is a dictionary
    assert isinstance(result['ansible_stats'], dict)
    assert result['changed'] is False
    assert result['failed'] is False
    assert result['msg'] is None

    assert 'data' in result['ansible_stats']

# Generated at 2022-06-13 10:45:21.244857
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test error of invalid task_vars
    action = ActionModule(dict(), dict(), False, "", "", "")
    with pytest.raises(Exception):
        action.run(None, dict())

    # Test success with minimal valid task_vars
    action = ActionModule(dict(), dict(ansible_facts=dict(), ansible_env=dict()), False, "", "", "")
    action.run(None, dict(ansible_facts=dict(), ansible_env=dict()))

# Generated at 2022-06-13 10:45:24.156038
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.module_utils.parsing.convert_bool import boolean

    module = ActionModule()
    result = module._execute_module(dict(data=dict(), per_host='yes', aggregate='no'))
    assert result['changed'] is False
    assert result['ansible_stats'] == {'data': {}, 'per_host': True, 'aggregate': False}

# Generated at 2022-06-13 10:45:53.256022
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def test_data(result):
        expected = {'changed': False, 'ansible_stats': 
                    {'per_host': False, 
                     'data': {'version': {'changed': 5, 'failures': 3}, 'time': {'seconds': 20}}, 
                     'aggregate': True}}
        assert result == expected

    def test_data_N_per_host(result):
        expected = {'changed': False, 'ansible_stats': 
                    {'per_host': True, 
                     'data': {'version': {'changed': 5, 'failures': 3}, 'time': {'seconds': 20}}, 
                     'aggregate': False}}
        assert result == expected


# Generated at 2022-06-13 10:45:55.899438
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:46:04.294971
# Unit test for constructor of class ActionModule
def test_ActionModule():
    filename = 'set_stats.py'
    m = __import__(filename[:-3])  # Load the module
    test_object = getattr(m, 'ActionModule')(None, dict())
    assert isinstance(test_object.method, string_types)
    assert isinstance(test_object.rescue, string_types)
    assert isinstance(test_object.always, string_types)
    assert isinstance(test_object.timeout, int)
    assert isinstance(test_object.delegate_to, string_types)
    assert isinstance(test_object.run_once, bool)
    assert isinstance(test_object.noop, bool)
    assert isinstance(test_object._valid_args, frozenset)

# Generated at 2022-06-13 10:46:13.090193
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test 1: Verify that module fail if no data is provided
    test_module_1 = ActionModule()
    test_task_1 = object()
    test_task_1.args = {}
    ret_test_1 = test_module_1.run(test_task_1, 'tmp')
    assert ret_test_1['failed'] is True
    assert ret_test_1['msg'] == "The 'data' option needs to be a dictionary/hash"

    # Test 2: Verify that module fail if data is not a string or a dictionary
    test_module_2 = ActionModule()
    test_task_2 = object()
    test_task_2.args = {'data': []}
    ret_test_2 = test_module_2.run(test_task_2, 'tmp')
    assert ret_test_2

# Generated at 2022-06-13 10:46:16.694370
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    data = {'a': 1, 'b': 2, 'data':  {'a': 11, 'b': 22, 'c': 33}, 'per_host': False, 'aggregate': True}
    stats = {'data': {'a': 11, 'b': 22, 'c': 33}, 'per_host': False, 'aggregate': True}

    module = ActionModule(None, data)

    assert module.run() == {'changed': False, 'ansible_stats': stats}



# Generated at 2022-06-13 10:46:20.505902
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_name = 'set_stats'
    action_path = 'ansible.builtin.set_stats'
    task_and_args = {'data': {'foo': 'bar'}}
    task = {'name': action_name, 'action': action_path, 'args': task_and_args}

    am = ActionModule(task, {}, {})

    assert type(am) == ActionModule

# Generated at 2022-06-13 10:46:24.520498
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:46:34.980610
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create instance of ActionModule with _task
    with open('./test/unit/plugins/action/set_stats.py','r') as fh:
        _task = ''.join(fh.readlines())
    action_module = ActionModule(task=_task)

    # Set required values for _task.args
    action_module._task.args['data'] = 'data_dict'

    # Create tmp file for unit test
    with open('./test/unit/plugins/action/tmp','w') as fh:
        fh.write('tmp')

    # Create a TaskVars instance for unit test
    task_vars = {}

    # Execute run method of class ActionModule with required values

# Generated at 2022-06-13 10:46:40.817506
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.set_stats import ActionModule

    am = ActionModule(None, None, None, None, None, None, None, None)

    # call method run and get result
    result = am.run()

    # check if result is good
    assert result['changed'] == False
    assert result['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}



# Generated at 2022-06-13 10:46:41.421949
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:47:34.121023
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # test with no args, per_host and aggregate should be False, and data is an empty dictionary
  # instance of ActionModule class
  action_module = ActionModule()
  # Dummy values for task_vars and tmp
  task_vars = {}
  tmp = '/tmp'
  # invokes run method with dummy values
  result = action_module.run(tmp, task_vars)
  # asserts the status of result is success
  assert result.get('failed') is False
  assert result.get('changed') is False
  # assert stats is as expected
  assert result.get('ansible_stats') == {'data': {}, 'per_host': False, 'aggregate': True}

  # test with args: test_data, per_host and aggregate should be False, and data is an empty dictionary
  # instance of ActionModule

# Generated at 2022-06-13 10:47:38.797105
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test of method run of class ActionModule
    """
    result = {'changed': False, 'msg': '', 'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}}
    assert result == ActionModule.run(None, None)

# Generated at 2022-06-13 10:47:51.032351
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    data = {'a': '1', 'b': '2', 'c': '3'}
    args = {'data': data, 'per_host': True}
    action_module._task.args = args

    # Test 1: test running with a str for the value of each var
    result = action_module.run()
    assert isinstance(result['ansible_stats'], dict)
    assert 'data' in result['ansible_stats']
    assert 'per_host' in result['ansible_stats']
    assert result['ansible_stats']['per_host'] == True
    assert 'aggregate' in result['ansible_stats']
    assert result['ansible_stats']['aggregate'] == True
    assert 'changed' in result

# Generated at 2022-06-13 10:48:02.439229
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    test_ActionModule_run tests the run() method of the ActionModule class
    """
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils.common._collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    variable_manager.set_inventory(
        Inventory(
            loader=DataLoader(),
            variable_manager=variable_manager,
            host_list='/dev/null'
        )
    )
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='/dev/null')

    # Construct a play

# Generated at 2022-06-13 10:48:04.700200
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    testActionModule = ActionModule()
    assert isinstance(testActionModule.run, object)

# Generated at 2022-06-13 10:48:14.454695
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    action = ActionModule()
    action.task = dict()
    action.task['args'] = dict()
    action.task['args']['data'] = dict()
    action.task['args']['data']['foo'] = 'FOO'
    action.task['args']['data']['bar'] = 'BAR'
    action.task['args']['per_host'] = False
    action.task['args']['aggregate'] = True
    result = action.run(task_vars=dict())

    assert not result['failed']
    assert result['ansible_stats']['per_host'] == False
    assert result['ansible_stats']['aggregate'] == True
    assert result['ansible_stats']['data']['foo'] == 'FOO'

# Generated at 2022-06-13 10:48:17.114901
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = 'localhost'
    task = dict(action=dict(module='set_stats', args=dict(data=dict(a=1, b=2), per_host=True)))
    action = ActionModule(host, task, dict(), {})

    assert action.run(None, dict()) == dict(ansible_facts=dict(), changed=False, ansible_stats=dict(data=dict(a=1, b=2), per_host=True, aggregate=True))

# Generated at 2022-06-13 10:48:21.654666
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module = ActionModule(
        {},
        {
            'task': {
                'args': {
                    'data': '{{ foo }}',
                    'aggregate': '{{ True }}'
                }
            },
            'templar': {
                'template': {}
            }
        }
    )

    assert module.run() == {
        'ansible_stats': {
            'aggregate': True,
            'per_host': False,
            'data': {}
        },
        'changed': False
    }

# Generated at 2022-06-13 10:48:24.919871
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()

    assert module.TRANSFERS_FILES is False
    assert isinstance(module._VALID_ARGS, frozenset)
    assert len(module._VALID_ARGS) == 3


# Generated at 2022-06-13 10:48:32.351076
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test 1
    tmp = None
    task_vars = dict()
    task = dict()
    args = dict()
    args['per_host'] = True
    args['aggregate'] = False
    data = dict()
    data['data1'] = 1
    data['data2'] = 2
    args['data'] = data
    task['args'] = args
    play_context = dict()
    play_context['check_mode'] = False
    datastructure = dict()
    datastructure['data_object'] = 1
    datastructure['data_object1'] = 2
    datastructure['data_object2'] = 3

    # Test 1 ActionModule instance is created
    am = ActionModule(task, play_context, datastructure)
    # Test 1, 1st run method call

# Generated at 2022-06-13 10:50:22.760650
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_me = ActionModule(super_class=None, task=None, connection=None,
                           play_context=None, loader=None, templar=None,
                           shared_loader_obj=None)
    assert test_me
    assert isinstance(test_me, ActionModule)

# Generated at 2022-06-13 10:50:30.910236
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = None
    task_vars = {}
    result = dict()

    set_stats_obj = ActionModule(tmp, task_vars)
    set_stats_obj._task.args = dict(data=dict(b=20), aggregate=True, per_host=False)
    set_stats_obj._task.args['data']['a'] = 10
    task_vars['a'] = 15
    set_stats_obj._templar.template = lambda x: x

    result = set_stats_obj.run(tmp, task_vars)

    # Testing data option
    assert result['ansible_stats']['data']['a'] == 10
    assert result['ansible_stats']['data']['b'] == 20

    # Testing aggregate option

# Generated at 2022-06-13 10:50:31.440088
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:50:39.978751
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # Test typical usage
  am = ActionModule()
  am.setup()
  host_name = 'my_host'
  am.set_loader()

  # Test host with no data
  am.set_task(dict(args=dict(data={})))
  res = am.run(task_vars={'ansible_hostname': host_name})
  assert(res['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True})

  # Test host with one variable
  am.set_task(dict(args=dict(data={'var_1':'val_1'})))
  res = am.run(task_vars={'ansible_hostname': host_name})

# Generated at 2022-06-13 10:50:41.923796
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an action
    action = ActionModule()
    # Verify that the action has the right args defined
    assert action._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:50:51.450571
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

    data = dict()
    data["n1"] = "test"
    data["n2"] = 2

    task_args = dict()
    task_args["per_host"] = "True"
    task_args["aggregate"] = "True"
    task_args["data"] = data

    task = dict()
    task["args"] = task_args

    result = dict()
    action_module._task = task
    action_module.run(task_vars = dict())

# Generated at 2022-06-13 10:50:53.644892
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None)._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:51:00.225934
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Constructor for class ActionModule
    module_args = dict(
        aggregate=True,
        data=dict(
          a=1,
          b=2,
          c=3,
          d=4,
        )
    )
    am = ActionModule(dict(), module_args, None)

    assert am.__class__.__name__ == 'ActionModule'
    assert am.TRANSFERS_FILES == False
    assert am._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

    assert am._task.args['aggregate'] == True
    assert am._task.args['data'] == dict(
          a=1,
          b=2,
          c=3,
          d=4,
        )

# Generated at 2022-06-13 10:51:00.836116
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    assert True

# Generated at 2022-06-13 10:51:01.613033
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass