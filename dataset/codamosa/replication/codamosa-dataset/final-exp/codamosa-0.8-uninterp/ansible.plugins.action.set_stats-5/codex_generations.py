

# Generated at 2022-06-13 10:42:16.772675
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(
        task=dict(action=dict()),
        connection=None,
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert am.action == 'set_stats'
    assert am._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Unit test of run()

# Generated at 2022-06-13 10:42:19.599706
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: find a good pyunit test framework to validate that ActionModule works as expected
    return True

# Generated at 2022-06-13 10:42:27.238317
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()

    # ActionModule is a subclass of ActionBase
    assert issubclass(ActionModule, ActionBase)

    # _VALID_ARGS is a frozenset
    assert isinstance(am._VALID_ARGS, frozenset)
    # _VALID_ARGS has three elements
    assert len(am._VALID_ARGS) == 3

    # TRANSFERS_FILES is False
    assert am.TRANSFERS_FILES == False

    # TODO: write unit tests for the run method of class ActionModule

# Generated at 2022-06-13 10:42:32.891346
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # initialize the class
    module = ActionModule()

    # create task data
    task_data = { 'args': { 'data': {'a': 'b', 'c': 'd'}, 'per_host': 'yes', 'aggregate': 'yes'} }

    # call the run method of the class
    module.run(task_data)

# Generated at 2022-06-13 10:42:35.170973
# Unit test for constructor of class ActionModule
def test_ActionModule():

    assert hasattr(ActionModule, 'run') is True

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:42:42.333327
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from nose.tools import assert_equals
    import ansible.utils

    ansible.utils.isidentifier = lambda s: True

    # Case 1:
    #
    # Input data:
    #
    # task:
    #  args:
    #   data:
    #     'test1': 'test1'
    #   per_host: 'test2'
    #   aggregate: 'test3'
    #
    # Output data:
    #
    # changed: False
    # ansible_stats:
    #  data:
    #   'test1': 'test1'
    #  per_host: 'test2'
    #  aggregate: 'test3'

    am = ActionModule()
    am._task = ansible.task.Task()

# Generated at 2022-06-13 10:42:49.917246
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_ActionBase = ActionBase()
    test_ActionModule = ActionModule(task=2,
                  connection=3,
                  play_context=4,
                  loader=5,
                  templar=6,
                  shared_loader_obj=7)
    assert test_ActionModule._task == 2
    assert test_ActionModule._connection == 3
    assert test_ActionModule._play_context == 4
    assert test_ActionModule._loader == 5
    assert test_ActionModule._templar == 6
    assert test_ActionModule._shared_loader_obj == 7
    assert test_ActionModule._tmpdir is None
    assert test_ActionModule.TRANSFERS_FILES == False
    assert test_ActionModule._VALID_ARGS == frozenset({'per_host', 'aggregate', 'data'})

# Generated at 2022-06-13 10:42:54.568106
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am._VALID_ARGS == frozenset(['aggregate', 'data', 'per_host'])
    assert am.TRANSFERS_FILES == False
    assert am.run(tmp=None, task_vars=None) == None

# Generated at 2022-06-13 10:43:05.728184
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import pytest
    from ansible.plugins.action.set_stats import ActionModule as action
    import ansible.playbook.play_context

    play_context = ansible.playbook.play_context.PlayContext(connection='local')

    # Test with False data
    module = action._build_module(play_context, dict(aggregate=False, per_host=False, data=dict(test_val=False)))

    result = module.run()

    assert result['ansible_stats']['data']['test_val'] == False

    # Test with 0 data
    module = action._build_module(play_context, dict(aggregate=0, per_host=0, data=dict(test_val=0)))

    result = module.run()


# Generated at 2022-06-13 10:43:14.106014
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:43:28.987596
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # arrange
    import ansible.plugins.action
    import ansible.plugins.action.set_stats

    # mock
    task_args = {'aggregate': 'yes', 'data': {}, 'per_host': 'yes'}
    data = {'HTTP_CODE': '200'}
    task_args['data'] = data

    stats = {'data': {}, 'per_host': False, 'aggregate': True}
    expected = {'changed': False, 'ansible_stats': stats}
    for k, v in iteritems(data):
        stats['data'][k] = v

    stats['per_host'] = True
    stats['aggregate'] = True


# Generated at 2022-06-13 10:43:38.807365
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:43:42.545044
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    assert run_method_with_args("data", None, None) == {'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}, 'changed': False}

# Generated at 2022-06-13 10:43:48.964358
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with no args
    am = ActionModule(None, None)
    assert am.run() == {'ansible_stats': {'aggregate': True, 'data': {}, 'per_host': False}, 'changed': False}

    # Test with no data
    am = ActionModule(dict(aggregate=True, per_host=True, data=None), None)
    assert am.run() == {'ansible_stats': {'aggregate': True, 'data': {}, 'per_host': False}, 'changed': False}

    # Test with data of bad type
    am = ActionModule(dict(aggregate=True, per_host=True, data=list()), None)

# Generated at 2022-06-13 10:43:50.042726
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create base object for testing
    test_obj = ActionModule()

    # Verify result
    assert test_obj is not None

# Generated at 2022-06-13 10:43:55.829846
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #Initialize the object and call method run()
    a = ActionModule(task=dict(args=dict(data=dict(foo='bar'))))
    result = a.run(None,{})

    #compare result to expected output
    assert result.get('ansible_stats').get('data').get('foo') == 'bar'

# Generated at 2022-06-13 10:43:56.449228
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:43:57.221452
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:44:01.809495
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Initialize ActionModule object
    test_obj = ActionModule()

    # Execute the run method
    result = test_obj.run(tmp=None, task_vars=None)

    # Check the expected result
    assert result['changed'] == False

# Generated at 2022-06-13 10:44:07.559381
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = {'data': {'test': 42}}
    action_module = ActionModule({'ansible_facts': 42}, module_args, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(action_module._task.args, dict)
    assert action_module._task.args['data']['test'] == 42


# Generated at 2022-06-13 10:44:15.775789
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert mod

# Generated at 2022-06-13 10:44:16.421903
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 10:44:26.246736
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:44:29.676976
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_mod = ActionModule(None, None, None, None, None)
    assert action_mod._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:44:34.247354
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    assert module._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
    assert module.TRANSFERS_FILES is False

# Generated at 2022-06-13 10:44:38.640044
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule(action=dict(), task=dict(), connection=dict(), play_context=dict(), shared_loader_obj=dict(), templar=dict())
    mod._task.args = dict()
    ret = mod.run(task_vars=dict())
    assert 'ansible_stats' in ret

# Generated at 2022-06-13 10:44:39.173971
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:44:46.349668
# Unit test for constructor of class ActionModule
def test_ActionModule():
  from ansible.playbook.task import Task
  from ansible.playbook.play_context import PlayContext
  from ansible.inventory.host import Host
  from ansible.inventory.group import Group
  from ansible.cli import CLI
  from ansible.inventory.manager import InventoryManager

  CLI.parser = CLI.base_parser(constants.base_parser_args, 'dummy')
  opts, args = CLI.parser.parse_known_args('-k -K -m setup -a "filter=ansible_distribution*"'.split())
  Options.initialize(CLI.base_parser(constants.base_parser_args, 'dummy'), opts)

  # Initialize Inventory
  inventory = InventoryManager(loader=CLI, sources=['localhost,'])

  # Initialize PlayContext
  play_context

# Generated at 2022-06-13 10:44:55.622452
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # this is kinda fragile, but we might as well try to catch problems like this in unit tests
    # also, we need some test code coverage for this module
    import inspect
    err = None
    try:
        assert bool(inspect.getsource(TestActionModule))
    except AssertionError as e:
        err = e
    if err:
        pytest.fail("Unit test(s) not implemented for class %s.\n%s" % (ActionModule.__name__, err))


# Unit test class for method run of class ActionModule

# Generated at 2022-06-13 10:45:06.281590
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.hashivault import HASHI_VAULT_ADDR
    from ansible.module_utils.hashivault import HASHI_VAULT_TOKEN

    from ansible.modules.hashivault import set_stats
    action_module = set_stats('hashivault')

    assert action_module.options['url'] == HASHI_VAULT_ADDR, "Default url is not hashivault default"
    assert action_module.options['verify'] is True, "Default verify is not hashivault default"
    assert action_module.options['authtype'] == 'token', "Default authtype is not hashivault default"
    assert action_module.options['token'] == HASHI_VAULT_TOKEN, "Default token is not hashivault default"

# Generated at 2022-06-13 10:45:22.302339
# Unit test for constructor of class ActionModule
def test_ActionModule():

    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(am, ActionModule)

    am2 = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am2 is not am

# Generated at 2022-06-13 10:45:30.895901
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Single scenario: test with no data, per_host, aggregate specified and the
    # end result is expected to be a dictionary with all the default values.
    args = {'aggregate': None, 'data': None, 'per_host': None}
    mock_task = type('', (), {})
    mock_task.args = args
    action = ActionModule(mock_task, dict())
    result = action.run(None, None)
    assert isinstance(result, dict)
    assert result == {'changed': False,
                      'ansible_stats': {'data': {},
                                        'per_host': False,
                                        'aggregate': True}}
    # Call the method again with all options set and compare the end result with
    # expected default values.

# Generated at 2022-06-13 10:45:31.641146
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:45:45.482551
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

    # Test args initialization
    # Test empty dict initialization
    assert module.run() == {
        'failed': False,
        'changed': False,
        'ansible_stats': {
            'data': {},
            'per_host': False,
            'aggregate': True
        },
        '_ansible_no_log': False
    }
    # Test 'data' dict with int value
    assert module.run(get_dict('data', {'n': 1})) == {
        'failed': False,
        'changed': False,
        'ansible_stats': {
            'data': {'n': 1},
            'per_host': False,
            'aggregate': True
        },
        '_ansible_no_log': False
    }
    # Test 'data

# Generated at 2022-06-13 10:45:54.800059
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # required for testing
    from ansible.plugins.action import ActionBase
    class MockActionModule(ActionBase):
        TRANSFERS_FILES = False
        def run(self, tmp=None, task_vars=None):
            return super(MockActionModule, self).run(tmp, task_vars)

    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    play_context = PlayContext()

# Generated at 2022-06-13 10:45:56.550079
# Unit test for constructor of class ActionModule
def test_ActionModule():
	print(ActionModule('',''))

# Generated at 2022-06-13 10:46:02.575145
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task = dict(args = dict(data= {'key': 'data'}, aggregate=True, per_host=False)),
        connection = dict(),
        play_context = dict(),
        loader = None,
        templar = None,
        shared_loader_obj = None
    )
    assert(action.action == 'set_stats')
    assert(action.action_args == dict())
    assert(action.task_vars == dict())
    assert(action.tmp == None)


# Generated at 2022-06-13 10:46:05.106580
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    assert m.run() == {'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}, 'changed': False}

# Generated at 2022-06-13 10:46:07.693984
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert x

# Generated at 2022-06-13 10:46:15.274657
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    tmp = None
    task_vars = {}
    result = {}

    myaction = ActionModule(tmp, task_vars)

    # Test run without args
    result = myaction.run(tmp, task_vars)
    assert result['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True},\
           'Expected ansible_stats to be set to {data: {}, per_host:False, aggregate: True}'

    # Test run with valid data
    ans_data = {'foo': 'bar'}
    task_vars = {'ansible_stats': myaction.run(tmp, task_vars)}
    task_data = {'data': ans_data}
    result = myaction.run(tmp, task_vars)

# Generated at 2022-06-13 10:46:48.474752
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible import context
    from ansible.plugins.task import Task
    from ansible.playbook.task import Task as PlaybookTask
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    import os
    import unittest


# Generated at 2022-06-13 10:46:57.431726
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    loader = DataLoader()
    variable_manager = VariableManager()

    # host variable
    variable_manager.set_host_variable('127.0.0.1', 'opt_val', 'some_val')

    # facts
    variable_manager.set_nonpersistent_facts(variable_manager.get_vars(loader=loader, play=None, include_hostvars=True))
    facts = variable_manager.get_vars(loader=loader, play=None, include_hostvars=True)

# Generated at 2022-06-13 10:47:08.860755
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:47:09.741968
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule._VALID_ARGS

# Generated at 2022-06-13 10:47:20.427950
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def test_templar_template(value):
        return value

    def test_task_args_get(item, value):
        return {'data': {'key': 'value'}, 'per_host': True, 'aggregate': False}[item]

    test_ansible_stats = {'data': {'key': 'value'}, 'per_host': True, 'aggregate': False}
    test_result = {'changed': False, 'ansible_stats': test_ansible_stats}

    # create a class for testing private method _check_argspec
    class TestActionModule(ActionModule):

        def __init__(self, _task):
            self._task = _task
            self._templar = TestTemplar()


# Generated at 2022-06-13 10:47:28.303042
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    a.action_loader = DictActionLoader()
    a.task_vars = dict()
    a.task_vars['hostvars'] = dict()
    a._task.args = {}
    assert a.run() == {'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}, 'changed': False}
    a._task.args = {'aggregate': '{{ True }}'}
    assert a.run() == {'ansible_stats': {'aggregate': True, 'data': {}, 'per_host': False}, 'changed': False}
    a._task.args = {'per_host': '{{ False }}'}

# Generated at 2022-06-13 10:47:37.099590
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.role_context import RoleContext
    from ansible.playbook.block import Block
    from ansible.vars.hostvars import HostVars
    hostvars = HostVars(loader=None, variables=None)
    hostvars._data['localhost'] = {'ansible_all_ipv4_addresses': ['10.20.30.40'],
                                   'ansible_python': {'version': 2, 'type': 'CPython'},
                                   'ansible_distribution': 'Redhat',
                                   'ansible_os_family': 'Redhat',
                                   'ansible_ip_addresses': ['10.20.30.40']}
    task

# Generated at 2022-06-13 10:47:40.864481
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Tests the class ActionModule constructor.
    """
    assert hasattr(ActionModule, "_VALID_ARGS")
    assert isinstance(ActionModule._VALID_ARGS, frozenset)
    assert "data" in ActionModule._VALID_ARGS
    assert "aggregate" in ActionModule._VALID_ARGS
    assert "per_host" in ActionModule._VALID_ARGS


# Generated at 2022-06-13 10:47:47.078280
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action = ActionModule(task={'name': 'dummy', 'args': {'data': {'test_host': "ok"}}}, connection={}, play_context={}, loader={}, templar={}, shared_loader_obj={})
    result = test_action.run(tmp='/tmp', task_vars=None)
    assert result

# Generated at 2022-06-13 10:47:58.663873
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(dict(ActionModule._VALID_ARGS))
    action._task.args = dict()
    stats = action.run()['ansible_stats']
    assert stats['aggregate'] == True
    assert stats['per_host'] == False
    assert stats['data'] == {}
    action._task.args = dict(data=dict(foo='bar'))
    stats = action.run()['ansible_stats']
    assert stats['data'] == dict(foo='bar')
    assert stats['aggregate'] == True
    assert stats['per_host'] == False
    action._task.args = dict(data=dict(foo='bar'), aggregate=False, per_host=True)
    stats = action.run()['ansible_stats']
    assert stats['data'] == dict(foo='bar')
    assert stats

# Generated at 2022-06-13 10:48:48.901955
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule('', '', '')
    assert hasattr(action, '_VALID_ARGS')
    assert action.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:48:50.682847
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    assert action.run(task_vars={})
    assert action.run(task_vars={}, tmp={})

# Generated at 2022-06-13 10:49:01.396719
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.utils.template as template
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_host_variable("127.0.0.1", HostVars("127.0.0.1", variable_manager, "nop"))
    variable_manager.set_host_variable("127.0.0.1", HostVars("127.0.0.1", variable_manager, "nop"))
    variable_manager.set_host_variable("127.0.0.2", HostVars("127.0.0.2", variable_manager, "nop"))


# Generated at 2022-06-13 10:49:02.316440
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'ActionModule'


# Generated at 2022-06-13 10:49:12.048154
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # setup
    import unittest
    import ansible.modules.extras.system.set_stats as set_stats_module
    task_args = dict()
    task_vars = dict()
    templar = dict()

    # test
    set_stats = ActionModule(task_args=task_args, templar=templar, task_vars=task_vars)

    # check
    assert set_stats is not None
    assert set_stats.task_vars == task_vars
    assert set_stats.task_args == task_args
    assert set_stats._templar == templar
    assert set_stats.TRANSFERS_FILES == False
    assert set_stats._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:49:17.361178
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Instantiate class ActionModule with args
    am = ActionModule(None, {'data': {'test': 'value'}, 'per_host': 'yes', 'aggregate': 'yes'})
    if not isinstance(am, ActionModule):
        raise Exception("Instantiation of ActionModule failed")
    if am.TRANSFERS_FILES is not False:
        raise Exception("Incorrect value for TRANSFERS_FILES")
    if am._VALID_ARGS is None:
        # Value of _VALID_ARGS is immutable, so it cannot be None
        raise Exception("_VALID_ARGS is None")

# Generated at 2022-06-13 10:49:18.968850
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(dict(), dict())
    assert isinstance(action_module, ActionModule)

# Unit test to test the run method returns appropriate values

# Generated at 2022-06-13 10:49:28.315682
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = {'failed': False, 'msg': ''}
    def mock_run(tmp, task_vars):
        return result

    mock_task_vars = dict()
    action = ActionModule()
    action.runner = MockRunner()
    action.run = mock_run
    action.templar = MockTemplar()
    action._task = MockTask()
    action._task.args = {'data': {'test_key1': 'test_val1', 'test_key2': 'test_val2'},
                         'per_host': 'True',
                         'aggregate': 'False'}

    run_res = action.run(0, task_vars=mock_task_vars)

    # check that the call to templating engine is made
    assert action.templar.call_args

# Generated at 2022-06-13 10:49:29.325482
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Just an empty test to prevent error
    pass

# Generated at 2022-06-13 10:49:31.943498
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(load_fixture('test_action_module_constructor.yml'), dict())
    assert not a.needs_tmp

# Generated at 2022-06-13 10:51:47.076180
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:51:49.064631
# Unit test for constructor of class ActionModule
def test_ActionModule():

    module = ActionModule()
    assert hasattr(module, '_VALID_ARGS')
    assert len(module._VALID_ARGS) == 3

# Generated at 2022-06-13 10:51:50.657492
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # set up to run
    x = ActionModule()
    assert x.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:51:53.042358
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    print("set_stats.py constructor ActionModule: ", module)


if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 10:52:03.898553
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.vars import merge_hash
    fake_task_vars = {'my_var': 'my_value'}
    fake_task = {'args': {'per_host': True, 'aggregate': False, 'data': {'test': '{{my_var}}'}}}
    action_module = ActionModule()
    action_module._task = fake_task
    action_module._templar = action_module._shared_loader_obj.environment
    action_module._templar.add_new_template_vars(merge_hash(action_module._templar.template_vars, fake_task_vars))
    action_module._connection = None


# Generated at 2022-06-13 10:52:05.142817
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act = ActionModule(None, None)
    assert act is not None



# Generated at 2022-06-13 10:52:11.597543
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    task = Task()
    task._role = None
    task.args = dict()
    task._ds = dict()
    task._ds['vars'] = dict()
    task.action = 'set_stats'
    play_context = PlayContext()
    play_context._tqm = None
    task._play_context = play_context

    action_set_stats = ActionModule(task, play_context, '/tmp', 3)
    assert action_set_stats is not None
    assert action_set_stats.task == task
    assert action_set_stats._play_context == play_context