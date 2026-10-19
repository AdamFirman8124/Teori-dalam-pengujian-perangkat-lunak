

# Generated at 2022-06-13 10:42:29.039289
# Unit test for method run of class ActionModule
def test_ActionModule_run():
        from ansible.playbook.play_context import PlayContext
        from ansible.executor.task_queue_manager import TaskQueueManager
        from ansible.plugins.strategy import ActionModule

        class MockTaskQueueManager(TaskQueueManager):
            def __init__(self):
                self.stats = dict()
                self.tqm_rc = 1

        class MockPlayContext(PlayContext):
            def __init__(self):
                self.check_mode = False
                self.remote_addr = None
                self.remote_user = None
                self.connection = None

        class MockTask(object):
            def __init__(self):
                self.args = dict(aggregate="yes", per_host="False", data=dict(total_task="1", success_task="0", failed_task="1"))


# Generated at 2022-06-13 10:42:31.990832
# Unit test for constructor of class ActionModule
def test_ActionModule():
   action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:42:43.750976
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    class FakeRunner(object):

        def __init__(self):
            self._tmp_path = None

        def get_basedir(self):
            return None

        def get_tmp_path(self):
            return self._tmp_path

        def set_tmp_path(self, tmp_path):
            self._tmp_path = tmp_path

    class FakeTask(object):

        def __init__(self):
            self._args = {}

        def get_args(self):
            return self._args

        def set_args(self, args):
            self._args = args

    class FakeTemplar(object):

        def __init__(self):
            self._resolve_vaild_identifiers = True


# Generated at 2022-06-13 10:42:44.803385
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("test_ActionModule")
    assert ActionModule(None, None) is not None

# Generated at 2022-06-13 10:42:48.014118
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )

    assert act is not None

# Generated at 2022-06-13 10:42:50.414131
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None)
    assert am.TRANSFERS_FILES == False
    assert type(am._VALID_ARGS) == frozenset

# Generated at 2022-06-13 10:42:51.334851
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # TODO: Add unit tests

    pass

# Generated at 2022-06-13 10:43:01.980040
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

# Generated at 2022-06-13 10:43:10.126132
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # set up task and action module
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    args = {'data': {'foo': 'bar', 'baz': 'bam' }, 'aggregate': True}
    action._task.args = args
    action._task.action = 'set_stats'

    # test run method
    result = action.run(None, None)
    assert result['ansible_stats']['data']['foo'] == 'bar'
    assert result['ansible_stats']['data']['baz'] == 'bam'
    assert result['ansible_stats']['aggregate'] == True

    # test run method with per_host

# Generated at 2022-06-13 10:43:15.166825
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(
        task=dict(action=dict(module_name='ping', module_args=dict()), args=dict(data=dict(), aggregate=True, per_host=False))
        , connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert actionmodule is not None

# Generated at 2022-06-13 10:43:23.207816
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am.TRANSFERS_FILES == False
    assert am._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:43:29.655702
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Set up test input
    tmp = None
    task_vars = None

    # Invoke method being tested
    action_module_obj = ActionModule(tmp, task_vars)
    output = action_module_obj.run(tmp, task_vars)

    # Check if method invocation succeeded
    assert output['failed'] is None

    # Check the output
    # Check if the output matches with expected output
    assert output == {'changed': False, 'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}}



# Generated at 2022-06-13 10:43:35.627207
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    module = 'set_stats'
    data = {'test': {'data': {'test': 'value'}}}
    expected_result = {'ansible_stats': {'data': {'test': 'value'}, 'per_host': False, 'aggregate': True}}
    assert am.run(data, module) == expected_result

# Generated at 2022-06-13 10:43:48.568113
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # load test json object for the unit test
    from ansible.utils.vars import combine_vars

    test_object = []
    with open('test_ActionModule.json', 'r') as f:
        for line in f:
            test_object.append(json.loads(line))

    # unit test for ActionModule.run
    for test_case in test_object:
        am = ActionModule()
        am.templar = Templar()
        setattr(am._task, 'args', test_case['args'])
        if 'task_vars' in test_case:
            task_vars = combine_vars(test_case['task_vars'], None)
        else:
            task_vars = None
        am.run(task_vars=task_vars)


# Generated at 2022-06-13 10:43:53.504956
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test function run of class ActionModule
    fake_templar = FakeTemplar()
    fake_templar.template_result = "my_stats"

    fake_module = FakeModule()

    test_data = {
        'test_data': {
            'test_data': {
                'test_data': {
                    'test_data': {
                        'test_data': {'var_name1': 'var_value1', 'var_name2': 'var_value2'}}}}}
    }

    fake_action = ActionModule(fake_module, task_vars={}, templar=fake_templar, shared_loader_obj=None)
    fake_action._task.args = test_data

    result = fake_action.run(tmp=None, task_vars=None)

    assert result

# Generated at 2022-06-13 10:43:57.814918
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    data = {'data': {'a': 5}, 'aggregate': True, 'per_host': False}
    action_module._task.args = data
    assert action_module.run()['ansible_stats'] == data

# Generated at 2022-06-13 10:44:10.223848
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:44:13.427353
# Unit test for constructor of class ActionModule
def test_ActionModule():
  am = ActionModule()
  assert am.TRANSFERS_FILES == False
  assert am._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Unit Tests for run()
from ansible.module_utils.six import PY3
from ansible.template import Templar


# Generated at 2022-06-13 10:44:19.528302
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = {}
    am = ActionModule(task=None, connection=None, _play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am.TRANSFERS_FILES == False
    assert am._VALID_ARGS == frozenset({'aggregate', 'data', 'per_host'})
    assert am.run(tmp=None, task_vars=None) == result

# Generated at 2022-06-13 10:44:28.227445
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    '''
    This test checks if method run of class ActionModule works OK.
    '''

    class FakeTemplar(object):  # Create a fake Templar
        def template(self, var, convert_bare=False, fail_on_undefined=True):
            return '_' + var  # add an underscore to the var

    class FakeTask(object):  # Create a fake Task
        def __init__(self):
            self.args = {'data' : 'my_data'}  # Set data in the task args

    class FakeTaskVars(object):
        pass

    templar = FakeTemplar()
    task = FakeTask()
    task_vars = FakeTaskVars()

# Generated at 2022-06-13 10:44:40.036977
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict()).run(None, dict()) == dict(changed=False, ansible_stats=dict(data=dict(), per_host=False, aggregate=True))


# Generated at 2022-06-13 10:44:53.861957
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mocks
    m_set_stats_run = Mock(side_effect={'msg': 'test_msg'})

    m_set_stats_get_type_for_value = Mock(side_effect={"test": "Success"})

    # m_set_stats_copy = Mock()
    # m_set_stats_run_safe = Mock()

    m_set_stats_get_option_boolean = Mock(side_effect={"test": True})

    # Mocks for class ActionBase
    m_acttion_base_run = Mock(return_value={"test": "Success"})
    m_acttion_base_get_type_for_value = Mock(side_effect={'test': "String"})

# Generated at 2022-06-13 10:44:59.700278
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(action=dict(module_name="set_stats", module_args=dict(data=dict(foo="8", bar="9"), aggregate=True))),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        share_loader_obj=False
    )
    assert action_module._task.action['module_name'] == "set_stats"
    assert action_module._task.action['module_args'] == dict(data=dict(foo="8", bar="9"), aggregate=True)
    assert action_module.TRANSFERS_FILES == False
    assert action_module._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:45:06.148366
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def check_action_module_class(cls, cls_name):
        assert isinstance(cls.TRANSFERS_FILES, bool)
        assert isinstance(cls._VALID_ARGS, frozenset)
        assert isinstance(cls._task.args, dict)
        assert isinstance(cls._templar, string_types)

    check_action_module_class(ActionModule, "ActionModule")

# Generated at 2022-06-13 10:45:08.301190
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)'''

    # TODO: Add tests

# Generated at 2022-06-13 10:45:09.137152
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(ActionBase, 'dummy-task')

# Generated at 2022-06-13 10:45:12.708021
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = object()
    task.args = {'data': {'a': 10}}
    task_vars = dict()
    action = ActionModule(task, task_vars)
    result = action.run()
    assert result.get('ansible_stats') == {'data': {'a': 10}, 'per_host': False, 'aggregate': True}

# Generated at 2022-06-13 10:45:23.128662
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # minimal args to init ActionModule
    action_module = ActionModule(None, None)
    # Run method should return the stats structure
    # so we can test for that.
    result = action_module.run(None, None)
    # test for a successful run
    assert result.get('ansible_stats') is not None
    # test for a failed run with a 'data' variable
    # that does not return a dict
    action_module = ActionModule(dict(data='blah'), None)
    result = action_module.run(None, None)
    assert 'failed' in result
    # test with a valid 'per_host' value
    action_module = ActionModule(dict(per_host='blah'), None)
    result = action_module.run(None, None)

# Generated at 2022-06-13 10:45:28.838042
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isidentifier("_abc")
    assert isidentifier("abc")
    assert isidentifier("abc123")
    assert not isidentifier("123abc")
    assert not isidentifier("123")
    assert not isidentifier("")
    assert not isidentifier("!")
    assert not isidentifier("a!")

# Generated at 2022-06-13 10:45:39.000545
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test for constructor of class ActionModule

    @id - unittest-lib-inventory-plugins-action_plugins-ActionModule-test_ActionModule

    @assert - object of class ActionModule is initialized.
    """
    # Create object of class ActionModule
    action_module = ActionModule(action_base=None)
    action_module.action_base = None
    action_module._task = None
    action_module._shared_loader_obj = None
    action_module._connection = None
    action_module._play_context = None
    action_module._loader = None
    action_module._templar = None
    action_module._task_vars = None
    action_module.transfers = None
    action_module.noop_vars = None

# Generated at 2022-06-13 10:45:58.004562
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:45:58.922590
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(ActionBase(), dict())

# Generated at 2022-06-13 10:46:04.045634
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test for ansible_stats module"""
    task_args = dict(data=dict(a=1, b=2))
    task_vars = dict()
    tmp = None
    fake_module = ActionModule(tmp, task_vars)

    assert fake_module.run(tmp, task_vars)['ansible_stats'] == dict(data=dict(a=1, b=2), aggregate=True, per_host=False)

# Generated at 2022-06-13 10:46:12.954679
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule()
    assert hasattr(x, 'set_attributes')
    assert hasattr(x, 'setup')
    assert hasattr(x, 'run')
    assert hasattr(x, '_convert_bool')
    assert hasattr(x, '_convert_to_integer')
    assert hasattr(x, '_convert_to_float')
    assert hasattr(x, '_convert_to_date')
    assert hasattr(x, '_convert_to_none')
    assert hasattr(x, '_supports_check_mode')
    assert hasattr(x, '_supports_async')
    assert hasattr(x, '_supports_become')
    assert hasattr(x, '_no_log')

# Generated at 2022-06-13 10:46:20.174589
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    _play_context = PlayContext()
    import ansible.constants as C
    import ansible.executor.task_result as task_result
    import ansible.executor.stats as stats
    task_result._stats = stats.AggregateStats()
    _task_result = task_result.TaskResult()
    import ansible.plugins.loader as plugin_loader
    _loader = plugin_loader.ActionModuleLoader()
    _action = _loader.get('set_stats', {})
    _action._task = {}
    _action._task['args'] = {}
    _action._task.remote_user = C.DEFAULT_REMOTE_USER
    _action._task.args['data'] = {}
    _action._task.args['per_host'] = True

# Generated at 2022-06-13 10:46:28.176572
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    verify_run_method_works_with_right_params()
    verify_run_method_works_with_one_word_key()
    verify_run_method_works_with_string_value()
    verify_run_method_works_with_integer_value()
    verify_run_method_works_with_boolean_value()
    verify_run_method_works_with_list_value()
    verify_run_method_works_with_list_value_and_no_aggregation()
    verify_run_method_works_with_dict_value()
    verify_run_method_works_with_dict_value_and_no_aggregation()
# Test if method works with right params

# Generated at 2022-06-13 10:46:29.211229
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()


# Generated at 2022-06-13 10:46:35.756807
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # ###
    # Setup MagicMock instance and setup required mocks
    # ###
    am = ActionModule(
        action_plugin_mock,
        task_mock,
        connection_mock,
        ansible_consts_mock,
        loader_mock,
        cli_options_mock,
        display_mock
    )

    # ###
    # Test constructor of class ActionModule
    # ###
    assert(isinstance(am, ActionModule))



# Generated at 2022-06-13 10:46:46.274120
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup mock object for ActionModule object.
    action_module = ActionModule(runner=None, task=None)

    # Conveniently, the mock object for ActionModule object has the run
    # as a method.  We can use it to directly test the method.
    result = action_module.run(tmp=None, task_vars=None)

    # Let's assert that the run method returns a dict
    assert type(result) is dict
    assert set(result.keys()) == set(['msg', 'failed', 'ansible_stats', 'changed'])

    # The default values for aggregate, per_host, data and
    # changed are as we expect them to be.
    assert result['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}
    assert result['changed'] is False

# Generated at 2022-06-13 10:46:55.846928
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """This function is a simple unit test for the run method of the class ActionModule.
       It must be improved when other cases are coded.
    """
    my_vars = {'ansible_facts': {'os_family': 'Debian', 'distribution': 'Debian', 'distribution_version': '8.0'}}
    my_host = "localhost"
    my_module_args = {'data': {'os_variable': 'os_value', 'ajt_variable': 'ajt_value'}, 'per_host': True}
    my_module_name = "ajt_module"
    my_task_name = "ajt_task"
    my_play_context = None
    my_loader = None


# Generated at 2022-06-13 10:47:48.591698
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    data = {'api_user': '2.2.2.2',
            'api_password': 'cisco',
            'api_http_method': 'post',
            'api_timeout': '3',
            'host': '1.1.1.1',
            'port': '443',
            'use_proxy': True,
            'validate_certs': False,
            'use_ssl': True,
            'force': True,
            'state': 'absent',
            'vrf': 'mgmt'}

    v = mock.Mock()
    v.vars = {}
    v.to_text.return_value = True
    v.template.return_value = True


# Generated at 2022-06-13 10:47:50.284965
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModuleTest = ActionModule()
    assert isinstance(ActionModuleTest, dict) is True

# Generated at 2022-06-13 10:48:01.777280
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # We need valid_args to be a list
    # So, we convert it to a list to use in this test, and
    # we convert it back when we are done.
    valid_args = list(ActionModule._VALID_ARGS)
    ActionModule._VALID_ARGS = valid_args
    assert ActionModule._VALID_ARGS == frozenset(valid_args)

    valid_args.append('bad_arg')

    # This will fail because the _VALID_ARGS doesn't match what is in valid_args
    # It should not be 'bad_arg'
    assert ActionModule._VALID_ARGS == frozenset(valid_args)

    # Now, we set _VALID_ARGS to what is in valid_args
    ActionModule._VALID_ARGS = valid_args
    assert ActionModule._

# Generated at 2022-06-13 10:48:08.576965
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    sys.path.append('/home/tsaarni/ansible/lib/ansible')
    from ansible.module_utils.parsing.convert_bool import boolean
    class FakeTask(object):
        def __init__(self):
            self.args = {}
    class FakeModuleUtils(object):
        def __init__(self):
            self.insert = True
            self.template = template
        def template(self, data):
            return data
    class FakeModule(object):
        def __init__(self):
            self._shared_loader_obj = FakeModuleUtils()
            self._task_fields = FakeTask()
            self._task = FakeTask()
        def get_loader(self, **kwargs):
            return self._shared_loader_obj
    action = ActionModule()

# Generated at 2022-06-13 10:48:09.678446
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:48:11.956278
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Unit test implementation goes here
    assert False

# Generated at 2022-06-13 10:48:13.798226
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Method run of class ActionModule is tested in functional testing
    pass

# Generated at 2022-06-13 10:48:17.104963
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing ActionModule constructor")
    # For looks only
    action_module = ActionModule()
    assert(action_module.TRANSFERS_FILES is False)

# Generated at 2022-06-13 10:48:22.875671
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    result = {}
    stats = {"data": {}, "per_host": False, "aggregate": True}
    data = {"a": "b"}
    stats['data'] = data
    result['ansible_stats'] = stats
    result['changed'] = False
    assert result == module.run(task_vars={"ansible_play_hosts": ["localhost"]}, tmp=None)

# Generated at 2022-06-13 10:48:29.179326
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = {'data': {'a': 'b', 'c': 'd'}, 'aggregate': True, 'per_host': False}
    _task = dict()
    _task['args'] = module_args
    action = ActionModule(None, _task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action.run(tmp=None, task_vars=None)['ansible_stats'] == {'data': {'a': 'b', 'c': 'd'}, 'aggregate': True, 'per_host': False}



# Generated at 2022-06-13 10:50:16.740070
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:50:22.660506
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor has no parameters:
    obj = ActionModule()
    assert bool(obj)    # Unit test stub: "assert bool(self)" is redundant
    assert obj._task   # Unit test stub
    assert obj.TRANSFERS_FILES

    # Constructor has parameters:
    obj = ActionModule(task = {}, connection = {} , play_context = {}, loader = {}, templar = {}, shared_loader_obj = {})
    assert bool(obj)    # Unit test stub: "assert bool(self)" is redundant
    assert obj._task   # Unit test stub
    assert obj.TRANSFERS_FILES

# Generated at 2022-06-13 10:50:23.741027
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Write a unit test
    pass

# Generated at 2022-06-13 10:50:27.559145
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(None, None)

    assert mod._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
    assert mod.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:50:29.117835
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None


# Generated at 2022-06-13 10:50:29.698756
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass # TODO

# Generated at 2022-06-13 10:50:30.589483
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, dict())

# Generated at 2022-06-13 10:50:31.838338
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(runner=None)
    assert am.run is not None

# Generated at 2022-06-13 10:50:33.320660
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None
    assert type(action_module) is ActionModule

# Generated at 2022-06-13 10:50:41.788969
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a=ActionModule(task={'args': { 'per_host': False, 'aggregate': True, 'data': {'a': 'b', 'c': 'd'} }}, connection='local', play_context={}, loader=None, templar=None, shared_loader_obj=None)
    assert a.run(None,None) == {'changed': False, 'ansible_stats': {'data': {'a': 'b', 'c': 'd'}, 'per_host': False, 'aggregate': True}}