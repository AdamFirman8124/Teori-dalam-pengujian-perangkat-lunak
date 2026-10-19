

# Generated at 2022-06-13 09:44:43.433485
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, dict(msg = 'This is a test message'))
    result = module.run(task_vars = dict())
    assert result[u'failed'] == False
    assert result[u'msg'] == 'This is a test message'

# Generated at 2022-06-13 09:44:47.343938
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(
        task=dict(args=dict(
            var='var',
        )),
        connection=None,
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert a is not None

# Generated at 2022-06-13 09:44:58.347821
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.strategy import StrategyBase
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role_include import IncludeRole
    from ansible.module_utils.facts import ModuleReplacer
    from ansible.executor.task_result import TaskResult

# Generated at 2022-06-13 09:45:05.555309
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # init ActionModule object
    am = ActionModule(None, {'var':{'a':1, 'b':2}, 'msg':"test", 'verbosity':0}) # will print msg
    results = am.run({}, task_vars={'a':1, 'b':2})
    assert isinstance(results, dict) is True
    assert results['failed'] == False
    assert results['msg'] == "test"
    assert '_ansible_verbose_always' in results
    assert results['_ansible_verbose_always'] == True

    # test with var
    am = ActionModule(None, {'var':['a', 'b'], 'msg':"test", 'verbosity':0}) # will print msg
    results = am.run({}, task_vars={'a':1, 'b':2})

# Generated at 2022-06-13 09:45:10.129840
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import random
    import string

    # test random string of size 6
    def random_string():
        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))

    test_msg = random_string()
    test_dict = {'test_msg': test_msg}
    test_var = 'test_msg'
    test_var_not_exist = 'test_msg1'

    # test with verbosity 0
    print("\ntest with verbosity 0")
    task_vars = test_dict
    task_args = {'verbosity': 0, 'msg': test_msg}
    task_args2 = {'verbosity': 0, 'var': test_var}

# Generated at 2022-06-13 09:45:10.973374
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()

# Generated at 2022-06-13 09:45:11.586469
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:45:19.346293
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''
    # Test module with existing var
    module = ActionModule()

    # Test module with existing var
    task_vars = dict(foo='foo')
    task = dict(action='debug', args=dict(msg='hello world'))
    module._execute_module(task_vars=task_vars, task=task)
    assert module._result['msg'] == 'hello world'

    # Test module with existing var
    task_vars = dict(foo='foo')
    task = dict(action='debug', args=dict(var='foo'))
    module._execute_module(task_vars=task_vars, task=task)
    assert module._result['foo'] == 'foo'

    # Test module with not existing var
    task_vars = dict()

# Generated at 2022-06-13 09:45:19.996517
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()

# Generated at 2022-06-13 09:45:20.831466
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:45:29.903140
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #Unit test for the run method of the class ActionModule
    #args = {'verbosity': u'1'}
    #action = ActionModule()
    #result = action.run(args)
    action = ActionModule()
    print(action.run())

# Generated at 2022-06-13 09:45:34.492924
# Unit test for constructor of class ActionModule
def test_ActionModule():
	from ansible.plugins.action import ActionModule
	print ("<==========Unit test of ActionModule() constructor==========>\n")
	action=ActionModule('', {'key':'value'}, '', '', '', '')
	print ("\n<==========Unit test of ActionModule() constructor==========>")

# Unit test of run() function inside class ActionModule

# Generated at 2022-06-13 09:45:35.596559
# Unit test for constructor of class ActionModule
def test_ActionModule():
    return 0


# Generated at 2022-06-13 09:45:46.260377
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_data = [
        ('dict-type', {'var': {'name': 'test'}, 'verbosity': 1}, {'<type \'dict\'>': {'name': 'test'}}),
        ('list-type', {'var': ['name', 'test'], 'verbosity': 1}, {'<type \'list\'>': ['name', 'test']}),
        ('no-var', {'verbosity': 1}, {'msg': 'Hello world!'}),
        ('no-var-verbosity-2', {'verbosity': 2}, {'_ansible_verbose_always': True, 'msg': 'Hello world!'}),
        ('no-var-verbosity-2', {'verbosity': 1}, {'skipped': True, 'skipped_reason': 'Verbosity threshold not met.'})
    ]

# Generated at 2022-06-13 09:45:57.299247
# Unit test for constructor of class ActionModule
def test_ActionModule():
  import json

  # test case 1 - all parameters
  test_args = {}
  test_args['msg'] = 'Hello World!'
  test_args['var'] = 'test'
  test_args['verbosity'] = 2
  res = ActionModule(test_args, {})
  assert res['msg'] == test_args['msg']
  assert res['var'] == test_args['var']
  assert res['verbosity'] == test_args['verbosity']

  # test case 2 - minimal parameters
  test_args = {}
  test_args['var'] = 'test'
  test_args['verbosity'] = 1
  res = ActionModule(test_args, {})
  assert res['var'] == test_args['var']
  assert res['verbosity'] == test_args['verbosity']

  # test case

# Generated at 2022-06-13 09:45:58.524452
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule(None, None, None, None, None, None)
    assert obj is not None


# Generated at 2022-06-13 09:46:08.961696
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule
    """
    import sys
    sys.path.insert(0, '..')
    import module_utils.basic
    import plugins.action

    my_args = {'msg': 'Hello world!', 'verbosity': '0'}
    my_task = {'args': my_args}

    my_play_context = {'check_mode': False, 'verbosity': 1}
    my_loader = module_utils.basic.AnsibleModuleUtilsLoader()
    my_shared_loader_obj = module_utils.basic.AnsibleModuleUtilsSharedLoaderObj()
    my_action = plugins.action.ActionModule(my_target, my_connection, my_play_context, my_loader, my_shared_loader_obj, my_task)

    # Test with

# Generated at 2022-06-13 09:46:10.718558
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:46:11.963847
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None)


# Generated at 2022-06-13 09:46:17.498512
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import action_loader

    stub_class = action_loader.get('debug', class_only=True)
    assert stub_class != ActionModule
    stub_thing = stub_class()
    assert stub_thing._shared_loader_obj._loader._action_plugins['debug'] == ActionModule

# Generated at 2022-06-13 09:46:40.646795
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook import Play
    from ansible.inventory import Inventory
    from ansible.playbook.play import Playbook
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    import json

    # mock a task
    task = Task()
    task._role = None
    task.action = 'debug'
    task.loop = None
    task.once = None
    task._uuid = 'dummy_uuid'
    task._role_name = 'dummy_role_name'

    # mock a play
    play = Play()
    play.hosts

# Generated at 2022-06-13 09:46:44.556791
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    am._task.args = {'msg' : 'hello world'}
    tmp = "tmp"
    task_vars = {}
    result = am.run(tmp, task_vars)
    assert result['msg'] == 'hello world'

# Generated at 2022-06-13 09:46:50.053667
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(action=dict(module_name='debug', msg='Hello world!')),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert module._task.action['module_name'] == 'debug'
    assert module._task.action['msg'] == 'Hello world!'

# Generated at 2022-06-13 09:46:59.646899
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # initial setup
    class MockAnsibleModule(object):
        def fail_json(self, *args, **kwargs):
            return {'failed': True}

        def exit_json(self, *args, **kwargs):
            return {'failed': False}

    mod = MockAnsibleModule()
    mod.params = {"msg": "Dummy message", "verbosity": 10}

    # test case
    class MockTask(object):
        def __init__(self, module):
            self.args = {'msg': 'Dummy message', 'verbosity': 10}

    class MockDisplay(object):
        verbosity = 1

    task = MockTask(mod)
    display = MockDisplay()
    action_module = ActionModule(task, display)
    result = action_module.run()

    # check if the

# Generated at 2022-06-13 09:47:08.811995
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.module_utils.six import string_types

    # Load needed classes
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 09:47:18.971416
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class TestModule(ActionModule):
        def __init__(self, task, connection, action_loader, templar, shared_loader_obj):
            super(TestModule, self).__init__(task, connection, action_loader, templar, shared_loader_obj)

    class TestConnection:
        def __init__(self):
            self._shell = None
            self._play_context = None
            self._connected = None
            self._socket_path = None
            self._loader = None
            self._shell_type = None
            self._tmp = None

        def get_shell_type(self):
            return self._shell_type

        def set_shell_type(self, shell_type):
            self._shell_type = shell_type

    class TestTask:
        def __init__(self):
            self

# Generated at 2022-06-13 09:47:29.206666
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 09:47:38.990394
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Import modules
    from ansible.plugins.action.debug import ActionModule
    from ansible.module_utils.basic import AnsibleModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_context import PlayContext
    from ansible.playbook.play import Play

    # Variable initilization
    play_context = PlayContext()
    task_queue_manager = TaskQueueManager(play_context, '/home/pc/.ansible/plugins/modules', '/home/pc/.ansible/modules')

    # Play initilization

# Generated at 2022-06-13 09:47:46.467087
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test when args contain msg
    am = ActionModule(dict(msg='Hello world!'), dict(verbosity=0))
    result = am.run()
    assert result['msg'] == 'Hello world!'
    # test when args contains var
    am = ActionModule(dict(var='user'), dict(verbosity=0))
    result = am.run()
    assert 'user' in result
    assert result['user'] == 'VARIABLE IS NOT DEFINED!'
    am = ActionModule(dict(var='{{ user }}'), dict(verbosity=0))
    result = am.run()
    assert 'user' in result
    assert result['user'] == 'VARIABLE IS NOT DEFINED!'
    am = ActionModule(dict(var='user', verbosity=0), dict(user='toor'))

# Generated at 2022-06-13 09:47:47.074609
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 09:48:16.820046
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    test method run of class ActionModule
    '''
    import unittest.mock
    import sys
    if sys.version_info < (3, 0):
        builtin_str = '__builtin__.str'
    else:
        builtin_str = 'builtins.str'
    # object to be mock
    from ansible.plugins.action.debug import ActionModule
    # mock object
    from ansible.plugins.action.debug import mock_ansible_module, mock_templar
    # mock class
    from ansible.plugins.action.debug import mock_display

    # mock ansible_module
    ansible_module = mock_ansible_module.MockAnsibleModule()
    # mock templar
    templar = mock_templar.MockTemplar()

# Generated at 2022-06-13 09:48:27.226632
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None)
    assert module.run({}, {}) == {
        'failed': False,
        'msg': 'Hello world!',
        '_ansible_verbose_always': True,
    }, 'Bad output for the default case for the run method'

    assert module.run({}, {}, {
        'msg': 'hello world',
    }) == {
        'failed': False,
        'msg': 'hello world',
        '_ansible_verbose_always': True,
    }, 'Bad output for the default case for the run method'


# Generated at 2022-06-13 09:48:34.828422
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule"""
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action.runner = None
    action.connection = None
    action.connection_loader = None
    action._task.args = None
    action._templar = None
    action._low_level_runner_enabled = None
    action._display = None
    action._loader = None

    # with msg
    # setup the test class
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action.runner = None
    action.connection = None
    action.connection_loader = None

# Generated at 2022-06-13 09:48:43.953268
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.debug import ActionModule as m
    assert issubclass(m, ActionBase)

# Unit test suit for the action plugin
import unittest
from ansible.playbook.task import Task
from ansible.playbook.play_context import PlayContext
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_executor import TaskExecutor

from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

from ansible.plugins.loader import fragment_loader

from ansible.utils.vars import combine_vars

from ansible.utils.display import Display



# Generated at 2022-06-13 09:48:45.376576
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass



# Generated at 2022-06-13 09:48:50.103090
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """This is a test method for the class ActionModule.
    It should not be called manually.
    """

    module_args = {"msg": "Hello world!"}
    task_vars = {"var": "Hello world!"}
    am = ActionModule(None, module_args, task_vars)
    assert am is not None

# Generated at 2022-06-13 09:49:03.752620
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = {}
    host['ansible_verbosity'] = 0
    host['ansible_verbose'] = False

    task_args = {}
    task_vars = {}
    module_default_args = {}

    tmp = None
    display = None
    task = None
    action_plugin = None
    templar = None

    action_module_obj_1 = ActionModule(host=host, task=task, task_vars=task_vars, templar=templar, display=display)
    module_default_args.update({'msg':'Hello world!'})
    action_module_obj_1.set_modules_args(module_default_args)
    action_module_obj_1.set_args(task_args)

# Generated at 2022-06-13 09:49:09.867161
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    if sys.version_info[0] == 2:
        import __builtin__ as builtins
    else:
        import builtins
    import collections
    import ansible.plugins.action
    import ansible.playbook.play
    import ansible.utils.template

    loader_mock = collections.namedtuple('DummyLoader', ('get_basedir', 'path_dwim'))
    loader_mock.get_basedir.return_value = None

    templar_mock = ansible.utils.template.Templar(loader=loader_mock)

    variable_manager_mock = collections.namedtuple('DummyVariableManager', ('extra_vars',))
    variable_manager_mock.extra_vars = {}


# Generated at 2022-06-13 09:49:15.441560
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.playbook.task import Task

    module = ActionModule(Task(), dict())
    result = module.run(dict())
    assert result.get('failed') is False
    assert result['msg'] == 'Hello world!'
    assert result['_ansible_verbose_always'] is True

# Generated at 2022-06-13 09:49:22.005770
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    from ansible.plugins.loader import action_loader
    action_cls = action_loader.get('debug', class_only=True)

    task = Task()
    try:
        action = action_cls(task, {})
    except Exception as e:
        assert False, "ActionModule constructor throws exception with message {}".format(str(e))

# Generated at 2022-06-13 09:50:10.989187
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test constructor
    # import modules to Test
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins import module_loader
    from ansible.playbook import Playbook
    from ansible.playbook.block import Block
    import ansible.module_utils.six as six
    # Instantiate class.
    hostvars = dict()
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory()
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 09:50:24.239852
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # String msg:
    task = dict(msg='Hello')
    tmp = None
    task_vars = dict()

    am1 = ActionModule(task, tmp, task_vars)
    results1 = am1.run() # default verbosity is 0

    assert(results1['failed'] == False)
    assert(results1['msg'] == 'Hello')

    # String msg with verbosity
    task = dict(msg='Hello', verbosity='1')
    tmp = None
    task_vars = dict()

    am2 = ActionModule(task, tmp, task_vars)
    results2 = am2.run()

    assert(results2['failed'] == False)
    assert(results2['msg'] == 'Hello')

    # param var: string var
    task = dict(var='test_var')
    tmp

# Generated at 2022-06-13 09:50:25.267860
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:50:27.369284
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: Write unit tests for constructor of class ActionModule
    assert True


# Generated at 2022-06-13 09:50:39.692680
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    If the ActionModule class is passed to _load_action_plugin, ensure that we get
    an instance of our plugin back.
    '''
    def make_loader(action_class_name, action_class=None):
        '''
        Make just enough of a loader to load a plugin
        '''

# Generated at 2022-06-13 09:50:40.597805
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()

# Generated at 2022-06-13 09:50:47.954016
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_result = {'failed': False, 'changed': True, 'changed_when_results': True, 'invocation': {'module_args': {'msg': 'Hello world!', 'verbosity': 0, '_ansible_check_mode': False, '_ansible_debug': False, '_ansible_diff': False, '_ansible_verbosity': 4, '_ansible_version': '2.4.2.0', '_ansible_module_name': 'am_debug'}}, '_ansible_verbose_always': True}

# Generated at 2022-06-13 09:50:53.554691
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Init
    actionmodule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    actionmodule._display = DummyDisplay()
    actionmodule._task = DummyTask()
    actionmodule._templar = DummyTemplar()
    # Exercise

    # Assert
    assert isinstance(actionmodule.run(tmp=None, task_vars=None), dict)


# Generated at 2022-06-13 09:51:05.666441
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    import unittest

    class ActionModuleTest(unittest.TestCase):
        def setUp(self):
            self.loader = None
            self.invent = None
            self.variable_manager = None

            self.hosts = [Host(name='59.110.23.80', port=22)]
            self.groups = [Group('test_group')]

# Generated at 2022-06-13 09:51:10.417342
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initializing a sample task
    task = {"verbosity": 0, "msg": "This task is being executed"}
    task_vars = {}

    # Initializing ActionModule object
    action_obj = ActionModule(task, None, None)

    # Invoking run method
    action_obj.run()

# Generated at 2022-06-13 09:53:10.572040
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:53:16.756871
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule """

    # Run test
    actor = ActionModule()
    result = actor.run(tmp=None, task_vars=None)

    # Check result
    assert result['failed'] is False
    assert result['msg'] == 'Hello world!'


# Generated at 2022-06-13 09:53:28.021307
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.debug import ActionModule

    # Test case: check initialized variables of ActionModule
    print("test_ActionModule: check initialized variables of ActionModule")
    obj_module = ActionModule()
    assert obj_module.TRANSFERS_FILES == False

    # Test case: check methods of class ActionModule
    print("test_ActionModule: check methods of class ActionModule")
    print("test_ActionModule: check run method")
    parameters = {
        'msg': 'Hello world!',
    }
    assert obj_module.run(task_vars={}, tmp=None, **parameters)['msg'] == 'Hello world!'

# Generated at 2022-06-13 09:53:29.901971
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)
    action_module = ActionModule()
    assert isinstance(action_module, ActionBase)
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:53:38.882731
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    class Singleton(type):  # noqa
        _instances = {}
        def __call__(cls, *args, **kwargs):  # noqa
            if cls not in cls._instances:
                cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]

    class Display():  # noqa
        __metaclass__ = Singleton
        def __init__(self):  # noqa
            self.verbosity = 0

    class Task():  # noqa
        def __init__(self):
            self.args = dict(msg='Hello World')

    class PlayContext():  # noqa
        def __init__(self):
            self.check_mode = False

   

# Generated at 2022-06-13 09:53:49.761313
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost')
    play_source = {
            'name': "Ansible Play",
            'hosts': 'localhost',
            'gather_facts': 'no',
            'tasks': [
                {'action': {'module': 'debug', 'args': {'msg': 'Hello World'}}, 'name': 'debug'}
            ]
    }

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    #

# Generated at 2022-06-13 09:53:55.483516
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # instantiate a ActionModule object
    print('\nIn test_ActionModule')
    test_obj = ActionModule(None)
    print('type of test_ActionModule is:', type(test_obj))
    print(test_obj)
    assert test_obj is not None
    assert test_obj._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))

if __name__=='__main__':
    test_ActionModule()

# Generated at 2022-06-13 09:54:00.681173
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # check for abstract class
    try:
        action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    except TypeError as e:
        assert "Can't instantiate abstract class ActionModule with abstract methods run" == str(e)
    else:
        assert False, 'Expected error not thrown'


# Generated at 2022-06-13 09:54:14.064598
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict(
        result_key1=u"test_result_key1",
        result_key2=u"test_result_key2",
        debug_key1=u"test_debug_key1",
        debug_key2=u"test_debug_key2",
        debug_key3=u"test_debug_key3",
    )
    task_args = dict(
        msg=u"test_msg",
        var=u"result_key1",
        verbosity=3,
    )

    # Replace _templar with a class that simulates the templating
    class TestTemplate:
        def __init__(self, convert_bare=False, fail_on_undefined=False):
            self.convert_bare = convert_bare
            self.fail_on_und

# Generated at 2022-06-13 09:54:21.991777
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.vars.manager import VariableManager

    context = PlayContext()
    task = AnsibleModule(dict(action='debug',msg='Hello world!'),display=ActionBase._display,context=context)
    task.async_val = 0
    task._connection = None

    var_manager = VariableManager()
    task_queue = TaskQueueManager(inventory=None, variable_manager=var_manager)

    pbex = PlaybookExecutor(playbooks=[task], inventory=None, variable_manager=var_manager, loader=None,
                            options=None, passwords=None)

    pbex._