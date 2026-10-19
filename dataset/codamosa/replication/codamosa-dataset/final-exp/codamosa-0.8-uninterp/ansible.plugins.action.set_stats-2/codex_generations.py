

# Generated at 2022-06-13 10:42:15.436056
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None)

# Generated at 2022-06-13 10:42:18.723058
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(None)
    assert action.run()['ansible_stats']['data'] == {}
    assert action.run()['ansible_stats']['aggregate'] == True
    assert action.run()['ansible_stats']['per_host'] == False

# Generated at 2022-06-13 10:42:29.247914
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    check_filter = "The variable name '3w' is not valid. Variables must start with a letter or underscore character, and contain only letters, numbers and underscores."

    # No args declared for task
    task = dict(action=dict(module='set_stats', args=None))
    mock = {}

    # No args given for task
    ansible_run = ActionModule(task, mock)
    result = ansible_run.run()

    assert result['ansible_stats'] == dict(data={}, per_host=False, aggregate=True)

    # args given for task
    task_args = dict(data=dict(a="1", b="2"), aggregate="True", per_host="False")

# Generated at 2022-06-13 10:42:41.785101
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 10:42:49.616360
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test no args
    task = dict(action = dict(module = "set_stats", args = {}))
    am = ActionModule(task, dict())
    assert am.run(task_vars = dict())['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}

    testcases = {'data': {'foo': 1},
                 'per_host': True,
                 'aggregate': False}
    for (k, v) in iteritems(testcases):
        task = dict(action = dict(module = "set_stats", args = {k : v}))
        am = ActionModule(task, dict())

# Generated at 2022-06-13 10:42:52.652545
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

if __name__ == '__main__':
    import sys

    exit_code = pytest.main(sys.argv[1:])
    sys.exit(exit_code)

# Generated at 2022-06-13 10:42:53.163463
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:43:03.187225
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule."""
    #tests = {'_task': {'args': {'data': {'a': 1}, 'per_host': False, 'aggregate': True}}}
    tests = {'_task': {'args': {'data': {'a': 1}, 'per_host': 'false', 'aggregate': 'true'}}}

    for m_name in dir(ActionModule):
        if not m_name.startswith('_'):
            #print(m_name)
            m = getattr(ActionModule, m_name)
            if callable(m):
                tests[m_name] = m
    action = ActionModule(None, tests)
    print(action.run())


# Generated at 2022-06-13 10:43:11.196947
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    hostvars = {
        'localhost': {
            'success': True,
            'results': 'pass',
            'alive': True,
            'exception': '',
            'playbook_uuid': 'test-playbook',
            'omit': 'omit_me',
            'failed': False,
            'changed': True,
            'skipped': False,
        },
        'other_host': {
            'success': False,
            'results': 'fail',
            'alive': True,
            'exception': '',
            'playbook_uuid': 'test-playbook',
            'omit': 'omit_me',
            'failed': True,
            'changed': False,
            'skipped': False,
        },
    }

# Generated at 2022-06-13 10:43:20.375982
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def unit_test(controller):
        input_args = controller.input_args
        task_vars = controller.task_vars

        # set up the module args
        data_args = {
            'aggregate': controller.bool_var,
            'data': controller.data_var,
            'per_host': controller.bool_var,
        }
        # put it into the input args for the module
        for (k, v) in iteritems(input_args):
            input_args[k]['args'] = v

        # set up the module class
        module_instance = ActionModule(task_vars=task_vars)

        # run the code to be tested
        res = module_instance.run(task_vars=task_vars, **input_args)

        # make the asserts

# Generated at 2022-06-13 10:43:27.661113
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None, None)
    assert am.stats == {'data': {}, 'per_host': False, 'aggregate': True}

# Generated at 2022-06-13 10:43:30.212169
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Unit tests for run function of class ActionModule
# Test 1: Positive - data option is a dictionary

# Generated at 2022-06-13 10:43:31.876552
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing ActionModule class constructor")
    x = ActionModule()

# Generated at 2022-06-13 10:43:40.855659
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''

    import sys

    # test stdout:
    # sys.stdout = open(os.devnull,"w")

    test_ActionModule = ActionModule(
        {
            'name': 'test_name',
            'module_name': 'test_module_name',
            'args': {'data': {'test_data_key1': 'test_data_value1'}}
        }
    )

    print()

    test_task_vars = {}

    test_result = test_ActionModule.run(
        tmp='test_tmp',
        task_vars=test_task_vars,
    )

    print()

    print(test_result)

    print()

    # test stdout:
    # sys.stdout.

# Generated at 2022-06-13 10:43:52.195727
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module_instance = ActionModule(
        task=dict(name='test_task', args={'data': {'test_stat': 'test_value'}}),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )

# Generated at 2022-06-13 10:44:05.262777
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    task_vars.update(dict(
        ansible_stats_per_host=True,
        ansible_stats_aggregate=False,
    ))

    action = ActionModule()
    action._task = object()
    action._task.args = dict()
    action._task.args.update(dict(
        per_host=True,
    ))

    action._templar = object()
    action._templar.template = lambda x: x

    result = action.run(None, task_vars)
    assert result == dict(
        changed=False,
        ansible_stats=dict(
            data=dict(),
            per_host=True,
            aggregate=False,
        ),
    )

# Generated at 2022-06-13 10:44:14.452970
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager.set_inventory(inventory)

    # invalid 'data'
    stats = {'data': 2, 'per_host': False, 'aggregate': True}
    task = Task(name='test',  action='set_stats', args=stats, play=None)
    action = ActionModule(task, variable_manager, loader)
    result = action.run(task_vars=None)
    assert result['failed'] == True

# Generated at 2022-06-13 10:44:15.043680
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True is True

# Generated at 2022-06-13 10:44:22.676648
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(
            # inject any arguments here
            args=dict(
                # data can be a JSON string, but it can also be a python dictionary
                data=dict(foo="bar"),
                per_host=True,
                aggregate=False
            ),
            _host=dict(),
            _play=dict()
        ),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    assert action_module

# Generated at 2022-06-13 10:44:27.289842
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Initializations
    module_name = 'set_stats'
    module_args = {'data': {'test': 'true'}}
    module = ActionModule(None, module_name, module_args)
    args = module._task.args
    for arg in module._VALID_ARGS:
        assert arg in args, "The valid argument '%s' is not in args '%s'" % (arg, args)

# Generated at 2022-06-13 10:44:43.570543
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.set_stats

    module = ansible.plugins.action.set_stats.ActionModule(None, dict(), False, None)

    assert isinstance(module, ansible.plugins.action.ActionBase)
    assert module._shared_loader_obj is None
    assert module._connection is None
    assert module._play_context is None
    assert module._task.action == 'set_stats'
    assert module._loader is None
    assert module._task._role is None
    assert module._task.args == dict()
    assert module._loaded_vars_files is False
    assert module._task.delegate_to is None
    assert module._templar._available_variables.keys().sort() == ['hostvars', 'omit'].sort()
    assert module._templar._fail_on_

# Generated at 2022-06-13 10:44:56.516748
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:45:03.972690
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    s = """
- name: test
  set_stats:
    data:
      test_var: {'1': 2, '3': 4}
    per_host: no
    aggregate: yes
"""
    m = ActionModule(s, load_func=None, templar=None)
    task_vars = dict()
    result = m.run(tmp=None, task_vars=task_vars)
    print(result)


if __name__ == "__main__":
    test_ActionModule_run()

# Generated at 2022-06-13 10:45:12.341669
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import doctest, sys
    from ansible.module_utils import basic, vars
    from ansible.module_utils.parsing.convert_bool import boolean

    failed, tested = doctest.testmod(basic, optionflags=doctest.NORMALIZE_WHITESPACE, report=False)
    failed2, tested2 = doctest.testmod(vars, optionflags=doctest.NORMALIZE_WHITESPACE, report=False)

    failed3, tested3 = doctest.testmod(boolean, optionflags=doctest.NORMALIZE_WHITESPACE, report=False)

    module_dir = os.path.dirname(sys.modules['ansible'].__file__)

    size = 0

# Generated at 2022-06-13 10:45:13.220924
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:45:20.983595
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'ActionModule' == ActionModule.__name__
    assert 'action' == ActionModule.type
    assert not ActionModule.BYPASS_HOST_LOOP
    assert ActionModule.VALID_ARGS == ActionModule._VALID_ARGS
    assert not ActionModule.SHORT_ARGS
    assert not ActionModule.HAS_PARENT
    assert not ActionModule.STAYS_ON_FAILURE

    a = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert a

# Generated at 2022-06-13 10:45:24.502064
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins
    m = ansible.plugins.action.ActionModule(None, dict(one=1, two=2, three='{{ three }}'), dict(three=3))
    assert m._templar._available_variables == dict(one=1, two=2, three=3)
    assert m._task.action == 'set_stats'
    assert m._task.args == dict(one=1, two=2, three='{{ three }}')
    return

# Generated at 2022-06-13 10:45:34.177776
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  from ansible.playbook.task import Task
  from ansible.vars import VariableManager
  from ansible.inventory.manager import InventoryManager
  from ansible.parsing.dataloader import DataLoader
  from ansible.utils.vars import load_extra_vars
  from ansible.utils.vars import load_options_vars
  options = {'per_host': {'data': {'var': 'value'}}, 'aggregate': False}
  variable_manager = VariableManager()
  loader = DataLoader()
  paths = '/home/alice/ansible'
  inventory = InventoryManager(loader=loader, sources=paths)
  variable_manager.set_inventory(inventory=inventory)
  variable_manager.extra_vars = load_extra_vars(loader=loader, options=options)

# Generated at 2022-06-13 10:45:46.594821
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.definition import RoleDefinition

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils import context_objects as co

    play_context = PlayContext()
    task = TaskInclude()
    block = Block()
    play_context._prompt = {}

    play_context.network_os = 'ios'
    play_context.remote_addr = '20.1.1.1'

    # setup args to initialise ActionModule

# Generated at 2022-06-13 10:45:53.682327
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(task_id="taskid",
                workdir="/tmp/something",
                remote_user="something",
                environment=dict())
    play_context = dict()
    loader = dict()
    tmp = dict()
    shared_loader_obj = dict()
    variable_manager = dict()

    am = ActionModule(task, play_context, loader, tmp, shared_loader_obj, variable_manager)

    assert am._VALID_ARGS == frozenset(['aggregate', 'data', 'per_host'])

    assert am.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:46:19.601004
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    msg = "The variable name '%s' is not valid. Variables must start with a letter or underscore character, and contain only letters, numbers and underscores."
    module_class = ActionModule('test', '', {}, False)
    module_class._task.args = {}
    res = module_class.run()
    assert 'ansible_stats' in res
    assert res['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}

    # first test per_host and aggregate

    # per_host
    # 01 -> True
    module_class._task.args = {'per_host': 'true'}
    res = module_class.run()
    assert 'ansible_stats' in res

# Generated at 2022-06-13 10:46:20.231096
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: write me
    pass

# Generated at 2022-06-13 10:46:29.438498
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_text

    from ansible.plugins.action.set_stats import ActionModule as set_stats_action_module

    play_context = PlayContext()

    set_stats = set_stats_action_module(play_context)

    play_context._templar = basic.AnsibleModule(argument_spec=dict(), supports_check_mode=False)

    # test if method run returns changed
    play_context._task.args = dict(data={u'var1': u'val2', u'var2': u'val2'})
    result = set_stats.run(task_vars=dict(), play_context=play_context)
    assert result

# Generated at 2022-06-13 10:46:34.413962
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=None)

    assert(module.run(task_vars=dict()) == {'changed': False, 'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}})

# Generated at 2022-06-13 10:46:35.305956
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    assert a.run()

# Generated at 2022-06-13 10:46:35.838688
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print(ActionModule())

# Generated at 2022-06-13 10:46:46.323519
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils._text import to_bytes
    import json

    for k in ('aggregate', 'data', 'per_host'):
        assert hasattr(ActionModule, '_VALID_ARGS')
        assert k in ActionModule._VALID_ARGS

    args = {
        'data': {'key1': 'Value1', 'key2': 'Value2'},
        'per_host': True,
        'aggregate': False,
    }

    data = json.dumps(args)
    b_data = to_bytes(data)
    am = ActionModule(b_data, 'dummy', 'dummy', 'dummy', 'dummy')

    result = am.run(None, None)

    assert result['ansible_stats']

# Generated at 2022-06-13 10:46:48.792815
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action is not None
    assert action.__dict__ is not None

# Generated at 2022-06-13 10:46:50.138617
# Unit test for constructor of class ActionModule
def test_ActionModule():
    myaction = ActionModule()
    assert not myaction.TRANSFERS_FILES

# Generated at 2022-06-13 10:46:58.698777
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a plugin object and create a fake data to pass to its method run
    plugin = ActionModule('test', 'test', False, False, 'test', 'test.py')

    # create a fake task_vars data to pass to method run
    task_vars = {}

    # create fake arguments to pass to method run
    args = {'aggregate': True, 'data': {'ip_address': '192.168.123.123'}, 'per_host':False}

    # Call method run with fake data in arguments and task_vars
    result = plugin.run(task_vars=task_vars, tmp=None, **args)

    # Check if method run successfully completed
    assert result['failed'] == False
    assert result['changed'] == False

# Generated at 2022-06-13 10:47:41.165542
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test case where args is empty
    task_args = dict()
    assert(ActionModule._VALID_ARGS == ActionModule.run(task_args))

# Generated at 2022-06-13 10:47:52.188410
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule(loader=None,
                       action_base=ActionBase(),
                       task_vars=None,
                       connection=None,
                       play_context=None,
                       loader_cache=None,
                       templar=None,
                       shared_loader_obj=None)

    set_stats_args = dict(
        aggregate = True,
        data = dict(
            test1 = 1,
            test2 = '2'
        )
    )
    res = mod.run(tmp=None, task_vars=None)
    assert 'ansible_stats' in res
    stats = res['ansible_stats']
    assert stats['aggregate']
    assert 'data' in stats
    data = stats['data']
    assert 'test1' in data
    assert 'test2' in data

# Generated at 2022-06-13 10:48:03.319968
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # action module args
    data = {
        "test_count": 1,
        "test_boolean": False
    }
    args = {
        'aggregate': True,
        'data': data,
        'per_host': False
    }

    # simple task args
    mock_action = {
        'name': 'mock action name',
        'action': 'set_stats',
        'delegate_to': 'localhost',
        'args': args
    }

    mock_task = {
        'id': 'mock task id',
        'name': 'mock task name',
        'tags': [],
        'when': [],
        'action': 'mock action name',
        'args': args
    }

    # mock task vars
    task_vars = {}

    action_module

# Generated at 2022-06-13 10:48:13.694389
# Unit test for constructor of class ActionModule
def test_ActionModule():
  # Test 1:
  # Checks that constructor assigns values to variables as expected
  # Empty constructor
  test_action = ActionModule()
  assert test_action.runner_name == "local"
  assert test_action.action_name == "set_stats"
  assert test_action.noop_action == "meta"
  assert test_action.deprecated_action is None
  assert test_action.deprecated_conditional_action is None
  assert test_action.deprecated_conditional_action_msg is None
  assert test_action._supports_check_mode is True
  assert test_action._supports_async is False

  # Test 2:
  # Checks that _VALID_ARGS is valid

# Generated at 2022-06-13 10:48:17.392993
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Constructor test """
    m = ActionModule(None, None)
    assert m.TRANSFERS_FILES is False
    assert m._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:48:27.838572
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #TODO: it's necessary to mock _task and _shared_loader_obj
    action_module = ActionModule()
    action_module._task = None
    action_module._shared_loader_obj = None

    result = {'ansible_stats': {'aggregate': True, 'data': {}, 'per_host': False}}
    assert action_module.run() == result
    assert type(action_module.run()) == dict
    assert action_module.run()['msg'] == 'missing required arguments: data'
    assert action_module.run('/path/to/tmp') == result
    assert type(action_module.run('/path/to/tmp')) == dict
    assert action_module.run('/path/to/tmp')['msg'] == 'missing required arguments: data'
    assert action_module.run

# Generated at 2022-06-13 10:48:34.709403
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    t = Task()
    a = ActionModule(t, dict(per_host=True, aggregate=True))
    assert a.run(tmp='/tmp', task_vars=dict()) == {u'msg': u'Perform another task to set per_host/aggregate properties', u'ansible_stats': {'aggregate': True, u'data': {}, 'per_host': True}, u'changed': False}


# Generated at 2022-06-13 10:48:39.607454
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module._task.args.get('data', {}) == {}
    assert module._task.args.get('per_host', False) == False
    assert module._task.args.get('aggregate', True) == True


# Generated at 2022-06-13 10:48:41.119890
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert issubclass(m.__class__, ActionBase)

# Generated at 2022-06-13 10:48:42.811035
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(ActionBase())
    assert module is not None

# Generated at 2022-06-13 10:50:37.064748
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module.run(task_vars={"test_var": "test_value"})

# Generated at 2022-06-13 10:50:39.889415
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    mod.args = {'data': {'foo': '{{ baz }}'}, 'per_host': 'yes', 'aggregate': 'yes'}
    mod._task.args = mod.args
    mod.task_vars = {'baz': 'bar'}
    mod.run(task_vars=mod.task_vars)

# Generated at 2022-06-13 10:50:41.458567
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("hello")
    am_instance = ActionModule()
    print(am_instance.run())

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:50:55.852307
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task = dict(
            args = dict(
                aggregate = True,
                per_host = False,
                data = dict( key = 'value' ),
            ),
        ),
        connection = None,
        play_context = None,
        loader = None,
        templar = None,
        shared_loader_obj = None)

    assert module.run(None, None) == dict(failed=False, ansible_stats=dict(data=dict(key='value'), per_host=False, aggregate=True))

if __name__ == '__main__':
    import os
    import sys

    if len(sys.argv) > 2 and sys.argv[1] == 'test':
        if sys.argv[2] == 'test_ActionModule':
            test_ActionModule()

# Generated at 2022-06-13 10:50:57.732165
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    print('ActionModule class constructor')
    assert am.TRANSFERS_FILES == False
    assert am.VARS_DEFAULT_TEMPLATE == 'yaml'

# Generated at 2022-06-13 10:51:02.540229
# Unit test for constructor of class ActionModule
def test_ActionModule():
    file_name = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'ansible_stats.result'
    print("output file name: " + file_name)

    with open(file_name, 'w') as f:
        f.write('---\n')
        f.write('data:\n')
        f.write('  quotacheck: "0"\n')
        f.write('  quotatool: "0"\n')
        f.write('per_host: false\n')
        f.write('changed: false\n')
        f.write('aggregate: true\n')
        f.write('\n')

    from ansible.playbook.task import Task

    t = Task()

# Generated at 2022-06-13 10:51:14.240602
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ unit testing for module class file action.py """

    import unittest
    import ansible.plugins.action.set_stats
    from ansible.modules.system.ping import ActionModule as PingModule
    from ansible.plugins.loader import get_action_module

    class TestActionModule(unittest.TestCase):

        def setUp(self):
            self.action_module = ansible.plugins.action.set_stats.ActionModule(PingModule())

        def tearDown(self):
            pass

        def test_run_method(self):
            """ unit testing for run method """
            results = self.action_module.run(tmp=None, task_vars=None)

            self.assertEqual(results['ansible_stats']['data'], {})

# Generated at 2022-06-13 10:51:16.625698
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(None, None)

    assert(mod.TRANSFERS_FILES is False)
    assert(type(mod._VALID_ARGS) is frozenset)



# Generated at 2022-06-13 10:51:21.695538
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    t = Task()
    t._role = Role()
    t._block = Block()
    t.args = {'data': {'a':1}, 'aggregate': True, 'per_host': False}
    action = ActionModule(t, {}, False, '/path/to/ansible')
    assert action._task.args == t.args

# Generated at 2022-06-13 10:51:29.089251
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager


    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    # Create task with invalid data value
    task = Task()
    task.action = 'set_stats'
    task._role = Role()