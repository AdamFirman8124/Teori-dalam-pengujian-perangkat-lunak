

# Generated at 2022-06-13 10:42:17.323614
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule('test')
    assert module._task.action == 'test'

# Generated at 2022-06-13 10:42:22.341545
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.common._collections_compat import Mapping
    dict_object = dict()
    result = ActionModule.run(tmp=None, task_vars=dict_object)
    assert isinstance(result, Mapping)


# Generated at 2022-06-13 10:42:23.761525
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    result = action_module
    assert result == action_module

# Generated at 2022-06-13 10:42:30.063938
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import Include
    from ansible.executor.task_result import TaskResult

    # Create a task, with a variable amount of arguments, to check if
    # the correct exception is raised for an invalid amount of arguments
    for args in (dict(), dict(a=1, b=2)), dict(args=dict(a=1, b=2)):
        task = Task()
        if args:
            task._load_data(args)

        try:
            action = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
            raise AssertionError('ActionModule constructor has not raised an exception for the given arguments')
        except TypeError:
            pass

    task

# Generated at 2022-06-13 10:42:42.437103
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create fake task with task_vars (needed to use test_loader from UnitTestCase)
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()
    task = Task()
    task_vars = variable_manager.get_vars(play_context)
    task_vars['name'] = 'test_host'
    # Create object and test if the required attributes are set
    am = ActionModule(task, loader, play_context, variable_manager=variable_manager, task_vars=task_vars)
    assert am._task == task

# Generated at 2022-06-13 10:42:43.445146
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'data' in ActionModule._VALID_ARGS

# Generated at 2022-06-13 10:42:51.303781
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' unit testing for method run of class ActionModule '''

    template_dict = dict(aggregate=False, data=dict(my_var='hello'), per_host=True)

    results = dict(ansible_stats=None)

    # TODO: Mock of class ActionModule
    #mock_class = Mock(spec=ActionModule)
    #mock_class.run.return_value = results
    #mock_class.run.assert_called_with(template_dict)

    test_class = ActionModule()
    test_class.run(template_dict)

# unit testing for function isidentifier of class ActionModule

# Generated at 2022-06-13 10:42:53.820847
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert len(ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None).run()) == 3

# Generated at 2022-06-13 10:43:04.500699
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule({
        'name': 'test_ActionModule',
        'args': {
            'data': {'foo': 'bar'},
            'per_host': True,
            'aggregate': True
        }
    })

    result = action.run()

    assert result['changed'] == False, "Change should be False"
    assert result['ansible_stats']['data']['foo'] == 'bar', 'Data should be what we set it to'
    assert isinstance(result['ansible_stats']['data'], dict)
    assert result['ansible_stats']['per_host'] == True, 'Per host should be true'
    assert result['ansible_stats']['aggregate'] == True, 'Aggregate should be true'

    # test that per_host can be set to a string

# Generated at 2022-06-13 10:43:13.445115
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionBase()
    assert(a.action_loader)
    assert(a.action_loader.public_action_plugins)
    assert(a.action_loader.all_action_plugins)
    assert(a.action_loader.action_paths)
    assert(a.action_loader.action_paths)
    assert(a.connection)
    assert(a.connection_loader)
    assert(a.connection_loader.all_connection_plugins)
    assert(a.connection_loader.all_connection_plugins)
    assert(a.connection_loader.connection_paths)
    assert(a.connection_loader.connection_paths)
    assert(a.connection_loader.plugins)
    assert(a.become)
    assert(a.become_method)

# Generated at 2022-06-13 10:43:20.603190
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    assert am.run() == {'changed': False}

# Generated at 2022-06-13 10:43:23.552657
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a.TRANSFERS_FILES == False
    assert a._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))


# Generated at 2022-06-13 10:43:26.695256
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__bases__ == (ActionBase,)
    assert ActionModule._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
    assert ActionModule.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:43:27.243951
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:43:34.218181
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test with all default options
    result = ActionModule().run(task_vars={})

    assert isinstance(result, dict)
    assert 'changed' in result
    assert result['changed'] == False
    assert 'ansible_stats' in result
    assert isinstance(result['ansible_stats'], dict)
    assert 'data' in result['ansible_stats']
    assert isinstance(result['ansible_stats']['data'], dict)
    assert len(result['ansible_stats']['data']) == 0
    assert 'per_host' in result['ansible_stats']
    assert result['ansible_stats']['per_host'] == False
    assert 'aggregate' in result['ansible_stats']
    assert result['aggregate'] == True

    # test with dict option 'data'


# Generated at 2022-06-13 10:43:47.451864
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test 1 (success)
    action_base_instance = ActionBase()
    action_module_instance = ActionModule(action_base_instance._task, action_base_instance._connection, action_base_instance._play_context,
                                          action_base_instance._loader, action_base_instance._templar, action_base_instance._shared_loader_obj)
    assert action_module_instance._task == action_base_instance._task
    assert action_module_instance._connection == action_base_instance._connection
    assert action_module_instance._play_context == action_base_instance._play_context
    assert action_module_instance._loader == action_base_instance._loader
    assert action_module_instance._templar == action_base_instance._templar
    assert action_module_instance._shared_loader

# Generated at 2022-06-13 10:43:53.391138
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_base_instance = ActionBase()
    action_module = ActionModule(action_base_instance._task, action_base_instance._connection, action_base_instance._play_context, action_base_instance._loader, action_base_instance._templar, action_base_instance._shared_loader_obj)

    tmp = 'abc'
    task_vars = {}
    result = action_module.run(tmp, task_vars)
    assert result['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}

# Generated at 2022-06-13 10:43:59.039512
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(
        task=dict(
            args=dict(
               data=dict(foo=1)
            ),
        ),
    )
    assert a._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:44:03.588235
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_mod = ActionModule(load_fixture("test_set_stats_data.yaml"), dict())
    assert action_mod
    assert action_mod.run() == load_fixture("test_set_stats_output.json")

# Generated at 2022-06-13 10:44:09.056488
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert m._VALID_ARGS == frozenset(['aggregate', 'data', 'per_host'])
    assert m.TRANSFERS_FILES == False
    assert m.CACHEABLE_RESULTS == False

# Generated at 2022-06-13 10:44:20.437150
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule({}, {'constructor':'test_ActionModule'})
    assert am._task.args == {}

# Generated at 2022-06-13 10:44:28.924920
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

    action_module._generate_tmp_path = lambda x: '/tmp/' + x
    action_module._connection._shell.join_path = lambda x, y: '/tmp/' + x + '/' + y

    task = {
        'delegate_to': 'localhost',
        'args': {'data': {'some_var': 'some_value'}, 'per_host': True},
        '_ansible_no_log': False,
        'action': 'set_stats',
        'delegate_facts': False
    }
    task_vars = {}


# Generated at 2022-06-13 10:44:29.537052
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:44:40.579602
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule._templar = {}
    class FakeTaskModule:
        def __init__(self):
            self.args = {'data': {'a': '[1,2,3]', 'b': '{k:v}'}}
            self.environment = []
            self.action = None
            self.loop = None
            self.notified_by = None
            self.role_name = None
            self.task_vars = None

    fake_task = FakeTaskModule()
    fake_task.environment.append({'data': '{a:b}'})
    fake_task.environment.append({'data': {'a': 'b'}})


# Generated at 2022-06-13 10:44:42.388428
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:44:49.995825
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a test object from class ActionModule and set some module_utils arguments
    am = ActionModule(dict(ANSIBLE_MODULE_ARGS={}), fail_on_undefined=False, no_log=False)
    assert not am.fail_on_undefined
    assert not am.no_log
    assert not am.DEFAULT_AS_ROOT
    assert not am.TRANSFERS_FILES
    assert am._valid_args == ()

# Generated at 2022-06-13 10:44:55.909689
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # ActionModule.__init__()
    actionModule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Return the actual object's class name
    assert actionModule.__class__.__name__ == 'ActionModule'


# Generated at 2022-06-13 10:45:06.561587
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Test: Run")

    data = {'ansible_stats': {'data': {'x': 1, 'y': 2, 'z': 3}, 'per_host': False, 'aggregate': True}}
    assert data == ActionModule({}, {'_ansible_verbosity': 0}).run()
    data = {'ansible_stats': {'data': {'x': 1, 'y': 2, 'z': 3}, 'per_host': False, 'aggregate': True}, 'changed': False}
    assert data == ActionModule({'data': {'x': 1, 'y': 2, 'z': 3}}, {'_ansible_verbosity': 0}).run()

# Generated at 2022-06-13 10:45:16.443096
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.modules.system import set_stats
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook import Playbook
    from ansible.plugins.loader import find_action_plugin
    from ansible.plugins.loader import find_callback_plugin
    from ansible.executor.playbook_executor import PlaybookExecutor


# Generated at 2022-06-13 10:45:25.817367
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Unit test for constructor of class ActionModule'''
    task = dict()
    task['action'] = dict()
    task['action']['module_name'] = 'set_stats'
    task['action']['module_args'] = dict()

    task_copy = task.copy()
    set_stats_instance = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert set_stats_instance.task == task_copy
    assert set_stats_instance.connection is None
    assert set_stats_instance.play_context is None
    assert set_stats_instance.loader is None
    assert set_stats_instance.templar is None
    assert set_stats_instance.shared_loader_obj is None
    assert set_

# Generated at 2022-06-13 10:45:54.054121
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method ActionModule.run """

    _ActionBase = ActionBase()
    _ActionBase.runner = object()
    _ActionModule = ActionModule(
        task=dict(action=dict(module_name='set_stats', args=dict())),
        connection=_ActionBase.connection,
        play_context=_ActionBase.play_context,
        loader=_ActionBase.loader,
        templar=_ActionBase.loader.templar,
        shared_loader_obj=_ActionBase._shared_loader_obj)
    
    _ActionModule._connection = object()
    _ActionModule.connection = _ActionModule._connection
    _ActionModule.name = 'set_stats'
    _ActionModule.no_log = False
    _ActionModule._templar = _ActionBase.loader.templar



# Generated at 2022-06-13 10:46:03.450012
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Test for ActionModule.run ; returns True if test passes and False if it fails
    """
    # set ansible_stats values
    data = {'var1':'value1','var2':'value2'}
    aggregate = True
    per_host = False
    
    # create args from aggregate,per_host and data
    args = {'aggregate':aggregate,'per_host':per_host,'data':data}

    # create a task
    action_module = ActionModule()
    action_module._shared_loader_obj = None
    action_module._task = action_module.load_task_plugins(None, play=dict(name='myplay',playbook=None))
    action_module._task.args = args
    action_module._task.action = 'set_stats'

# Generated at 2022-06-13 10:46:12.390962
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Setup
    import sys
    if sys.version_info[0] < 3:
        from cStringIO import StringIO
    else:
        from io import StringIO
    module_args = {}
    tmp = ''
    task_vars = {}
    inject = {}

    from ansible.plugins.action.set_stats import ActionModule
    am = ActionModule(None, inject, task_vars=task_vars)

    am._task.args = module_args
    am._task.action = None
    am._connection = None


# Generated at 2022-06-13 10:46:14.572634
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule({}, {}, {}, [])
    assert isinstance(action_module, ActionModule)


# Unit tests for _VALID_ARGS property of class ActionModule

# Generated at 2022-06-13 10:46:21.388718
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Tmp:
        pass
    tmp = Tmp()
    tmp.args = dict(
        aggregate = True
    )

    class Tmp1:
        pass
    tmp1 = Tmp1()
    tmp1.args = dict(
        aggregate = None
    )

    class Tmp2:
        pass
    tmp2 = Tmp2()
    tmp2.args = dict(
        aggregate = '{{ lookup("file", "{{ lookupfile }}") }}'
    )

    class Tmp3:
        pass
    tmp3 = Tmp3()
    tmp3.args = dict(
        aggregate = '{{ lookup("file", "{{ lookupfile }}") }}'
    )
    class Tmp4:
        pass
    tmp4 = Tmp4()

# Generated at 2022-06-13 10:46:31.566527
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class Test:
        def __init__(self, _task):
            self._task = _task

        def run(self, *_):
            return self._task

    class Task:
        pass

    task = Task()
    task.args = {}
    action = ActionModule(Test(task))
    data = {'A': 'a', 'B': 'b'}
    task.args['data'] = data
    result = action.run(task)
    assert 'ansible_stats' in result
    ansible_stats = result['ansible_stats']
    assert ansible_stats == {'aggregate': True, 'per_host': False, 'data': data}
    data = ['A=a', 'B=b']
    task.args['data'] = data
    result = action.run(task)

# Generated at 2022-06-13 10:46:36.253671
# Unit test for constructor of class ActionModule
def test_ActionModule():
    self = dict()
    task = dict()
    task['args'] = dict()
    task['args']['data'] = "{{ var_with_underscore }}"
    task['args']['per_host'] = True
    task['args']['aggregate'] = False
    instance = ActionModule(self, task)
    instance.run(tmp='None', task_vars=None)

# Generated at 2022-06-13 10:46:47.090082
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert module.run()

    assert module.run(task_vars={'ansible_host': '1.1.1.1'})

    # For this test we need to mock the actual template call since it calls an ansible module
    module.templar.template = lambda x, y, z: x


# Generated at 2022-06-13 10:46:49.366110
# Unit test for constructor of class ActionModule
def test_ActionModule():
  assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:46:50.766556
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: add unit tests for method run of class ActionModule
    pass

# Generated at 2022-06-13 10:47:37.438377
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:47:50.877878
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    task_args = {'aggregate': False, 'data': {'var1': 'data1'}, 'per_host': False}
    task_vars = {}
    tmp = '/tmp'
    templar = object()

    action = ActionModule(task=dict(), connection=None, play_context=None, loader=None, templar=templar, shared_loader_obj=None)
    action._task.args = task_args
    action._templar = templar

    expected_dict = {'aggregate': False, 'per_host': False, 'data': {'var1': 'data1'}}
    assert action.run(tmp, task_vars)['ansible_stats'] == expected_dict

    # Negative case

# Generated at 2022-06-13 10:48:02.364672
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class Task(object):
        def __init__(self, args, vars):
            self.args = args
            self.vars = vars
    class TaskVars(object):
        args = {'per_host': True, 'aggregate': False, 'data': {'foo': 3}}
        vars = {'foo': 3, 'bar': 3}
    class TaskVars2(object):
        args = {'per_host': 'yes', 'aggregate': False, 'data': {'foo': '{{ bar }}'}}
        vars = {'foo': 3, 'bar': 3}
    class TaskVars3(object):
        args = {'per_host': 'yes', 'aggregate': False, 'data': {'foo': '{{ bar }}'}}

# Generated at 2022-06-13 10:48:13.219900
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_text
    from ansible.plugins.action.set_stats import ActionModule
    from ansible.template import Templar

    t = Templar(None, {})

    assert t is not None

    assert {} == ActionModule._validate_data({'data': "{}"}, t)
    assert {} == ActionModule._validate_data({'data': '{"foo": "bar"}'}, t)
    assert {} == ActionModule._validate_data({'data': {"foo": "bar"}}, t)
    assert {} == ActionModule._validate_data({'data': {"foo": "bar", "baz": "quux"}}, t)

    # test bools
    assert False == ActionModule._validate_data({'per_host': 'no'}, t)
    assert True == ActionModule

# Generated at 2022-06-13 10:48:21.051372
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    data = { "data":{"user":{"Evan":"Fay"}}}
    task_vars = dict(ansible_stats={})
    action = ActionModule()
    result = action.run(None,task_vars)
    assert result["ansible_stats"] == {'data': {}, 'per_host': False, 'aggregate': True}
    action = ActionModule(data,task_vars)
    result = action.run(None,task_vars)
    assert result["ansible_stats"] == {'aggregate': True, 'data': {'user': {'Evan': 'Fay'}}, 'per_host': False}
    data = { "data":{"user":{"Evan":"Fay"}},"aggregate":False}
    action = ActionModule(data,task_vars)
    result = action.run

# Generated at 2022-06-13 10:48:22.804236
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.set_stats
    ansible.plugins.action.set_stats.ActionModule

# Generated at 2022-06-13 10:48:32.305915
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

    ret_value = module.run(tmp=None, task_vars=None)
    assert ret_value['changed'] is False
    assert ret_value['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}

    ret_value = module.run(tmp=None, task_vars={'var1': 10, 'var2': 'this is var2', 'var3': 'var3 is a True'})
    assert ret_value['changed'] is False
    assert ret_value['ansible_stats'] == {'data': {u'var1': 10, u'var2': 'this is var2', u'var3': u'var3 is a True'}, 'per_host': True, 'aggregate': True}


# Generated at 2022-06-13 10:48:41.192591
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockTask(object):
        def __init__(self):
            self.args = {}
    class MockPlay(object):
        def __init__(self):
            self.hostvars = {'localhost': {'keya': 'valuea'}}
        def get_variable_manager(self):
            class MockVariableManager(object):
                def __init__(self):
                    self.hostvars = {'localhost': {'keya': 'valuea'}}
                def get_vars(self, loader, path, entities, cache=True):
                    return {'keya':'valuea'}
            return MockVariableManager()
    class MockPlayContext(object):
        def __init__(self):
            self.remote_addr = 'localhost'
            self.play = MockPlay()

# Generated at 2022-06-13 10:48:51.007097
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    AnsibleModule = AnsibleModule
    test_data = {'data': {'test_var': 1, 'another_var': 3}, 'per_host': False, 'aggregate': True}
    test_tmp = None
    test_task_vars = None
    action_module = ActionModule(None, None)
    action_module.task = AnsibleModule({})
    action_module._task.args = test_data
    action_module.run(test_tmp, test_task_vars)
    assert action_module.run(test_tmp, test_task_vars)['ansible_stats']['data'] == test_data['data']

# Generated at 2022-06-13 10:49:01.434291
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes

    mod = ActionModule()

    # test regular case
    task = {"args": {}}
    task["args"]["data"] = {"a": 1}
    task_vars = {"hostvars": {}}
    result = mod.run(task, task_vars)

    assert result["ansible_stats"]["data"] == {"a": 1}

    # test data outside of quotes
    task = {"args": {}}
    task["args"]["data"] = {'a': '{{ foo }}', 'b': '{{ bar }}'}
    task_vars = {"foo": 123, "bar": 456, "hostvars": {}}
    result = mod.run(task, task_vars)


# Generated at 2022-06-13 10:51:00.087742
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # unit test for method run() of class ActionModule
    # init ActionModule object
    actionModule = ActionModule(task=None, connection=None, templar=None, shared_loader_obj=None)
    actionModule._task.args = dict(data=dict(a=1, b=2), aggregate=True, per_host=False)
    actionModule._templar.bubble_data = dict(c=3, d=4)
    actionModule._templar.template = lambda x, convert_bare=False, fail_on_undefined=True: x
    result = actionModule.run()
    assert result['changed'] == False
    assert result['ansible_stats'] == dict(data=dict(a=1, b=2, c=3, d=4), per_host=False, aggregate=True)

# Generated at 2022-06-13 10:51:00.734747
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule)

# Generated at 2022-06-13 10:51:03.123124
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:51:14.918330
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    proto = {'module_name': 'set_stats', '_task': {'task_name': 'set_stats'}, '_templar': {'template': {}}, '_task_vars': {}}
    target = ActionModule(proto)

    test_args = {'data': {'key': 'val'}, 'per_host': 'True', 'aggregate': 'False'}
    expected_result = {'changed': False, 'ansible_stats': {'data': {'key': 'val'}, 'per_host': True, 'aggregate': False}}
    result = target.run(task_vars=proto['_task_vars'], tmp='tmp', inject=None, static_inject=None, task_vars=None, args=test_args)
    assert result == expected_result

   

# Generated at 2022-06-13 10:51:20.195503
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Setting up mock objects
    task_vars = dict()
    tmp = None
    result = dict(failed=False, changed=False, msg="", ansible_stats=dict())


# Generated at 2022-06-13 10:51:26.896599
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # tests ActionModule with no data dictionary
    actionModule = ActionModule()
    assert actionModule.run() == {'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}, 'changed': False}

    # tests ActionModule with no data dictionary
    actionModule = ActionModule()
    assert actionModule.run(task_vars = {'data': {'key': 'value'}}) == {'ansible_stats': {'data': {'key': 'value'}, 'per_host': False, 'aggregate': True}, 'changed': False}

    # tests ActionModule with aggregate option set to False
    actionModule = ActionModule()

# Generated at 2022-06-13 10:51:29.470549
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Initialize an object of ActionModule class
    obj = ActionModule()
    # validate action name
    assert obj.__class__.__name__ == 'ActionModule'
    # validate action option
    assert obj._valid_args == frozenset({'aggregate', 'data', 'per_host'})

# Generated at 2022-06-13 10:51:34.059210
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:51:44.910987
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    from ansible.plugins.action.set_stats import ActionModule
    import pytest

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    task = Task()
    task.action = 'set_stats'

# Generated at 2022-06-13 10:51:54.049747
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from collections import namedtuple
    from ansible.playbook import Play
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_queue_manager import TaskQueueManager

    Options = namedtuple('Options', ['connection', 'module_path', 'forks',
                           'become', 'become_method', 'become_user', 'check',
                           'listhosts', 'listtasks', 'listtags', 'syntax',
                           'sudo_user', 'sudo', 'diff'])