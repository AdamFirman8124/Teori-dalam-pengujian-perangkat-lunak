

# Generated at 2022-06-13 09:44:44.814514
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.debug import ActionModule

    main_obj = ActionBase()
    ActionModule(main_obj._connection, main_obj._play_context, main_obj._loader, main_obj._templar, main_obj._shared_loader_obj)

# Generated at 2022-06-13 09:44:47.716382
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class TestActionModule(ActionModule):
        def run(self):
            super(TestActionModule, self).run()

    with pytest.raises(AnsibleUndefinedVariable):
        TestActionModule(dict(), dict(), None).run()

# Generated at 2022-06-13 09:44:57.636436
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Verify constructor throw exception when no argument passed in
    result = dict(failed=False, msg='Hello world!', skipped=False, changed=False)
    mock_display = Mock()
    mock_display.verbosity = 0
    mock_task = Mock(args=None)
    mock_task.args = dict()
    mock_task.args['msg'] = 'Hello world!'
    mock_task.args['verbosity'] = 0
    action = ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action._display = mock_display
    assert action.run() == result


# Generated at 2022-06-13 09:44:58.596901
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # ToDo: create a mock of ActionModule
    pass

# Generated at 2022-06-13 09:45:05.668234
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.executor.task_result import TaskResult
    
    # Create a mock task
    task = MockTask()
    task.run.return_value = TaskResult()
    
    # Create a mock display
    display = MockDisplay()
    
    # Create a mock task in executor
    task_ret = TaskResult()
    task_in_executor = MockTask()
    task_in_executor.run.return_value = task_ret

    # Create test fixture
    fake_task_vars = dict()
    fixture = ActionModule(task, display, fake_task_vars)
    result = fixture.run()

    # Assertion
    assert result is not None
    assert result == task_ret


# Mock class for TaskResult class

# Generated at 2022-06-13 09:45:15.985651
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ 
    Test method run of class ActionModule.

    Unit test for the method run of class ActionModule.
    """
    print("\nStarting test_ActionModule_run.")
    import sys
    import os
    import unittest
    sys.path.insert(0,os.path.abspath((os.path.join(os.path.dirname(__file__),'..'))))
    from plugins.action import ActionModule
    from lib.module_utils import temp_dir
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.plugins.action import action_base
    from units.mock.plugins.action import TaskExecutor
    from units.mock.plugins.action import TaskVars


# Generated at 2022-06-13 09:45:27.715459
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Test class ActionModule with normal operation
    '''

    module = ActionModule(load_attributes_from_file=False)
    module.set_options({'verbosity': 0})
    module._task.args = {'var': 'myvar', 'verbosity': 0}
    module._display.verbosity = 0

    module._templar.template = lambda a, b=False, c=False: a
    module._templar.template = lambda a, b=False, c=False: a

    result = module.run({}, {'myvar': 'result'})
    if 'result' not in result:
        raise AssertionError("Missing 'result' in %s" % (result))

# Generated at 2022-06-13 09:45:28.627635
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass


# Generated at 2022-06-13 09:45:38.339210
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager

    context = PlayContext()
    task = Task()
    # Just to satisfy constructor
    task_q_mgr = TaskQueueManager()

    # Creating ansible.plugins.action.ActionBase object

# Generated at 2022-06-13 09:45:46.788951
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor of class ActionModule
    class_ActionModule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # get transaction, class instance attributes
    dict_class_ActionModule = class_ActionModule.__dict__

    # Check if transaction and class instance attributes are not none
    assert (dict_class_ActionModule['_connection'] is not None)
    assert (dict_class_ActionModule['_loader'] is not None)
    assert (dict_class_ActionModule['_play_context'] is not None)
    assert (dict_class_ActionModule['_shared_loader_obj'] is not None)
    assert (dict_class_ActionModule['_templar'] is not None)

# Generated at 2022-06-13 09:45:53.555362
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, {})

# Generated at 2022-06-13 09:46:00.640139
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize classes for testing
    # Templates are created from this path
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader
    from ansible.plugins.callback import CallbackBase
    import ansible.constants as C
    import sys


# Generated at 2022-06-13 09:46:09.289577
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create instance of class ActionModule
    a = ActionModule()

    # Create object for AnsibleOptions
    AnsibleOptions = type('AnsibleOptions', (), {})
    opt = AnsibleOptions()

    # Create object for AnsibleTask
    AnsibleTask = type('AnsibleTask', (), {})
    t = AnsibleTask()

    # Create object for AnsiblePlay
    AnsiblePlay = type('AnsiblePlay', (), {})
    p = AnsiblePlay()

    # Create object for AnsibleRunner
    AnsibleRunner = type('AnsibleRunner', (), {})
    r = AnsibleRunner()

    # Create object for AnsibleModule
    AnsibleModule = type('AnsibleModule', (), {})
    m = AnsibleModule()

    # Create object for ModuleResult

# Generated at 2022-06-13 09:46:10.220952
# Unit test for constructor of class ActionModule
def test_ActionModule():
    return True

# Generated at 2022-06-13 09:46:19.297464
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action_module = ActionModule(
        task=dict(args={'msg': 'Hello world!'}),
        connection=None,
        play_context={},
        loader=None,
        templar=None,
        shared_loader_obj=None)
    # test the __init__ function of class ActionModule
    assert test_action_module is not None
    assert test_action_module.transfers_files is False
    assert test_action_module.VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))

# Generated at 2022-06-13 09:46:19.795743
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:46:30.904329
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import PluginLoader

    # get a loaded ActionBase class for test
    class_ = PluginLoader.get_plugin(ActionBase)
    # construct a test object of ActionBase from the loaded class, with arguments
    obj = class_(task=None, connection=None, play_context=PlayContext(), loader=DataLoader(), templar=None, shared_loader_obj=None)
    # create a temp result dict
    result = dict()

    # test

# Generated at 2022-06-13 09:46:39.434938
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test ActionModule.run method
    """
    ####################
    # Test the scenario, when neither 'msg' nor 'var' argument is specified
    # in the task.
    ####################
    module = ActionModule()
    task = {
        'args': {},
        'action': 'debug'
    }
    module._task = task
    module._task.action = 'debug'
    module._display = MockDisplay()
    res = module.run(None, {})
    assert 'msg' in res, "No 'msg' key in the returned result"
    assert res['msg'] == 'Hello world!', "Unexpected 'msg' value: %s" % res['msg']

    ####################
    # Test the scenario, when 'msg' argument is specified
    # in the task.
    ####################



# Generated at 2022-06-13 09:46:44.341591
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = {}
    task = {'args':{}}
    tmp = 0
    task_vars = {}
    am = ActionModule(task, tmp, task_vars)
    # test run
    am.run()

if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 09:46:54.954875
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.network import Network
    from ansible.module_utils.facts.virtual.base import Base
    from ansible.module_utils.facts.virtual.lspci import Lspci
    from ansible.plugins.strategy.linear import StrategyModule

    options = dict(gather_facts='no', verbosity=3)
    play_context = PlayContext(options=options, become_method='sudo')
    task = Task()

# Generated at 2022-06-13 09:47:08.439935
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''
    # TODO: This test needs to be implemented
    assert False


# Generated at 2022-06-13 09:47:10.420288
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule(1, 2, 3)
    assert isinstance(x, ActionBase)

# Generated at 2022-06-13 09:47:14.675178
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Execute a simple test to check if method run is working as expected
    module = ActionModule()
    module._task = {'args': {'msg': 'Hello world!'}}
    assert module.run() == {
        'changed': False,
        '_ansible_verbose_always': True,
        'failed': False,
        'msg': 'Hello world!'
    }


# Generated at 2022-06-13 09:47:21.107345
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

    #Verbosity threshold is met and the output of msg is Hello world!
    results = module.run(task_vars={'verbosity': 3})
    assert results['failed'] == False
    assert results['changed'] == False
    assert results['msg'] == 'Hello world!'

    #Verbosity threshold is not met and the output of msg is skipped
    results = module.run(task_vars={'verbosity': 2})
    assert results['failed'] == False
    assert results['changed'] == False
    assert results['skipped_reason'] == 'Verbosity threshold not met.'
    assert results['skipped'] == True

# Generated at 2022-06-13 09:47:21.728310
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:47:24.585263
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task=dict(args=dict()),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 09:47:33.946070
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import pytest
    from ansible.plugins.action.debug import ActionModule
    from ansible.template.template import Templar
    from ansible.vars.hostvars import HostVars
    class FakeTask(object):
        def __init__(self):
            self.args = dict()
    class FakeVariableManager(object):
        def __init__(self):
            self.hostvars = HostVars()
        def get_vars(self):
            return self.hostvars
    class FakeDisplay(object):
        def __init__(self):
            self.verbosity = 1
    class FakeOptions(object):
        verbosity = 3
    class FakeTemplar(object):
        def __init__(self):
            pass

# Generated at 2022-06-13 09:47:37.338633
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test_object is an instance of class ActionModule
    #test_object = ActionModule()
    #test_object.run()
    print("test_ActionModule_run")
    return

# Generated at 2022-06-13 09:47:38.253888
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 09:47:46.251569
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.module_utils.six import StringIO
    from ansible.utils.display import Display
    from ansible.utils.color import ANSIBLE_COLOR, stringc
    from ansible import constants
    import json

    _task = {'args': {} }

    # Test with no arguments (default)
    action = action_loader.get('debug', task=_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    display = Display()
    action._display = display
    result = action.run(None, None)

    assert result['msg'] == u'Hello world!'
    assert result['_ansible_verbose_always'] is True
    assert result['failed'] is False

    # Test

# Generated at 2022-06-13 09:48:10.405288
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module=ActionModule()
    assert(isinstance(action_module,ActionModule))

# Generated at 2022-06-13 09:48:11.933559
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass  # Nothing to test

# Generated at 2022-06-13 09:48:21.819985
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Construct an object of class ActionModule
    module = ActionModule()

    # Arrange: Set task.args
    task = object()
    setattr(task, 'args', {'msg': None, 'var': 'foo', 'verbosity': 0})

    # Arrange: Set task.tmpdir
    tmpdir = object()
    setattr(task, 'tmpdir', tmpdir)

    # Arrange: Set task.vars
    task_vars = {'foo': 'bar'}

    # Act: Call method run
    actual = module.run(task_vars=task_vars, tmp=tmpdir)

    # Assert
    expected = {'foo': 'bar', 'failed': False}
    assert actual == expected

# Generated at 2022-06-13 09:48:31.306506
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.debug import ActionModule
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.process.worker import WorkerProcess
    import ansible.constants as C
    from ansible.utils.display import Display
    import ansible.playbook.task as task
    import ansible.playbook.block as block
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # initialize needed objects
    loader = DataLoader()

# Generated at 2022-06-13 09:48:39.346997
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test constructor for ActionModule
    '''
    try:
        from ansible.module_utils.basic import AnsibleModule
    except ImportError:
        print("failed=True msg='module basic import failed'")

    module = AnsibleModule(
        argument_spec={'msg': {'required': True, 'type': 'str'},
                       'var': {'required': False, 'type': 'str'},
                       'verbosity': {'required': False, 'type': 'int', 'default': 0}}
    )

    am = ActionModule(module, {})
    print("result={{'msg':'Hello world!', 'failed':False}}")
    print("changed=False")

# Generated at 2022-06-13 09:48:46.451929
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #Create instance of ActionModule class
    actionmodule_obj = ActionModule(action=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    
    # Mock the required object
    task_obj = MagicMock()
    task_obj.args = {}
    actionmodule_obj._task=task_obj
    display_obj = MagicMock()
    display_obj.verbosity = 0
    actionmodule_obj._display = display_obj
    templar_obj = MagicMock()
    actionmodule_obj._templar=templar_obj
    argument_dict = {}
    
    # Set default values
    result = dict(skipped=False, failed=False, changed=False)

# Generated at 2022-06-13 09:48:52.570860
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.debug import ActionModule as Cls
    import types
    x = Cls(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert x._task.__class__.__name__ == 'Task'
    assert x._play_context.__class__.__name__ == 'PlayContext'
    assert x._shared_loader_obj.__class__.__name__ == 'DataLoader'


# Generated at 2022-06-13 09:49:05.796690
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    test_json = """
    {
    "playbook_dir": "/Users/nikita.tolstikov/Documents/Code/ansible-testing",
    "stdout": [
        "Hello world!"
    ],
    "verbosity": 0,
    "_ansible_verbose_always": true,
    "_ansible_no_log": false,
    "changed": false,
    "failed": false,
    "invocation": {
        "module_args": {
            "verbosity": 0
        },
        "module_name": "debug"
    }
}
"""

# Generated at 2022-06-13 09:49:11.257467
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    my_play_context = PlayContext()
    my_play_context.remote_addr = '127.0.0.1'
    my_display = DummyDisplay()
    my_task = Task()
    my_task.args = {'msg': 'Hello world!', 'verbosity': 0}
    my_variable_manager = VariableManager()
    my_action_plugin = ActionModule(my_task, my_play_context, my_display, my_variable_manager)
    result = my_action_plugin.run()
    assert (result['msg'] == 'Hello world!')
    assert (result['failed'] == False)


# Generated at 2022-06-13 09:49:22.162326
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import context
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager

    config = context.CLIARGS
    config['verbosity'] = 2
    context._init_global_context(config)
    display = Display()
    variable_manager = VariableManager()

    # test when no option
    task = {'args': {}}
    action = ActionModule(task, {})
    result = action.run(None, {})
    assert result['failed'] is False
    assert result['skipped'] is False
    assert result['skipped_reason'] is None
    assert result['_ansible_verbose_always'] is True
    assert result['msg'] == 'Hello world!'

    # test for verbosity=1
    task = {'args': {'verbosity': 1}}

# Generated at 2022-06-13 09:50:18.057872
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Arrange
    am = ActionModule(None)
    am._task = mock.Mock()
    am._task.args = {}
    am._task.args['verbosity'] = 0
    am._task.args['msg'] = "test msg"
    am._display = mock.Mock()
    am._display.verbosity = 0
    am._templar = mock.Mock()
    # Act
    result = am.run(None, None)
    # Assert
    assert(result['failed'] == False)
    assert(result['msg'] == "test msg")



# Generated at 2022-06-13 09:50:21.058075
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.debug import ActionModule
    t = ActionModule('test', 'action', {})
    assert t.add_args == {}

# Generated at 2022-06-13 09:50:22.226182
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Check that you can create an object of ActionModule'''

    action_module = ActionModule()
    assert action_module

# Generated at 2022-06-13 09:50:27.994104
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # test with verbosity greater than 0
    mock_task = Mock()
    mock_task.args = {'var':'foobar', 'verbosity':1}
    mock_task_vars = {}

    obj = ActionModule()
    obj._task = mock_task
    obj._templar = Mock()
    obj._display = Mock()
    obj._display.verbosity = 0

    result = obj.run(task_vars=mock_task_vars)
    
    # assertion
    if result['_ansible_verbose_always'] and result['str'] == "VARIABLE IS NOT DEFINED!":
        print("Successfully test making request with verbosity greater than 0")
    else:
        print("Failed to test making request with verbosity greater than 0")


# Generated at 2022-06-13 09:50:40.545908
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.debug import ActionModule
    from ansible.module_utils.six import StringIO
    from ansible.action import ActionModule
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task_include import TaskInclude

    # initialize a task
    task = TaskInclude()
    task.action = 'debug'

    # initialize a ActionModule
    action_plugin = action_loader.get('debug', task, Connection())
    am = ActionModule(task, connection=Connection(), play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None)

    # initialize an ansible result
    result = AnsibleResult()

    # set task args
    task_args = {"msg": "Test ActionModule.run method."}
    task.args = task

# Generated at 2022-06-13 09:50:44.780892
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module.TRANSFERS_FILES == False
    assert action_module._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))
    assert not action_module.run()

# Generated at 2022-06-13 09:50:54.317609
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.facts import FactCollector

    class MyTaskQueueManager(TaskQueueManager):
        def __init__(self, inventory, variable_manager, loader, options, passwords, stdout_callback=None):
            self._stdout_callback = stdout_callback

# Generated at 2022-06-13 09:50:59.682079
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.block import Block

    test_task = Task()
    test_task._role = IncludeRole()
    test_task._block = Block()

    test_action_module = ActionModule(task=test_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    print(dir(test_action_module))
    print(repr(test_action_module))
    print(test_action_module)
    print(test_action_module.run())

if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 09:51:05.815926
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Constructor: test_ActionModule()
    Purpose:     To test the constructor of class ActionModule
    Parameters:  None
    Returns:     Nothing
    Example:     test_ActionModule()
    '''
    def __init__(self):
        '''
        Constructor: __init__
        Purpose:     Constructor of class ActionModule
        Parameters:  None
        Returns:     Nothing
        Example:     __init__()
        '''
        pass


# Generated at 2022-06-13 09:51:09.719139
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert action

# Generated at 2022-06-13 09:53:28.115000
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import copy, json
    from ansible.plugins.action.debug import ActionModule
    original_task_args = dict(msg='bar')
    original_task_vars = dict(foo='bar')
    original_tmp = "/tmp/foo"

    am = ActionModule(task=copy.deepcopy(original_task_args), connection=None,
            play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = am.run(task_vars=original_task_vars, tmp=original_tmp)
    assert result['msg'] == 'bar', 'msg in task args should be returned'
    assert result['failed'] is False, 'failed flag should be False'

    original_task_args = dict(var=dict(foo='bar'))

# Generated at 2022-06-13 09:53:36.531240
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock of class
    class Mock_ModuleLoader():
        pass

    mock_loader = Mock_ModuleLoader()

    # mock of class
    class Mock_Display():
        def __init__(self):
            self.verbosity = 0

    mock_display = Mock_Display()

    # mock of class
    class Mock_Templar():
        def __init__(self):
            pass

        def template(self, var, convert_bare=True, fail_on_undefined=True):
            if var == "{{var}}":
                return "var"
            elif var == "var":
                return "var"
            else:
                raise AnsibleUndefinedVariable

    mock_templar = Mock_Templar()

    # mock of class

# Generated at 2022-06-13 09:53:37.413974
# Unit test for constructor of class ActionModule
def test_ActionModule():
	actionmodule = ActionModule()
	assert actionmodule

# Generated at 2022-06-13 09:53:48.979376
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test constructor with valid arguments
    action = ActionModule(
        task=dict(args=dict(verbosity=0, msg="Hello world!")),
        connection=dict(),
        play_context=dict(check_mode=False),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    assert action is not None

    # Test constructor with invalid arguments
    try:
        action = ActionModule(
            task=dict(args=dict(verbosity=None, msg="Hello world!")),
            connection=dict(),
            play_context=dict(check_mode=False),
            loader=dict(),
            templar=dict(),
            shared_loader_obj=dict()
        )
        assert False, "Should fail because of undefined verbosity"
    except TypeError:
        pass

# Generated at 2022-06-13 09:53:57.629835
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #import pdb; pdb.set_trace()
    action = ActionModule()
    # Parameter 'msg' has value and 'var' has no value, so _task.args will be
    # {'msg': 'hello world', 'verbosity': 0}
    action._task.args['msg'] = 'hello world'
    action._task.args['verbosity'] = '0'
    # Compare the result and expected result. This test case is passed.
    assert action.run() == {"failed": False, '_ansible_verbose_always': True, '_ansible_no_log': False, 'msg': 'hello world'}

    # Parameter 'msg' has no value and 'var' has value, so _task.args will be
    # {'var': 'my_var', 'verbosity': 0}
    del action

# Generated at 2022-06-13 09:53:58.235566
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 09:54:06.305925
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    This method tests the 'run' method of class ActionModule.
    """
    # TODO:
    #    - Complete this unit test.
    # References:
    #    - http://docs.pytest.org/en/latest/
    #    - https://pytest-cov.readthedocs.io/en/latest/
    #    - https://docs.pytest.org/en/latest/example/simple.html#incremental-testing-test-steps
    #    - http://pythontesting.net/framework/pytest/pytest-introduction/
    #    - http://www.drdobbs.com/testing/using-pytest-for-blackbox-and-whitebox/240168251
    #    - http://pytest.org/latest/capture.html
    #

# Generated at 2022-06-13 09:54:18.498009
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.parsing.vault import VaultLib

    # Create a new instance of ActionModule
    am = ActionModule(None, None)

    # Set _task of am object to a mock object
    am._task = Mock()

    # Set _display of am object to a mock object
    am._display = Mock()
    am._display.verbosity = 0

    # Set _templar of am object to a mock object
    am._templar = Mock()
    am._templar.template.return_value = "VARIABLE IS NOT DEFINED"

    # Set VaultLib._get_encryption_key of am._templar.vault_secrets to a mock object
    am._templar.vault_secrets = VaultLib(None)
    am._templar.vault_secrets._

# Generated at 2022-06-13 09:54:19.015151
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:54:21.917807
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)