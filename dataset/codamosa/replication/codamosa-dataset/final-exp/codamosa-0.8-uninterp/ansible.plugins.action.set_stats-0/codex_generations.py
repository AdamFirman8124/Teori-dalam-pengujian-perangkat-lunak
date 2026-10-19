

# Generated at 2022-06-13 10:42:14.195754
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:42:17.489399
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task=dict(
            args=dict(
                aggregate=True,
                per_host=True,
                data=dict(
                    test=True
                )
            )
        )
    )

    print(action._task)
    print(action._task.args)
    print(action._task.args.get('aggregate'))
    print(action._task.args.get('per_host'))
    print(action._task.args.get('data'))
    print(action._task.args.get('data').get('test'))

# Generated at 2022-06-13 10:42:19.608303
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule), "ActionModule constructor failed"


# Generated at 2022-06-13 10:42:24.184132
# Unit test for constructor of class ActionModule
def test_ActionModule():
    first_new_action = ActionModule(None, {})
    assert isinstance(first_new_action, ActionModule)

    second_new_action = ActionModule(None, {})
    assert isinstance(second_new_action, ActionModule)

    assert first_new_action is not second_new_action

# Generated at 2022-06-13 10:42:25.140877
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:42:32.622513
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
    action_module._task.args = {}

    tmp_action_module = action_module
    tmp_task_vars = None
    assert action_module.run(tmp_action_module, tmp_task_vars) == {'failed': False,
                                                                   'changed': False,
                                                                   'ansible_stats': {'data': {}, 
                                                                                     'per_host': False, 
                                                                                     'aggregate': True}}

    tmp_action_module = action_module
    tmp_task_vars = None

# Generated at 2022-06-13 10:42:36.781789
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_ = ActionModule()
    task_vars = {'a': {'b':{'c' : 1, 'd': [5,6,7]}}, 'e': "vijju"}
    action_.run(None, task_vars)

# Generated at 2022-06-13 10:42:37.824376
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert isinstance(m, ActionModule)


# Generated at 2022-06-13 10:42:41.323611
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None)

    assert (isinstance(action._VALID_ARGS, frozenset))
    assert (action._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host')))
    assert (action.TRANSFERS_FILES == False)

    assert (isinstance(action.run(None, None), dict))

# Generated at 2022-06-13 10:42:42.757135
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # call constructor of parent class
    assert ActionModule.__init__

# Generated at 2022-06-13 10:42:49.487284
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule, type)
    assert issubclass(ActionModule, ActionBase)

# Generated at 2022-06-13 10:42:56.927420
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    Unit tests are executed by pytest which is why this is in a method
    instead of inside an ActionModule class definition
    """
    import ansible.executor.task_result as task_result
    import ansible.constants as C
    import ansible.module_utils.parsing.convert_bool as convert_bool
    import ansible.plugins.action.set_stats as set_stats

    ansible.executor.module_common.connection_loader.persistent_connections = {}

    # input from user
    inp = dict(data={'a': 'b', 'c': 'd'})
    inp['per_host'] = 'yes'
    inp['aggregate'] = 'no'

    # set_stats as a module
    m = set_

# Generated at 2022-06-13 10:42:58.816352
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # check to see if ActionModule is initialized or not
    assert 'ActionModule' in globals()



# Generated at 2022-06-13 10:43:07.755364
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test results in dictionary
    template_dict = {'data': {'test_k': 'test_v', 'test_k2': 'test_v2'}, 'aggregate': False, 'per_host': True}
    # template
    template = """
- name: Gather test results
  gather_facts: no
  set_stats:
    %s
""" % template_dict
    # print(template)
    # Object ActionModule
    module = ActionModule()
    # set_variable method, input string
    ret = module.set_variable(template)
    # print(ret)
    # assert
    assert ret == template_dict

# Generated at 2022-06-13 10:43:08.976302
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert(module.TRANSFERS_FILES == False)

# Generated at 2022-06-13 10:43:10.681036
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None)
    assert action is not None

# Generated at 2022-06-13 10:43:19.943022
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    sys.path.append("t/lib")
    from unit_test_runner import AnsibleRunResult, PlayContext

    # setup mocks
    args = {'data': {'a': 1, 'b': '{{ c }}'}, 'per_host': False, 'aggregate': True}
    task = {
        'id': 12345,
        'args': args,
    }
    task_vars = {'c': 2}
    pc = PlayContext()

# Generated at 2022-06-13 10:43:21.624678
# Unit test for constructor of class ActionModule
def test_ActionModule():

    am = ActionModule(None, None, None, None, None, None, None, None)

    assert am is not None

# Generated at 2022-06-13 10:43:30.619569
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # pylint: disable=protected-access
    # from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult

    set_stats = dict(
        aggregate=True,
        data=dict(
            first=42,
            second=123,
            my_num=4,
            my_int=42,
            my_float=4.2,
            my_bool_true=True,
            my_bool_false=False,
        ),
        per_host=False,
    )


# Generated at 2022-06-13 10:43:36.405873
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # First test
    set_stats = {'data': {'foo': 'bar'}, 'per_host': False, 'aggregate': True}
    result = ActionModule.run(None, None)
    assert(result['changed'] == False)
    assert(result['ansible_stats'] == set_stats)

    #Second test
    set_stats = {'data': {'foo': 123}, 'per_host': False, 'aggregate': True}
    result = ActionModule.run(None, None)
    assert(result['changed'] == False)
    assert(result['ansible_stats'] == set_stats)

    #Third test
    result = ActionModule.run(None, None)
    assert(result['changed'] == False)
    assert(result['ansible_stats'] == set_stats)

    #Fourth test

# Generated at 2022-06-13 10:43:51.188088
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """This is a test method for ActionModule class constructor"""
    setattr(test_ActionModule, 'run', mock.Mock())
    action = ActionModule(task=mock.Mock(), connection=mock.Mock(), play_context=mock.Mock(), loader=mock.Mock(), templar=mock.Mock(), shared_loader_obj=mock.Mock())
    assert isinstance(action, ActionModule)
    assert hasattr(action, 'TRANSFERS_FILES')
    assert action.TRANSFERS_FILES == False
    assert hasattr(action, '_VALID_ARGS')
    assert isinstance(action._VALID_ARGS, frozenset)
    assert isinstance(action, ActionBase)



# Generated at 2022-06-13 10:44:02.807146
# Unit test for constructor of class ActionModule
def test_ActionModule():

    test_params = [{"aggregate":True, "per_host":True, "data": {"a":"b"}}]

    for test_param in test_params:
        action = ActionModule(dict(task_name="test-task"), task_vars=dict(ansible_facts=dict()), templar=dict(vars=dict()), module_vars=dict())
        actual = action.run(tmp=None, task_vars=None)
        assert actual['ansible_stats']['aggregate'] == test_param["aggregate"]
        assert actual['ansible_stats']['per_host'] == test_param["per_host"]
        assert actual['ansible_stats']['data']["a"] == test_param["data"]["a"]

    assert action.TRANSFERS_FILES

# Generated at 2022-06-13 10:44:05.523388
# Unit test for constructor of class ActionModule
def test_ActionModule():
    cls = ActionModule('testhostname')
    assert isinstance(cls, ActionBase)
    assert cls.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:44:14.610746
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    act = ActionModule()
    result = act.run(task_vars={"ansible_stats": {"data": {"var1":1, "var2": 2}}})
    assert result["ansible_stats"] == {"data": {"var1":1, "var2": 2}, "per_host": False, "aggregate": True}

    result = act.run(task_vars={})
    assert result["ansible_stats"] == {"data": {}, "per_host": False, "aggregate": True}


    result = act.run(task_vars={"ansible_stats": {"data": {"var1":1, "var2": 2}, "aggregate": False}})

# Generated at 2022-06-13 10:44:24.619067
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import ansible.utils.template as template
    import ansible.plugins

    class FakeTemplar(template.Templar):
        def __init__(self):
            pass
        def template(self, content, convert_bare=False, fail_on_undefined=True):
            return content

    class FakePlayContext(object):
        def __init__(self):
            self.remote_addr = "localhost"
            pass

    class FakeModule_run(object):
        def __init__(self):
            self._task = None
            self._templar = FakeTemplar()

    class TestActionModuleArgs(unittest.TestCase):

        def setUp(self):
            self.my_am = FakeModule_run()


# Generated at 2022-06-13 10:44:26.730614
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(action = None, task = None, connection = None,
                          play_context = None, loader = None, templar = None,
                          shared_loader_obj = None)
    assert action is not None


# Generated at 2022-06-13 10:44:35.806113
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # temporary environment variable 
    import os
    import tempfile
    import json
    p = tempfile.mkdtemp()
    os.environ['ANSIBLE_CONFIG'] = p + "/ansible.cfg"
    # temporary ansible.cfg file
    open(os.environ['ANSIBLE_CONFIG'], 'w').close()

    class Task():
        def __init__(self):
            self.args = {}

    class Play():
        def __init__(self):
            self.hosts = 'localhost'
            self.name = 'testPlay'

    class PlayContext():
        def __init__(self):
            self.play = Play()

    class ModuleUtil():
        def __init__(self):
            self.params = {'test': 1}


# Generated at 2022-06-13 10:44:44.003575
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test the case of valid variables
    set_stats = ActionModule()
    set_stats._task = {"args": {"data": {"var1": "Hi", "var2": "Hey"}}}
    set_stats._templar = None
    assert set_stats.run() == {'changed': False, 'ansible_stats': {'data': {'var1': 'Hi', 'var2': 'Hey'}, 'per_host': False, 'aggregate': True}}

    # Test the case of invalid variable
    set_stats = ActionModule()
    set_stats._task = {"args": {"data": {"111": "Hi", "var2": "Hey"}}}
    set_stats._templar = None

# Generated at 2022-06-13 10:44:46.030166
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None)
    action._task = None
    assert action.run(None, None) is None

# Generated at 2022-06-13 10:44:47.789548
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = module_runner()
    m.run()


# Generated at 2022-06-13 10:45:07.871525
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None,None)

# Generated at 2022-06-13 10:45:09.953234
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Tests if it is a class
    assert issubclass(ActionModule, ActionBase)

    # Tests if it is an instance of it class
    assert isinstance(ActionModule, ActionBase)

# Generated at 2022-06-13 10:45:14.308448
# Unit test for constructor of class ActionModule
def test_ActionModule():
  am = ActionModule(task={'args': {'aggregate': True, 'data': {}}}, connection={}, play_context={})
  assert am.run()['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}

# Generated at 2022-06-13 10:45:24.316828
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # pylint: disable=redefined-outer-name,unused-argument
    def create_task(task_args):
        def task():
            return None
        task.args = task_args
        return task
    def create_templar(template_result):
        class TemplateMock:
            def __init__(self, result):
                self.result = result
            def template(self, x, convert_bare, fail_on_undefined):
                return self.result
        return TemplateMock(template_result)

    test_task = create_task(dict(data=dict(foo=123), per_host=True, aggregate=False))
    test_module = ActionModule(None, test_task, None)
    test_module.set_loader(None)
    test_module._templar = create_tem

# Generated at 2022-06-13 10:45:31.934311
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # initialize necessary class method module
    test_module = ActionModule({})
    test_module._task = {
        'args': {
            'data': {
                'msg': False
            }
        }
    }
    # initialize necessary variables
    tmp = None
    task_vars = None
    # call method run of ActionModule class
    result = test_module.run(tmp, task_vars)
    # assert results
    assert result == {'ansible_stats': {'data': {'msg': False}, 'aggregate': True, 'per_host': False}, 'changed': False}



# Generated at 2022-06-13 10:45:35.584508
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    action = ActionModule(Task(), dict(foo="bar"))

    assert action._task.args['foo'] == 'bar'

# Generated at 2022-06-13 10:45:47.152497
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup mocks
    mock_actionBase = MagicMock()
    mock_task = MagicMock()
    mock_task_args = {
        'data': {
            'foo': 10,
            'bar': 20
        },
        'per_host': '{{ True }}',
        'aggregate': '{{ False }}'
    }

    mock_task.args = mock_task_args
    mock_result = {
        'changed': False,
        'ansible_stats': {
            'data': {
                'foo': 10,
                'bar': 20
            },
            'per_host': True,
            'aggregate': False
        }
    }

    mock_module = MagicMock()
    mock_module._templar = MagicMock()

# Generated at 2022-06-13 10:45:49.265855
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Verify that ActionModule is a subclass of ActionBase
    assert issubclass(ActionModule, ActionBase)

# Generated at 2022-06-13 10:45:59.445331
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader
    import ansible.playbook.task

    task_args = ImmutableDict(
        aggregate=False,
        data=dict(a=1, b=2),
        per_host=False,
    )

    loader = DataLoader()

    task = ansible.playbook.task.Task()
    task._role = None
    task.args = task_args
    task._ds = None
    task._loader = loader

    am = ActionModule(task, loader=loader, templar=None)
    assert 'aggregate' in am._VALID_ARGS
    assert 'data' in am._VALID_ARGS
    assert 'per_host' in am._VALID

# Generated at 2022-06-13 10:46:08.961892
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import MagicMock, patch

    class TestActionModule(unittest.TestCase):
        def setUp(self):
            self._task = MagicMock()
            self._task.action = 'set_stats'
            self._task.async_val = 42
            self._task.args = {}
            self._task.run_once = False
            self._task.notify = []
            self._task.tags = None
            self._task.when = []
            self._task.dep_chain = None

            self._loader = None
            self._connection = None
            self._play_context = None
            self._play = None
            self._loader = MagicMock()

# Generated at 2022-06-13 10:46:48.704013
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: implement this unit test
    module = ActionModule('/tmp', {})

# Generated at 2022-06-13 10:46:57.579911
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock a ActionModule object
    class MockActionModule(ActionModule):
        # Mock private method _execute_module of class ActionModule
        def _execute_module(self, m, p):
            return {"result": "test result string"}

    mock_self = MockActionModule()
    mock_self._task = {"args": {"data": {"key": "val", "key2": "val2"}}}
    mock_tmp = "test tmp"
    mock_task_vars = {"var": "val", "var2": "val2"}

    test_result = mock_self.run(mock_tmp, mock_task_vars)

    assert isinstance(test_result, dict)

# Generated at 2022-06-13 10:46:58.326542
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:47:09.515238
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import inspect
    import os
    import sys

    # get module path for action_plugins
    root_dir = inspect.getfile(inspect.currentframe())
    for i in range(3):
        root_dir = os.path.dirname(root_dir)
    # the following path is only valid for the test
    # I did not find other way to add the path for the test
    sys.path.append(root_dir + os.path.sep + 'action_plugins')
    sys.modules['nosetest'] = True
    sys.modules['__main__'] = True
    class TestActionModule():
        def __init__(self):
            self.__test_per_host_bool = False
            self.__test_aggregate_bool = False
            self.__test_data_dict = {}


# Generated at 2022-06-13 10:47:13.171688
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict(args=dict()), None).run(None, None) == {
        'changed': False,
        'ansible_stats': {'per_host': False, 'data': {}, 'aggregate': True}
    }

# Generated at 2022-06-13 10:47:23.143544
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(load_fixture("set_stats", "set_stats.py"))
    module.task_vars = dict()
    result = module._execute_module(task_vars=module.task_vars)
    assert result['failed'] == False
    assert result['changed'] == False
    result = module._execute_module(task_vars=module.task_vars, tmp='', task_action='set_stats')
    assert result['failed'] == False
    assert result['changed'] == False
    result = module._execute_module(task_vars=module.task_vars, tmp='', task_action='set_stats', args={'data': {'foo': 'bar'}})
    assert result['failed'] == False
    assert result['changed'] == False
    assert result['ansible_stats']

# Generated at 2022-06-13 10:47:27.838412
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test function, checks constructor of class ActionModule.
    """
    action_module = ActionModule()
    action_module.run()
    assert action_module._VALID_ARGS == {'aggregate', 'data', 'per_host'}

# Generated at 2022-06-13 10:47:36.976498
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock object for class AnsibleTask for class AnsibleActionModule
    class mock_class_for_AnsibleTask:
        # mock object for method args of class AnsibleTask for class AnsibleActionModule
        class mock_method_for_args:
            def get(self, key, value):
                if key == "data":
                    return value
                return {}

        # mock object for class AnsibleModule for class AnsibleActionModule
        class mock_class_for_AnsibleModule:
            def __init__(self):
                self.params = {}
            def fail_json(self, *args, **kwargs):
                raise Exception("fail_json")

        # mock object for method _load_params of class AnsibleModule for class AnsibleActionModule

# Generated at 2022-06-13 10:47:40.625635
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    run_result = {'changed': False,
                  'ansible_stats': {'data': {'a': 'b'}, 'per_host': False, 'aggregate': True}
                 }
    assert ActionModule().run(task_vars={'hostvars': {'host1': 'host1', 'host2': 'host2'}}, tmp='tmp') == run_result

# Generated at 2022-06-13 10:47:44.873312
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None)
    assert module.run(None, None) == {'changed': False, 'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}}



# Generated at 2022-06-13 10:49:13.663026
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actmod = ActionModule()
    assert actmod._task.args == {}
    assert actmod._task.action == 'set_stats'
    assert actmod._task.delegate_to == 'localhost'

# Generated at 2022-06-13 10:49:20.037761
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_module = ActionModule()
    task_vars = dict()
    result = dict()
    ansible_stats = dict()

    # Case 1: test with invalid variable name
    tmp = 'test_data'
    task_vars = dict()
    result = dict()
    result['changed'] = False
    ansible_stats = dict()

    task_vars['test_data'] = 'test'
    tmp = dict()
    tmp['data'] = '{{ test_data }}'
    tmp['per_host'] = 'yes'
    test_module._task.args = tmp
    result = test_module.run(tmp, task_vars)
    assert result['failed'] == True

# Generated at 2022-06-13 10:49:25.985815
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        myActionModule = ActionModule({"action": "set_stats"})
        print ("succeeded to create an instance of class ActionModule")
    except Exception as e:
        print ("failed to create an instance of class ActionModule", e)

    print ("displaying the contents of instance myActionModule of class ActionModule")
    print (myActionModule.__dict__)
    print ("finished displaying the contents of instance myActionModule of class ActionModule")


# Generated at 2022-06-13 10:49:31.450345
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    import mock
    import json

    module._task = mock.MagicMock()
    module._connection = mock.MagicMock()
    module._loader = mock.MagicMock()
    module._task_vars = mock.MagicMock()
    module._templar = mock.MagicMock()

    module._templar.template.return_value = {'test': 'success'}
    module.run()
    module._templar.template.assert_not_called()

    module._task.args = {'data': json.dumps({'test': 'success'})}
    module.run()

# Generated at 2022-06-13 10:49:38.475761
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    # instantiate the class
    action_module = ActionModule(
        task=Task(),
        connection=None,
        play_context=PlayContext(),
        loader=None,
        templar=Templar(),
        shared_loader_obj=None)

    # call the method run and pass two params 
    action_module.run(None, {"a": "b"})


# Generated at 2022-06-13 10:49:40.767037
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.set_stats import ActionModule
    # Test with no args passed
    am = ActionModule()
    assert am._VALID_ARGS is not None

# Generated at 2022-06-13 10:49:41.368906
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:49:43.049047
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: unit test for ActionModule.run
    pass


# Generated at 2022-06-13 10:49:52.031047
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import mock
    import json
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.dataloader import DataLoader

    name = 'test'
    action = {'__ansible_module__': 'test'}
    task = mock.MagicMock(TaskInclude)
    task.args = {'data': 'testing', 'per_host': False, 'aggregate': None}
    load = mock.MagicMock(DataLoader)
    templar = mock.MagicMock()
    templar.template.return_value = 'testing'
    am = ActionModule(task, load, templar, name, action)

    assert not am.run()['failed']
    am.run()['ansible_stats']
    templar.template.assert_any_call

# Generated at 2022-06-13 10:49:59.057966
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule('test_ActionModule_run', dict())
    mod._templar = 'test_templar'
    mod._task = 'test_task'
    mod._task.args = dict()
    mod._task.args['data'] = dict()
    mod._task.args['data']['test_key'] = 'test_value'
    assert mod.run() == dict(ansible_stats=dict(per_host=False, aggregate=True, data={'test_key': 'test_value'}), changed=False)

