

# Generated at 2022-06-13 09:44:42.573563
# Unit test for constructor of class ActionModule
def test_ActionModule():

    action = ActionModule()

    assert action._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))
    assert action.TRANSFERS_FILES == False

# Generated at 2022-06-13 09:44:52.098513
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
        Unit tests for constructor of class ActionModule
    '''

    def wrap_module_utils_basic(value):
        '''
            Method which will be used to wrap the module_utils.basic.AnsibleModule
        '''

        # Executing action module
        action_module = ActionModule()
        action_module.run(task_vars=dict(myvar=value))

        return action_module

# Generated at 2022-06-13 09:45:02.043384
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule()

    # First test, 'msg' option
    actionModule._task.args = {'msg': 'Hello world'}
    result = actionModule.run()

    assert result['msg'] == 'Hello world'
    assert result['failed'] == False

    # Second test, 'var' option
    
    # Second test, 'var' option
    actionModule._task.args = {'var': 'world'}
    actionModule._templar.available_variables = {'world': 'Hello'}
    result = actionModule.run()
    assert result['Hello'] == 'Hello'
    assert result['failed'] == False

    # Third test, 'var' option is a list
    actionModule._task.args = {'var': ['world', 'world1', 'world2']}
    actionModule._tem

# Generated at 2022-06-13 09:45:13.427858
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    task_vars = dict()
    module_name = 'ActionModule_run_test'
    basic._ANSIBLE_ARGS = None
    task_args = dict(
        var=['var1','var2','var3','var4','var5','var6'],
    )
    # module = ActionModule(
    #     task=task, task_vars=task_vars,
    #     runner_path='/home/jdoo/ansible/ansible/plugins/runners/')
    module_args = dict(
        var=['var1','var2','var3','var4','var5','var6'],
    )
    module = ActionModule()

    print(task_args)
    print(task_vars)
    print(module_args)



# Generated at 2022-06-13 09:45:14.063738
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:45:16.949195
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))

# Generated at 2022-06-13 09:45:31.347261
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule

    Check if the run method prints a message if verbosity is lower than the
    verbosity of the module
    """

    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    # create task
    block = Block()
    role = Role()
    task = Task()
    task._role = role
    task._block = block
    task.args = {
        'verbosity': 1,
        'msg': 'Hello world!'
    }

    # create action module
    new_stdout = StringIO()
    new_display = Display()
    new_display.verbosity = 0
    new_display.console = new_stdout


# Generated at 2022-06-13 09:45:42.011666
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:45:43.059999
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, {}, None)

# Generated at 2022-06-13 09:45:46.368042
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    task = Task()
    task.args = {
        'msg': 'Hello world!'
    }

    play_context = PlayContext()

    action = ActionModule(task, play_context)

# Generated at 2022-06-13 09:45:53.201461
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None)
    assert module is not None

# Generated at 2022-06-13 09:45:55.549243
# Unit test for constructor of class ActionModule
def test_ActionModule():
    cls = ActionModule(None, None, None, None, None)
    # TODO: Add asserts to see if all fields are set correctly
    assert (True)

# Generated at 2022-06-13 09:45:57.564525
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create ActionModule object
    am = ActionModule()

    # Assert object type ActionModule
    assert type(am) is ActionModule


# Generated at 2022-06-13 09:45:58.288657
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict(), dict(), True) is not None

# Generated at 2022-06-13 09:46:08.777851
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # set up object to call run on
    module = ActionModule()
    module._task.args = {}
    module._display.verbosity = 0
    module._templar.template = lambda x: x
    module._templar.bare_vars = lambda : []
    # call run
    results = module.run()
    # assert results
    assert 'msg' in results
    # set up another object
    module = ActionModule()
    module._task.args = {'msg': 'Hello from a test'}
    module._display.verbosity = 0
    module._templar.template = lambda x: x
    module._templar.bare_vars = lambda : []
    # call run
    results = module.run()
    assert 'msg' in results
    assert results['msg'] == 'Hello from a test'

# Generated at 2022-06-13 09:46:13.665947
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert_equals(am._VALID_ARGS, frozenset(('msg', 'var', 'verbosity')))
    assert am.TRANSFERS_FILES is False

# Generated at 2022-06-13 09:46:18.192984
# Unit test for constructor of class ActionModule
def test_ActionModule():
  action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
  assert action_module != None, "action_module should be defined"

# Generated at 2022-06-13 09:46:18.938050
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:46:29.840714
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    tmp = None

    test_action = ActionModule(task=dict(args=dict(verbosity=1)), tmp=tmp, task_vars=task_vars)

    assert isinstance(test_action, ActionModule)

    assert not test_action.run(tmp, task_vars)

    # Testing without msg and var
    test_action = ActionModule(task=dict(args=dict(verbosity=1)), tmp=tmp, task_vars=task_vars)
    assert test_action.run(tmp, task_vars)['msg'] == 'Hello world!'

    # Testing with msg
    test_action = ActionModule(task=dict(args=dict(verbosity=1, msg='Hello!')), tmp=tmp, task_vars=task_vars)
    assert test

# Generated at 2022-06-13 09:46:38.757779
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # creating mock instances
    task = Task()
    task.args = {'msg': 'Hello world!'}
    action_base = ActionBase()
    action_base._task = task
    action_module = ActionModule(action_base)
    result = action_module.run(None, None)

    assert result == {
        'msg': 'Hello world!',
        '_ansible_verbose_always': True,
        'failed': False
    }



# Generated at 2022-06-13 09:46:58.972234
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import unittest
    
    # Test template
    class TestTask(unittest.TestCase):
        def setUp(self):
            self.check_args = {
                'msg': 'Hello, world!',
                'verbosity': 3
            }
            self.check_play_context = {
                'verbosity': 3
            }
            self.check_iterator = {}
            self.check_play = {}
            self.check_basedir = '/path/to/ansible'
            self.check_templar = {}
            self.check_shared_loader_obj = {}

        def test_init_check(self):
            from ansible.plugins.action import ActionModule

# Generated at 2022-06-13 09:47:01.536582
# Unit test for constructor of class ActionModule
def test_ActionModule():
    template = "hello {{world}}"
    verbosity = 0
    obj = ActionModule(template, verbosity)
    # print(obj)
    assert False

# Generated at 2022-06-13 09:47:09.672178
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test ActionModule constructor without argument
    action_module = ActionModule()
    assert isinstance(action_module, ActionBase)
    # test ActionModule constructor with argument
    mock_task = {}
    action_module = ActionModule(task=mock_task)
    assert action_module._task == mock_task
    assert action_module.task_vars == {}
    # test ActionModule constructor with arguments
    mock_task = {}
    mock_connection = {}
    mock_play_context = {}
    mock_loader = {}
    mock_templar = {}
    mock_shared_loader_obj = {}

# Generated at 2022-06-13 09:47:19.431760
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import sys
    import mock

    test_dir = os.path.dirname(__file__)
    lib_dir = os.path.join(test_dir, '../..')
    sys.path.insert(0, os.path.realpath(lib_dir))

    # Test module and class name
    assert ActionModule.__module__ == 'ansible.plugins.action.debug'
    assert ActionModule.__name__ == "ActionModule"

    class AnsibleModule:
        def __init__(self, argument_spec, bypass_checks=None, no_log=None,
                     check_invalid_arguments=None, mutually_exclusive=None):
            assert bypass_checks is False
            assert no_log is False
            assert check_invalid_arguments is None
            assert mutually_exclusive is None
           

# Generated at 2022-06-13 09:47:24.598227
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = {'var2': 'value2'}
    action_module = ActionModule(Task(), Connection(), 'test')
    # Check that module returns a dictionary
    assert isinstance(action_module.run(task_vars=task_vars), dict), \
    "ActionModule.run() did not return a dictionary."

# Generated at 2022-06-13 09:47:30.456496
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule

    :return: None
    '''
    class PlayContext(object):
        ''' empty PlayContext class '''
        pass

    class Task(object):
        ''' empty Task class '''
        pass

    class Options(object):
        ''' empty Options class '''
        def __init__(self):
            self.module_path = '.'
            self.connection = 'ssh'
            self.remote_user = 'hong'
            self.private_key_file = '~/.ssh/id_rsa'
            self.verbosity = 0
            self.timeout = 10

    class DataLoader(object):
        ''' empty DataLoader class '''
        def __init__(self):
            pass


# Generated at 2022-06-13 09:47:40.365812
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a mock module
    module = AnsibleModule(
        argument_spec={'msg': {'type': 'str'}, 'var': {'type': 'str'}, 'verbosity': {'type': 'int'}},
        supports_check_mode=True
    )

    # Create object of class ActionModule
    action_module = ActionModule(module=module, task_vars={})

    # Run the method run of class ActionModule and test its result
    assert action_module.run(tmp=None, task_vars=None) == {'failed': False, 'msg': 'Hello world!'}
    assert action_module.run(tmp=None, task_vars=None) == {'failed': False, 'msg': 'Hello world!'}

# Generated at 2022-06-13 09:47:41.504155
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
        Unit test for ActionModule
    '''
    assert ActionModule(None, None, {})

# Generated at 2022-06-13 09:47:45.681100
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Check initial instance variables of ActionModule
    assert ActionModule._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))
    assert ActionModule.TRANSFERS_FILES == False

# Generated at 2022-06-13 09:47:49.320317
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = None
    task_vars = None
    test_obj = ActionModule(tmp, task_vars)

    assert test_obj.run() == None

# Generated at 2022-06-13 09:48:21.667566
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.display import Display
    from ansible.plugins.loader import plugin_loader
    # Need to register all action plugins
    plugin_loader.add_directory('./plugins/actions')

    variable_manager = VariableManager()
    loader = DataLoader()
    display = Display()

    # Create dummy plugin

# Generated at 2022-06-13 09:48:22.332383
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:48:31.674477
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionBase
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.cli.playbook.playbook_cli import PlaybookCLI
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display

    args = {'verbosity': 0, 'msg': 'Hello world!'}
    tqm = None
    loader = DataLoader()
    play_context = PlayContext()
    play_context._succeeded = True
    play_

# Generated at 2022-06-13 09:48:41.158023
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    pb = Playbook().load("test.yml", variable_manager=None, loader=None)
    pb.get_plays()

    assert len(pb.get_plays()) == 1
    assert isinstance(pb.get_plays()[0], Play)
    assert pb.get_plays()[0].hosts == ['hostname']
    assert pb.get_plays()[0].name == "Ansible Play"
    assert len(pb.get_plays()[0].tasks) == 1
    assert pb.get_plays()[0].tasks[0].action == "debug"
    assert pb.get_plays()[0].tasks[0].name == "msg"
    assert pb.get

# Generated at 2022-06-13 09:48:50.558387
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.template
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.play_context import PlayContext
    from operator import attrgetter

    # Fake class to use as callback plugin

# Generated at 2022-06-13 09:48:51.267307
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:49:00.324750
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    data = dict(
        msg='Hello world!',
        var={'test': 'Hello'},
        verbosity=0
    )

    action = ActionModule(None, None, data)
    result = action.run()

    # Check the results
    assert 'Hello world!' in result['msg']
    assert isinstance(result['dict'], dict)
    assert 'Hello' == result['dict']['test']

    # Check the module execution
    assert not result['failed']
    assert not result['skipped']

# Generated at 2022-06-13 09:49:09.176686
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.debug import ActionModule
    from ansible.module_utils.six import PY3
    import sys
    import json

    # Python 3 renamed unicode to str
    if PY3:
        unicode = str

    # get task verbosity
    verbosity = 2

    # call method run of class ActionModule
    obj = ActionModule()

    # create a task
    obj._task = type('task', (object,), dict())
    # create dict for task.args
    obj._task.args = dict()
    if verbosity <= obj._display.verbosity:
        # add msg to task.args
        obj._task.args['msg'] = "Hello world!"
    else:
        obj._task.args['verbosity'] = verbosity

# Generated at 2022-06-13 09:49:20.727382
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # import built-in module unittest
    import unittest

    # create test class
    class TestActionModuleRun(unittest.TestCase):
        def __init__(self, *args, **kwargs):
            # call super class init method
            super(TestActionModuleRun, self).__init__(*args, **kwargs)

        # public function to test method run of class ActionModule
        def test_ActionModule_run(self):
            # instantiate ActionModule class
            actmod = ActionModule()

        # public function to test method run of class ActionModule with msg parameter
        def test_ActionModule_run_msg(self):
            # instantiate ActionModule class
            actmod = ActionModule()

        # public function to test method run of class ActionModule with msg and verbosity parameter

# Generated at 2022-06-13 09:49:25.060355
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a ActionBase instance
    actionBase = ActionBase()

    # Create a ActionModule instance
    actionModule = ActionModule()


    # Run the method
    result = actionModule.run(tmp=None, task_vars=None)
    assert result == { 'failed': True, 'msg': "'msg' and 'var' are incompatible options" }

#Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:50:15.227729
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a new instance of class ActionModule
    action_module = ActionModule()
    # Check if property TRANSFERS_FILES of ActionModule is False
    assert action_module.TRANSFERS_FILES == False
    # Check if property _VALID_ARGS of ActionModule contains msg, var and verbosity
    assert action_module._VALID_ARGS == ("msg", "var", "verbosity")

# Generated at 2022-06-13 09:50:16.541459
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionBase)

# Generated at 2022-06-13 09:50:26.295323
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock normal run
    task_args = {'msg': 'Hello world!'}
    verbosity = 0
    display_verbosity = 0
    display_skipped_with_verbosity = False
    actionmodule = ActionModule(task_args, verbosity, display_verbosity, display_skipped_with_verbosity, None, None)
    results = actionmodule.run(None, None)
    assert results['msg'] == 'Hello world!'
    assert results['failed'] == False
    assert results['skipped'] == False

    # mock verbosity threshold not met
    task_args = {'msg': 'Hello world!', 'verbosity': 9}
    verbosity = 0
    display_verbosity = 0
    display_skipped_with_verbosity = False

# Generated at 2022-06-13 09:50:38.954502
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def make_task(**kwargs):
        return {'args': kwargs}

    class AnsibleModule(object):

        def __init__(self, out):
            self.return_values = out

        def exit_json(self, **kwargs):
            self.return_values = kwargs

        def fail_json(self, **kwargs):
            self.return_values = kwargs

    class MockConnection(object):
        def __init__(self, host, port, user, passwd):
            self.connected = False

        def connect(self, host, port, user, passwd):
            self.connected = True

        def disconnect(self):
            self.connected = False

    class MockTemplar(object):
        def __init__(self):
            self.return_values = 0


# Generated at 2022-06-13 09:50:39.809717
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None


# Generated at 2022-06-13 09:50:40.749239
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:50:46.005250
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule('dummy_playbook', 'dummy_task', task_args={'dummy_key': 'dummy_value'}, loader=None, templar=None, shared_loader_obj=None)
    assert action._task == 'dummy_task'
    assert action._task_vars == {}
    assert action._loader == None
    assert action._shared_loader_obj == None
    assert action._templar == None
    assert action._display == None
    assert action._task_vars == {}

# Generated at 2022-06-13 09:50:49.492764
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule, (type, object)), 'The type of ActionModule is not correct'
    assert isinstance(ActionModule.run, (object, type(lambda: True))), 'The type of ActionModule.run is not correct'

# Generated at 2022-06-13 09:50:50.148565
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 09:50:50.764480
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:52:50.622020
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test simple message printing
    args = {'msg': 'Hello world!'}
    action_module = ActionModule(dict(), dict(ANSIBLE_MODULE_ARGS=args))
    result = action_module.run()
    assert result == {'msg': 'Hello world!', 'failed': False, '_ansible_verbose_always': True}

    # Test skipped message printing
    args = {'msg': 'Hello world!', 'verbosity': 1}
    action_module = ActionModule(dict(), dict(ANSIBLE_MODULE_ARGS=args))
    result = action_module.run()
    assert result == {'skipped_reason': 'Verbosity threshold not met.', 'skipped': True}

    # Test printing of undefined variable
    test_module = 'testmodule'

# Generated at 2022-06-13 09:53:00.853048
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    _task = {}
    _play_context = {}
    _loader = {}
    _templar = {}
    _display = {}
    _connection = {}
    _play_context.verbosity = 3
    _task.args = {"verbosity" : 4}
    _actions = ActionModule(task=_task, play_context=_play_context, loader=_loader, templar=_templar, display=_display, connection=_connection)
    _result = _actions.run()
    assert _result['skipped'] == True
    assert _result['skipped_reason'] == "Verbosity threshold not met."
    _task.args = {"msg" : "test_msg"}

# Generated at 2022-06-13 09:53:11.473654
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import collections
    import unittest
    import ansible.errors
    import ansible.playbook.task
    import ansible.plugins.action
    import ansible.template
    import ansible.vars

    class Tac(collections.namedtuple('Tac', ['args'])):
        """Tuple action class"""

    class Vars(object):
        """Vars class"""
    vars = Vars()

    class ActionBaseClass(ansible.plugins.action.ActionBase):
        """ActionBaseClass used for unit test"""
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            self._task = task
            self._connection = connection
            self._play_context = play_context
            self._loader = loader
            self._templar = tem

# Generated at 2022-06-13 09:53:16.427202
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # This is just a sample test to show how to create unit tests for
    # custom modules.  Ansible modules should not need any unit tests
    # as the run() function should be used to validation the results
    # of the action module.
    action_module = ActionModule()
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:53:29.046246
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # In order to create this module an Ansible module mock has to be created.
    import ansible.modules.system.debug
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.ansible_release import __version__
    from ansible.module_utils.six import PY3

    # When we aren't on Python3, we need to encode the results as utf-8
    if not PY3:
        def to_native(s):
            return s.encode('utf-8')
    else:
        def to_native(s):
            return s

    # Initialize module
    task_args = dict(msg="Hello world!", verbosity=0)

# Generated at 2022-06-13 09:53:29.829600
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "TBD"

# Generated at 2022-06-13 09:53:33.076744
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule(action_base=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert actionModule is not None


# Generated at 2022-06-13 09:53:35.586789
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_object = ActionModule(action=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert ActionModule is type(test_object)

# Generated at 2022-06-13 09:53:38.808276
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #Asserting ActionBase had been called with no arguments
    assert isinstance(ActionModule(), ActionBase)

# Module testing for ActionModule
if __name__ == '__main__':
    #test_ActionModule()
    pass

# Generated at 2022-06-13 09:53:49.722648
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of the class
    # Note that we are not calling the __init__ function
    action_module = ActionModule()
    assert isinstance(action_module, ActionModule)

    # Test the __init__ function
    action_module = ActionModule('arg1', 'arg2', 'arg3','arg4', 'arg5', 'arg6')
    assert isinstance(action_module, ActionModule)

    # Test the get_valid_attrs function
    ret = action_module._get_valid_attrs()
    assert isinstance(ret, frozenset)
    assert ret == frozenset(('msg', 'var', 'verbosity'))

    # Test the get_valid_args function
    ret = action_module._get_valid_args()
    assert isinstance(ret, frozenset)
    assert ret == fro