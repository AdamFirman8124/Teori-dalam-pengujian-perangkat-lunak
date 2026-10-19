

# Generated at 2022-06-13 10:42:19.476005
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # this won't be required once we can pass in the task object via the runner
    # so it is only here for testing purposes for now

    t = dict(
        name='Add facts to host',
        args=dict(myvar='myvalue', other_var='foo'),
    )

    m = ActionModule(t, {})
    assert m, "ActionModule dictionary not created correctly"

    assert m._task.args['other_var'] == 'foo'
    assert m._task.args['myvar'] == 'myvalue'

    # Template the args
    m._templar = m._shared_loader_obj.templar

# Generated at 2022-06-13 10:42:25.920328
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.assert_test

    # Initialize arguments
    args = {}
    # Initialize task_vars
    task_vars = {}

    # Construct our object
    action = ansible.plugins.action.assert_test.ActionModule(None, None, task_vars, args)

    # We now run the class's test function
    ansible.plugins.action.assert_test.ActionModule.test(action)

    return None

# Generated at 2022-06-13 10:42:28.533286
# Unit test for constructor of class ActionModule
def test_ActionModule():
    myActionModule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert myActionModule.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:42:34.717868
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule('action', 'myhost', 
        {'Foo': 'bar'}, 
        {'foo': 'bar'}, 
        False, 
        'fake', 
        'fake', 
        'fake', 
        'fake', 
        'fake', 
        'fake', 
        'fake')

    assert module._connection.connection == 'local'

# Generated at 2022-06-13 10:42:37.824429
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action.name == 'set_fact'
    assert action.action_type == 'set_fact'

    assert action.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:42:45.426068
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test normal instantiation - no parameters
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action.name == 'setup'
    assert action.action_type == 'setup'

    # Test normal instantiation - with parameters
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action.name == 'setup'
    assert action.action_type == 'setup'

# Generated at 2022-06-13 10:42:51.000587
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Set up test data
    plugin_loader = ActionModule(
        task=dict(args=dict(action_key="action_value")),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    # Run test for constructor
    plugin_loader.run(None, None)

# Generated at 2022-06-13 10:43:01.576400
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:43:09.760373
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(action=dict(module='set_fact', args=dict(spam='eggs'))),
        connection=dict(host='localhost', port=22),
        play_context=dict(become=False, become_user=None, become_method=None),
        loader=dict(path=[]),
        templar=dict(),
        shared_loader_obj=dict()
    )

    assert module._task.args['spam'] == 'eggs'
    assert module._connection.host == 'localhost'
    assert module._connection.port == 22
    assert module._play_context.become is False
    assert module._play_context.become_user is None
    assert module._play_context.become_method is None
    assert module._loader.path == []

# Generated at 2022-06-13 10:43:16.537473
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  actionmodule = ActionModule()
  actionmodule._task = _Task()
  actionmodule._task.args = {}
  actionmodule._task.args['name'] = 'test-name'
  actionmodule._task.args['value'] = 'test-value'
  result = actionmodule.run(task_vars=None)
  assert result is not None
  assert result['ansible_facts']['name'] == 'test-name'
  assert result['ansible_facts']['value'] == 'test-value'


# Generated at 2022-06-13 10:43:21.365579
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:43:24.371529
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=None, templar=None, shared_loader_obj=None)
    result = module.run()
    assert result == dict()

# Generated at 2022-06-13 10:43:30.021067
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(load_config_file=False)
    assert isinstance(am, ActionModule)
    assert isinstance(am._task, dict)
    assert am._task == { 'args': {} }
    assert am.runner is None
    assert am.transport is None
    assert am._connection is None
    assert am._templar is None
    assert am._loader is None
    assert am._shared_loader_obj is None
    assert am._task_vars is None
    assert am._tmp is None

# Generated at 2022-06-13 10:43:37.962124
# Unit test for constructor of class ActionModule
def test_ActionModule():  
  fact = {'key1': 'value1', 'key2': 'value2'}
  task_vars = {}
  result = {'ansible_facts': None, '_ansible_facts_cacheable': False}
  setattr(ActionModule, '_task', {'args':fact})
  setattr(ActionModule, '_templar', {'template':lambda x:x})
  result = ActionModule().run(None, task_vars)
  assert result['ansible_facts'] == fact
  assert result['_ansible_facts_cacheable'] == False


# Generated at 2022-06-13 10:43:39.692375
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.constants as C
    action_module = ActionModule(None, None)

# Generated at 2022-06-13 10:43:47.083158
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module=ActionModule('testmodule','testpath',{'name': 'testactionmodule', 'args': {'key1': 'value1', 'key2': 'value2'}},load_needles=False)
    result=module.run(None,{})
    assert result['ansible_facts']['key1'] == 'value1'
    assert result['ansible_facts']['key2'] == 'value2'


# Generated at 2022-06-13 10:43:51.855669
# Unit test for constructor of class ActionModule
def test_ActionModule():
    t = dict(name='set_fact', args=dict(key_1='value1',key_2='value2'))
    am = ActionModule(t,None,None,None)
    assert am.run()['ansible_facts'] == {'key_1': 'value1', 'key_2': 'value2'}


# Generated at 2022-06-13 10:44:03.254457
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

    # Test when no arguments are provided
    try:
        module.run(tmp=None, task_vars=None)
    except AnsibleActionFail as e:
        assert e.__str__() == "No key/value pairs provided, at least one is required for this action to succeed"

    task_vars = dict()

    # Test when duplicate arguments are provided

# Generated at 2022-06-13 10:44:08.106568
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    task = Task()
    task._role = None
    task._block = None
    task._play = None

    # testing constructor without arguments
    am = ActionModule(task, task_vars={})

    # testing constructor with only one argument
    am = ActionModule(task)

# Generated at 2022-06-13 10:44:11.655912
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task = dict(action=dict(), args=dict()),
        connection = dict(),
        play_context = dict(),
        loader = None,
        templar = None,
        shared_loader_obj = None
    )
    assert action_module

# Generated at 2022-06-13 10:44:18.378789
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    return am

# Generated at 2022-06-13 10:44:22.216016
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test that the module can be initialized properly.
    :return:
    '''
    mod = ActionModule(task=None, connection=None, _play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert mod is not None

# Generated at 2022-06-13 10:44:25.105759
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None, None, None, None)
    assert action_module.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:44:30.982534
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = dict()

    # Test return no key/value pair
    args = dict()
    try:
        result = module.run(None, None, args)
    except AnsibleActionFail:
        assert True

    # Test return key/value pair
    args = dict(foo='bar')
    try:
        result = module.run(None, None, args)
    except AnsibleActionFail:
        assert False

    assert result['ansible_facts']['foo'] == 'bar'
    assert result['_ansible_facts_cacheable'] == False

# Generated at 2022-06-13 10:44:38.218667
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Check that when values are provided, but the form is wrong
    # that the constructor fails
    import os
    import q
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=os.path.dirname(q.system.fs.joinPaths(C.DEFAULT_LOCAL_TMP, 'ansible_test_inventory')))
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

# Generated at 2022-06-13 10:44:40.089367
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_object=None)
    assert am

# Generated at 2022-06-13 10:44:49.289200
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule('test', {'args': {'this is a string': 'not a list', 'list': ['this is a list']}})
    action._task.args['b_bool'] = True
    action._task.args['n_bool'] = False

    assert action.run() == {'changed': False, 'ansible_facts': {'this is a string': 'not a list', 'list': ['this is a list'], 'b_bool': True, 'n_bool': False}}

# Generated at 2022-06-13 10:44:57.223299
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = {'ansible_facts' : {}, '_ansible_facts_cacheable' : False}
    actionModule = ActionModule()
    actionModule._connection = {}
    actionModule._task = {}
    actionModule._task.args = { 'src': '/tmp', 'dest': '/usr/local' }
    resultExpected = {'ansible_facts': {}, '_ansible_facts_cacheable': False}
    resultReturned = actionModule.run()
    assert resultExpected == resultReturned

# Generated at 2022-06-13 10:45:06.772605
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_id = '1'
    action_name = 'file'
    args = {}
    task = {
        "action": action_name,
        "args": args,
    }
    task = TaskExecutor(task_id, task, "TASK", "", 0)
    task.task_vars = {"var1": "value1"}
    action_impl = ActionModule(task, "")
    assert isinstance(action_impl, ActionModule)
    assert isinstance(action_impl._task, TaskExecutor)
    assert action_impl._name == action_name
    assert action_impl._templar
    assert isinstance(action_impl._display, Display)

# Generated at 2022-06-13 10:45:16.805232
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  
    import unittest
    import unittest.mock as mock
    import sys

    if sys.version_info[0] >= 3:
        import _io

        class StringIO(_io.StringIO):

            def write_(self, msg):
                return super(StringIO, self).write(msg.decode('utf-8'))
    else:
        import StringIO

    class TestActionModule_run(unittest.TestCase):

        def setUp(self):
            super(TestActionModule_run, self).setUp()
            self.am = ActionModule()
            self.am._connection = mock.MagicMock()
            self.am._loader = mock.MagicMock()
            self.am._task = mock.MagicMock()
            self.am._templar = mock.MagicMock()


# Generated at 2022-06-13 10:45:34.733536
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import errors
    from ansible.playbook.task import Task
    from ansible.mock import Mock
    from ansible.mock import call

    class MyTask(Task):
        def __init__(self, args=None, module_name=None, module_args=None, loop=None, delegate_to=None, _ansible_delegated_vars=None):
            self._ansible_delegated_vars = _ansible_delegated_vars
            return

    module = Mock()
    task = MyTask(module_name='test', module_args='{ "key": "val" }')
    module.run.return_value = dict(ansible_facts=dict(a='b'))
    task.async_val = 0


# Generated at 2022-06-13 10:45:40.463531
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, None)
    assert isinstance(a._low_level_subprocess_args, list)
    assert 'virtualenv' in a._low_level_subprocess_args
    assert 'conditional' not in a._low_level_subprocess_args


# Generated at 2022-06-13 10:45:45.735545
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=dict(action=dict(module_name='set_fact')),
            connection=None, new_stdin=None)
    assert action._task.action.module_name == 'set_fact'
    assert action.connection is None
    assert action.new_stdin is None



# Generated at 2022-06-13 10:45:54.967786
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.process.worker import WorkerProcess
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    mock_loader = lambda: None
    mock_loader.get_basedir = lambda x: '/dev/null'
    mock_loader.path_exists = lambda x: True

    dag = DataLoader()
    dag.set_basedir('/dev/null')

    mock_queue_manager = lambda: None


# Generated at 2022-06-13 10:46:04.151489
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import tempfile

    class AnsibleModuleMock(object):
        def __init__(self, args):
            self.args = args
            self.params = args

        def fail_json(self, **kvargs):
            raise Exception(kvargs)

    class TaskMock(object):
        def __init__(self, args):
            self.args = args
            self.action = 'set_fact'

    class LoaderMock(object):
        def __init__(self):
            pass

        def get_basedir(self):
            return os.getcwd()

    class PlayContextMock(object):
        def __init__(self):
            pass

        def CLIConfiguration(self):
            return {}


# Generated at 2022-06-13 10:46:07.566568
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=dict(action=dict(cacheable=None), args=dict(foo='bar')))
    assert module.task.action['cacheable'] is False
    assert module.task.args['foo'] == 'bar'

# Generated at 2022-06-13 10:46:13.715344
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create a minimal ansible 'ActionModule' object
    am = ActionModule(None, {}, {})
    # define the a minimal valid kwargs
    am.task_vars = {'hostvars': {'samplehost': {}}}
    am.set_task_size_limit(100)
    am.set_task_weight_limit(100)
    # a None task_vars argument must raise an AnsibleActionFail
    try:
        am.run(None, None)
    except:
        # unit test succeed
        assert True
    else:
        # unit test failed
        assert False

# Generated at 2022-06-13 10:46:15.297131
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)
    assert ActionModule.__name__ == 'ActionModule'


# Generated at 2022-06-13 10:46:17.365203
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None) 
    
    # test method string of ActionModule
    assert action.string == 'Formatted Facts'

# Generated at 2022-06-13 10:46:18.637652
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None)
    assert am is not None



# Generated at 2022-06-13 10:46:36.977868
# Unit test for constructor of class ActionModule
def test_ActionModule():
    raise Exception("not implemented")

# Generated at 2022-06-13 10:46:39.599382
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None


# Generated at 2022-06-13 10:46:51.005495
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Construct an arbitrary task
    arbitrary_task = {
        'action': {
            '__ansible_arguments__': '',
            '__ansible_module__': 'set_fact',
            '__ansible_version__': '2.4',
            '__ansible_module_name__': 'set_fact',
            '__ansible_action__': 'set_fact',
            '__ansible_module_args__': '',
            '__ansible_action_name__': 'set_fact',
            '__ansible_action_aliases__': [],
            '__ansible_action_wrappers__': [],
            '__ansible_action_plugins__': [],
            '__ansible_action_extra_fields__': []
        }
    }

    # Construct an arbitrary task_v

# Generated at 2022-06-13 10:46:53.287332
# Unit test for constructor of class ActionModule
def test_ActionModule():
    fun = ActionModule(None, None)
    assert fun is not None
    assert isinstance(fun, ActionModule)
    assert fun.__class__.__name__ == 'ActionModule'

# Generated at 2022-06-13 10:47:00.631889
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import context

    context.CLIARGS = {}
    # test valid and invalid variable names


# Generated at 2022-06-13 10:47:09.585910
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    key = 'test_key'
    value = 'test_value'

    task_vars = dict()
    runner_args = {}
    runner_args['start_at_task'] = None

    runner = Runner(
        module_name = 'setup',
        module_args = dict(),
        module_paths = [],
        forks = 1,
        pattern = '*'
    )

    runner._push_action(
        ActionModule(runner, task_vars, runner_args, key=value)
    )

    result = runner.run()
    
    assert result['ansible_facts'][key] == value

# Generated at 2022-06-13 10:47:12.232082
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    am = ActionModule(loader=loader)
    assert am is not None

# Generated at 2022-06-13 10:47:18.957432
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class AcionModule
    '''
    import ansible.constants as C
    C.DEFAULT_JINJA2_NATIVE = False
    action_module = ActionModule()

    result = action_module.run(task_vars={})
    assert result['ansible_facts'] == {}
    assert result['changed'] == False
    assert result['_ansible_facts_cacheable'] == False

    result = action_module.run(task_vars={'foo': 'bar'})
    assert result['ansible_facts'] == {'foo': 'bar'}
    assert result['changed'] == False
    assert result['_ansible_facts_cacheable'] == False


# Generated at 2022-06-13 10:47:19.777703
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:47:33.559071
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_context import PlayContext
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.host import Host
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.persistent_fact_manager import PersistentFactManager
    from ansible.parsing.dataloader import DataLoader

    fake_loader = DataLoader()

# Generated at 2022-06-13 10:48:13.507113
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module

# Generated at 2022-06-13 10:48:14.771491
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, {}, {}, {})
    assert isinstance(a, ActionModule)

# Generated at 2022-06-13 10:48:25.142527
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create a mock config object
    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()
    display.verbosity = 3

    # create a mock object
    class ActionModule_run_mock(object):
        def __init__(self):
            self._task = {}
            self._task_vars = {}

    m = ActionModule_run_mock()
    m.TRANSFERS_FILES = False

    # test if ActionModule throws a fail when the arguments are not provided
    try:
        m.run(None, None)
    except AnsibleActionFail as e:
        assert "No key/value pairs provided" in e.args[0]

    # test if ActionModule runs successfully with arguments

# Generated at 2022-06-13 10:48:32.538444
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(
        argument_spec = dict(
            cacheable=dict(type='bool', default=False),
            a=dict(type='bool', required=False),
            b=dict(type='bool', default=False),
            c=dict(type='bool', default='true'),
            d=dict(type='bool', required=False),
            e=dict(type='int', required=False),
            f=dict(type='int', default=False),
            g=dict(type='int', default='7'),
            h=dict(type='int', required=False),
        ),
        supports_check_mode=True
    )

    m._ansible_no_log = True
    m.check_mode = False


# Generated at 2022-06-13 10:48:34.808630
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, '', '', None, None)
    assert am.TRANSFERS_FILES is False

# Generated at 2022-06-13 10:48:37.532433
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule(task=None, connection=None, _play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:48:44.062773
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = AnsibleModule(
        argument_spec = dict(
            cacheable = dict(required=False, type='bool', default=False),
            a = dict(required=True, type='str'),
            b = dict(required=True, type='str'),
        ),
        supports_check_mode=False
    )
    module.check_mode = False

    action_module = ActionModule(task=dict(action='set_fact', args=dict(a='value_a', b='value_b')), connection=None, play_context=None)
    result = action_module._execute_module(module_name='set_fact', module_args=dict(a='value_a', b='value_b'), task_vars=dict())

# Generated at 2022-06-13 10:48:44.617068
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:48:45.304441
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()

# Generated at 2022-06-13 10:48:47.738357
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ACTION_MODULE = ActionModule()
    # Verify that True is being returned when no error is thrown
    assert ACTION_MODULE.run() == True

# Generated at 2022-06-13 10:50:29.522039
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:50:31.154783
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None, None, None)
    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 10:50:39.738176
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def __get_task(args, task_vars=dict()):
        from ansible.playbook.task import Task
        from ansible.vars import VariableManager
        from ansible.utils.vars import load_extra_vars

        task = Task()
        task._role = None
        task.args = args
        if task_vars:
            task_vars = load_extra_vars(task_vars)
            variables = VariableManager(loader=None, inventory=None)
            variables.extra_vars = task_vars
        else:
            variables = VariableManager()
        task._variable_manager = variables

        return task

    class ActionModuleMixin(ActionModule):
        pass


# Generated at 2022-06-13 10:50:43.513038
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Executing constructor test for class ActionModule")

    # Constructor test 1
    print("Constructor test 1")
    import ansible.playbook.task_include
    action = ansible.playbook.task_include.TaskInclude()
    obj = ActionModule(action, dict())
    print("Exiting constructor test 1")
    return obj


# Generated at 2022-06-13 10:50:45.600572
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run'), 'ActionModule must have a run method'

# Generated at 2022-06-13 10:50:49.234869
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action is not None

# Generated at 2022-06-13 10:50:57.540422
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    data = dict(
        name="Test_Run_ACTION",
        args={'subscribe': '{{ ansible_hostname }}'},
    )

    # unit test without ansible_hostname defined
    action = ActionModule(None, data, None)
    try:
        action.run({}, {})
        assert False
    except AssertionError:
        assert True

    # unit test with ansible_hostname defined
    data['args']['ansible_hostname'] = 'TestValue'

    action = ActionModule(None, data, None)
    result = action.run({}, {})

    assert 'ansible_facts' in result
    assert result['ansible_facts']['subscribe'] == '{{ ansible_hostname }}'



# Generated at 2022-06-13 10:50:57.935414
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:50:59.072631
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None)
    assert(action is not None)

# Generated at 2022-06-13 10:51:03.659996
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor test: args
    test_data = {
            'args': {
                'test': 1,
                'test2': True,
                }
            }
    action = ActionModule(dict(), test_data)
    assert action._task.args['test'] == 1
    assert action._task.args['test2'] is True
    assert action._task.args['cacheable'] is False

    # Constructor test: args with cacheable
    test_data = {
            'args': {
                'test': 1,
                'test2': True,
                'cacheable': True,
                }
            }
    action = ActionModule(dict(), test_data)
    assert action._task.args['test'] == 1
    assert action._task.args['test2'] is True