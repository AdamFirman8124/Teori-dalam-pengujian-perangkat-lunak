

# Generated at 2022-06-13 10:42:28.408624
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest

    # test expection for TemplateError
    with pytest.raises(Exception) as excinfo:
        mod = ActionModule()
        mod.run(None, None)
    assert 'stats is undefined' in str(excinfo.value)

    # test expection for TemplateError
    with pytest.raises(Exception) as excinfo:
        mod = ActionModule()
        mod.run(None, dict(stats={'foo': '{{bar}}'}))
    assert 'bar is undefined' in str(excinfo.value)

    # test expection for AssertionError
    with pytest.raises(AssertionError) as excinfo:
        mod = ActionModule()
        mod.run(None, dict(stats=dict(foo=[])))

# Generated at 2022-06-13 10:42:41.050712
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global_vars = {
        'vars' : {
            'stat1' : 'stat1_value',
            'stat_value_int' : 99,
            'stat_value_bool_true' : True,
            'stat_value_bool_false' : False,
        },
    }

    class FakeTemplar(object):
        def __init__(self):
            pass
        def template(self, s, convert_bare=False, fail_on_undefined=True, silence_undefined=True):
            if not s in global_vars['vars']:
                raise Exception("Invalid template")
            return global_vars['vars'][s]

    class FakeTask(object):
        pass

    am = ActionModule()
    am._templar = FakeTemplar()
    am._

# Generated at 2022-06-13 10:42:49.252875
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task=dict(
            args=dict(
                data=dict(
                    x=1,
                    y=2,
                    z=3,
                    k="abc"
                ),
                aggregate=False,
                per_host=False,
            )
        )
    )
    action.included_filters = []
    action.included_filters.extend(ActionBase._configuration_filters)
    action.included_filters.extend(ActionBase._default_filters)
    action.task_vars = dict()
    action.templar = action.get_templar()
    result = action.run(
        task_vars=dict()
    )
    assert result['ansible_stats']['data']['x'] == 1
    assert result

# Generated at 2022-06-13 10:42:52.651788
# Unit test for constructor of class ActionModule
def test_ActionModule():
   actionmodule = ActionModule(None, None)
   assert actionmodule._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
   assert actionmodule.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:42:53.721235
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:43:04.416443
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class TestAction(ActionModule):
        TRANSFERS_FILES = False
        _VALID_ARGS = frozenset(('aggregate', 'data', 'per_host'))

        def __init__(self):
            self._task = None

        def run(self, tmp, task_vars=None):
            return super(TestAction, self).run(tmp, task_vars)

    action = TestAction()

    # test that data option must be dict
    task = dict()
    task['args'] = dict()
    task['args']['data'] = '{}'
    action._task = task

    results = action.run(tmp=None, task_vars=None)
    assert results['msg'] == "The 'data' option needs to be a dictionary/hash"
    assert results['failed']

   

# Generated at 2022-06-13 10:43:06.021927
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:43:13.423074
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    params = {
        'data': {
            'test_1': '{{ test_var_1 }}',
            'test_2': '{{ test_var_2 }}'
        },
        'per_host': True,
        'aggregate': False
    }
    task_vars = {
        'test_var_1': 1,
        'test_var_2': 'var_value_2'
    }
    tmp = None

    action_base_mock = ActionBase(task=None, connection='', play_context='', loader='', templar='', shared_loader_obj='')

    action_module_mock = ActionModule(task=None, connection='', play_context='', loader='', templar='', shared_loader_obj='')

# Generated at 2022-06-13 10:43:21.676798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    from collections import namedtuple
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.ajson import AnsibleJSONEncoder
    from ansible.parsing.convert_bool import boolean

    # import module locally
    sys.path.insert(0, os.path.abspath('../../lib/ansible/modules/system'))

    import set_stats

    # create mock ansible module
    mock_args = dict(
        data=dict(
            key1=1,
            key2='value2',
        ),
        per_host=False,
        aggregate=True,
    )

# Generated at 2022-06-13 10:43:30.697312
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    # Set up mocks and other test stuff needed
    mock_templar, mock_task, mock_self = setup_mocks()

    # Create the object that will be tested
    action_module = ActionModule(mock_task, mock_templar, None)

    # Create the return value for the module execution
    mock_templar.return_value = True
    mock_task.args = {'test_data': {'test_key': 'test_value'}}

    # Execute the method being tested
    result = action_module.run()

    # Check the results
    assert result['changed'] == False

# Generated at 2022-06-13 10:43:38.404415
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule._VALID_ARGS == ('aggregate', 'data', 'per_host')
    assert ActionModule.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:43:44.718578
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    action = ActionModule(None, None)
    assert action.run(None, None) == {
        'changed': False,
        'ansible_stats': {
            'data': {},
            'per_host': False,
            'aggregate': True,
        }
    }

# Generated at 2022-06-13 10:43:53.670361
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(load_params=dict())
    assert not module.run()["failed"]
    assert module.run(dict(data=dict(a=1, b=5.5, c="hello", d="world")))["ansible_stats"]["data"] == \
                      dict(a=1, b=5.5, c="hello", d="world")
    assert module.run(dict(data=dict(a=1, b=5.5, c="hello", d="world", e="{{a}}")))["ansible_stats"]["data"] == \
                      dict(a=1, b=5.5, c="hello", d="world", e="1")

# Generated at 2022-06-13 10:44:07.921013
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six.moves import builtins
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_context import PlayContext
    from ansible.executor.task_executor import TaskExecutor
    from ansible.plugins.action.set_stats import ActionModule
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    import pytest

   

# Generated at 2022-06-13 10:44:15.393175
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # set up class instance to be used in test cases
    am = ActionModule()
    # set up args for test cases
    args = {}
    # set up task_vars for test cases
    task_vars = {}

    # ################
    # test case 1 - data=123
    args['data'] = 123
    result = am.run(None, task_vars)
    assert result['failed'] == True
    assert result['msg'] == "The 'data' option needs to be a dictionary/hash"

    # ################
    # test case 2 - data=['a','b','c']
    args['data'] = ['a', 'b', 'c']
    result = am.run(None, task_vars)
    assert result['failed'] == True

# Generated at 2022-06-13 10:44:17.388750
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    task_vars = dict()
    module.run(tmp = None, task_vars = task_vars)

# Generated at 2022-06-13 10:44:26.916454
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    def _get_task(dummy_loader, task_path, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        task = Task()
        task._role = None
        task.args = {}
        task.action = 'statistics'
        task.vars = task_vars

        return task

    # Create a test object of ActionModule
    am = ActionModule(dummy_loader, {}, {}, _get_task, None)

    # Test return values of run method
    assert(am.run(tmp=None, task_vars={})['ansible_stats']['aggregate'] == True)

# Generated at 2022-06-13 10:44:35.950714
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.utils.vars import combine_vars
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    module_args = dict(
        aggregate=False,
        per_host=True,
        data=dict(
            one=1,
            two=0,
            three=dict(
                four=4,
                five=5,
                six=6
            ),
        )
    )

    am = ActionModule(dict(
        task_vars=dict(
            var_1="var_1",
            var_2=1,
            var_3=True,
        ),
        play_context=dict(
            vault_password="1234",
        )
    ))


# Generated at 2022-06-13 10:44:38.164473
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:44:45.638262
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(omit=['task_vars'])
    set_stats = ActionModule(dict(task_vars=task_vars, tmp='/tmp'),
                             dict(action=dict(set_stats=dict(args=dict(data=dict(a=1, b=2),
                                                                       per_host=True,
                                                                       aggregate=False)))))
    set_stats_result = set_stats.run(None, task_vars)
    assert set_stats_result['failed'] is False, \
        "set_stats should not have failed, got: {0}".format(set_stats_result['msg'])

# Generated at 2022-06-13 10:45:05.474695
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    This is just a sample unit test for ActionModule class. It is not expected to be executed as part of normal test suite.
    """
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    import ansible.constants as C

    class FakeOptionModule(object):
        connection = 'local'
        forks = C.DEFAULT_FORKS
        become = None
        become_method = None
        become_user = None
        check = False
        diff = False
        remote_user = 'testuser'

    task = Task()
    task._role = None
    task._block = None
    task._play = None
    task._ds = None
    task._loader = None

    fake_task_v

# Generated at 2022-06-13 10:45:08.443628
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(args={'data': {'xyz': 'abc'}, 'per_host': True}),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)
    assert module

# Generated at 2022-06-13 10:45:11.488269
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test one: check that constructor return a instance of expected class
    test_one = ActionModule(None, None)
    assert isinstance(test_one, ActionBase)
    assert test_one._task.action == "set_stats"

# Generated at 2022-06-13 10:45:22.434534
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = None
    task_vars = {'ansible_facts': {'sample': 'value'}}
    results = {'ansible_stats': {'data': {'sample': 'value'}, 'per_host': False, 'aggregate': True}, 'failed': False, 'changed': False}
    # mock class for AnsibleModule to use return values
    module = MockAnsibleModule()

    set_stats = ActionModule(task=MockTask(), connection=MockConnection(), templar=MockTempler())
    assert set_stats._task.args == {}
    assert set_stats._task.action == 'set_stats'
    # mock class for AnsibleModule to use as superclass
    assert set_stats.run(tmp, task_vars) == results
    # mock class for AnsibleModule to use return values


# Generated at 2022-06-13 10:45:25.690396
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module

# Generated at 2022-06-13 10:45:26.465836
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(True)

# Generated at 2022-06-13 10:45:34.634003
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test branch of code where no args are passed

    # create the object
    a = ActionModule(None, None, None, None, None, {})
    
    # call the method which we want to test
    result = a.run()
    agg = result['ansible_stats']['aggregate']
    assert agg == True

    # test branch of code where args are passed
    # create the object
    a = ActionModule(None, None, None, None, None, {'data': {'a': 1, 'b': 2}, 'aggregate': False})
    
    # call the method which we want to test
    result = a.run()
    agg = result['ansible_stats']['aggregate']
    assert agg == False

# Generated at 2022-06-13 10:45:46.784043
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import logging
    import unittest
    class MockTemplar(object):
        def __init__(self, *args, **kwargs):
            pass
        def template(self, *args, **kwargs):
            return args[0]
    class MockTask(object):
        def __init__(self, *args, **kwargs):
            self.args = {}
    class MockTaskVars(object):
        def __init__(self, *args, **kwargs):
            pass

    # Error: Invalid type for 'data'
    actionModule = ActionModule(logging.getLogger())
    actionModule._templar = MockTemplar()
    actionModule._task = MockTask()
    actionModule._task.args['data'] = True
    #self.assertRaises(TypeError, actionModule.run())

# Generated at 2022-06-13 10:45:47.725929
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, dict(), True)
    assert action

# Generated at 2022-06-13 10:45:48.772378
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:46:08.113810
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule, "Constructor of class ActionModule should exists"


# Generated at 2022-06-13 10:46:13.058168
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Importing 'ansible.module_utils.facts.system.base' raises
    # ImportError, so we cannot import it
    import ansible.module_utils.facts.system.base
    act = ActionModule(ansible.module_utils.facts.system.base.BaseFactCollector(),
                       dict(action=dict(module_name='set_stats', module_args=dict())))
    assert act.run() == {}
    return True

# Generated at 2022-06-13 10:46:14.945695
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am  = ActionModule()
    am.task_vars = {}
    assert am.run() == {'changed': False, 'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}}

# Generated at 2022-06-13 10:46:15.344427
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:46:20.813430
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create mock module
    module_mock = MagicMock()
    module_mock.params = None
    module_mock.run_command.return_value = (0, 'ok')
    module_mock.run_command.return_value = (0, 'ok')
    base_mock = MagicMock()
    base_mock.run.return_value = {'failed': False, 'ansible_facts': {'test': 'success'}}

    # set up ActionModule object
    mod = ActionModule(module_mock, base_mock)
    mod.set_runner = MagicMock()

    # set up return value of ActionModule.set_runner
    stat = {'data': {'test': 'success'}, 'per_host': False, 'aggregate': True}

# Generated at 2022-06-13 10:46:24.968248
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None)

    assert(isinstance(module._VALID_ARGS, frozenset))
    assert(len(module._VALID_ARGS) == 3)
    assert('aggregate' in module._VALID_ARGS)
    assert('data' in module._VALID_ARGS)
    assert('per_host' in module._VALID_ARGS)

# Generated at 2022-06-13 10:46:26.019353
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:46:36.085167
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test with no args
    actionModule = ActionModule()
    result = actionModule.run(None, None)

    assert 'failed' not in result
    assert result['msg'] is None
    assert result['changed'] is False

    # test with fail level data
    testObject = type('testObject', (object,), {'args': {'data': 'blah'}})
    actionModule = ActionModule()
    actionModule._task = testObject
    result = actionModule.run(None, None)

    assert result['failed'] is True
    assert result['msg'] == "The 'data' option needs to be a dictionary/hash"

    # test with valid data
    testObject = type('testObject', (object,), {'args': {'data': {'stat1': 1, 'stat2': 2}}})

# Generated at 2022-06-13 10:46:41.218162
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod=ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert mod.run(tmp=None, task_vars=None) == {'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}, 'changed': False}

# Generated at 2022-06-13 10:46:50.186784
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule('set_stats', 'data', {'data': {'success': True, 'ignored': False}}, True, {}, {'tasks': [{'action': 'set_stats', 'args': {'data': {'success': True, 'ignored': False}}}]}, None, 'tasks', 0, None)
    task_result = action.run(None, {'data_foo': {'success': True, 'ignored': False}})
    assert task_result['ansible_stats']['data']['success'] == True
    assert task_result['ansible_stats']['data']['ignored'] == False


# Generated at 2022-06-13 10:47:32.455363
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule(1, 1, 1)
    assert obj._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
    assert obj.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:47:40.789383
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # arrange
    import utils.module_utils.basic
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible import context
    from ansible.plugins.action import ActionBase

    class ActionModuleTest(ActionModule):
        def run(self, tmp=None, task_vars=None):
            return super(ActionModuleTest, self).run(tmp, task_vars)

# Generated at 2022-06-13 10:47:52.113785
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import MutableMapping

    from ansible.plugins.loader import action_loader
    from ansible.template import Templar
    from ansible.vars import VariableManager

    def get_connection():
        return None

    def get_module_path(module_name):
        if module_name not in ['stat', 'copy', 'file']:
            raise Exception("What is this module name " + module_name)
        else:
            return ''

    def get_loader(module_name):
        return action_loader

    loader = get_loader('stat')

# Generated at 2022-06-13 10:48:03.274244
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for `ActionModule.run` method for class `ActionModule`."""

    # Test fixture
    invalid_data_input = """
      data: '{{ test_var }}'
    """
    invalid_data_output = {
        'ansible_stats': {
            'aggregate': True,
            'data': {},
            'per_host': False,
        },
        'changed': False,
        'failed': True,
        'msg': "The 'data' option needs to be a dictionary/hash"
    }

    # Test setup
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:48:06.240397
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test the module
    """
    ap = ActionModule()
    temp = {}
    ap.run(tmp=temp)

# Generated at 2022-06-13 10:48:08.300838
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule(load_fixture=False, action_plugin=None)



# Generated at 2022-06-13 10:48:09.440530
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:48:21.967994
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager

    module = AnsibleModule(
        argument_spec = dict(
            aggregate = dict(type='bool', required=False),
            data = dict(type='dict', required=False),
            per_host = dict(type='bool', required=False),
        )
    )

    # set up dummy variables and context
    task_vars = dict()
    variable_manager = VariableManager()
    loader = TestDataLoader()
    play_context = PlayContext()
    play_context.network_os = 'ios'
    play_context.remote_addr = '1.1.1.1'
   

# Generated at 2022-06-13 10:48:28.891071
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # check for when task args is not empty
    fake_task = mock.Mock(args=dict(
        per_host=True, aggregate=False, data=dict(a='1', b='2')
    ))
    fake_task.add_md_to_facts = True
    fake_task.async_val = 2
    action_module = ActionModule(task=fake_task)
    tmp = None
    task_vars = dict()
    result = action_module.run(tmp, task_vars)
    assert result['changed'] == False
    assert result['ansible_stats'] == {
        'aggregate': False,
        'data': {'a': '1', 'b': '2'},
        'per_host': True
    }

    # check for when task args is empty
    fake_task

# Generated at 2022-06-13 10:48:32.348992
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(Task(), Connection(None), play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None).run(tmp=None, task_vars=None) is not None

# Generated at 2022-06-13 10:50:26.958985
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule.ActionModule(
        dict(foo='bar', action=dict(), task=dict(args=dict(data=dict(), aggregate=True, per_host=False), async_val=1, delegate_to='localhost')))
    task_vars = dict()

    # Test variables not set
    task_vars['action_result'] = dict(failed=False)
    task_vars['ansible_stats'] = dict(data=dict(), aggregate=True, per_host=False)
    task_vars['foo'] = dict(bar='none')

    # Test success by checking action_result
    assert(action.run(tmp=dict(), task_vars=task_vars) == dict(changed=False, ansible_stats=dict(data=dict(), aggregate=True, per_host=False)))

# Generated at 2022-06-13 10:50:30.667974
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Instantiate ActionModule
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None) is not None

# Generated at 2022-06-13 10:50:32.204066
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    this is a test for the constructor of the ActionModule class
    '''
    pass

# Generated at 2022-06-13 10:50:37.060240
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ldict = locals()
    args = {'data': {'a': 1, 'b': 2}, 'aggregate': False, 'per_host': True}
    ldict['self'] = ActionModule(ldict['module'], ldict['task'])
    task_vars = {}
    result = ldict['self'].run(tmp='/tmp', task_vars=task_vars)

# Generated at 2022-06-13 10:50:40.994099
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # construct an object of class ActionModule with arguments for its constructor
    #args = {"data": {'input_data': 1}, 'aggregate': True, 'per_host': False}
    #print(args)
    #actionmodule_object = ansible.plugins.action.ActionModule(None, args, None)
    #add_to_facts = actionmodule_object.run()
    #print(add_to_facts)
    return


# Generated at 2022-06-13 10:50:50.778573
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # NOTE: this is not a full unittest, just a quick smoke test to
    #       verify some basic functionality without requiring the
    #       full-blown unit test infrastructure.

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager

    play_context = PlayContext()
    task_queue_manager = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback=None,
    )


# Generated at 2022-06-13 10:50:54.788881
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert isinstance(action._VALID_ARGS, frozenset)
    assert 'aggregate' in action._VALID_ARGS
    assert 'data' in action._VALID_ARGS
    assert 'per_host' in action._VALID_ARGS


# Generated at 2022-06-13 10:51:00.821812
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    test run method of class ActionModule.
    """
    am = ActionModule()

    # test invalid case
    assert am.run({}, {})['msg'] == "The 'data' option needs to be a dictionary/hash"

    # test valid cases
    data = {'var1': '{{ "abcd" }}', 'var2': '{{ lookup("pipe", "echo 123")}}'}
    assert am.run({}, {}, {"data": data})['msg'] == 'OK'
    assert am.run({}, {}, {"data": data, "per_host": True})['msg'] == 'OK'
    assert am.run({}, {}, {"data": data, "aggregate": False, "per_host": False})['msg'] == 'OK'

# Generated at 2022-06-13 10:51:04.152889
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None,
                        shared_loader_obj=None)

# Generated at 2022-06-13 10:51:15.633242
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.plugins.action import ActionBase

    data_dict = {'data': {'my_name': 'my_value'}}
    data_dict_with_bad_data = {'data': 'my_data'}
    data_dict_with_bool_per_host = {'data': {'my_name': 'my_value'}, 'per_host': 'True'}
    data_dict_with_invalid_per_host = {'data': {'my_name': 'my_value'}, 'per_host': 'invalid'}
    data_dict_with_valid_per_host = {'data': {'my_name': 'my_value'}, 'per_host': 'True'}
    data_dict_with_bad_