

# Generated at 2022-06-13 10:16:09.562050
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:16:13.782554
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule(None, None)._task.action == {})
    assert(ActionModule(None, None)._connection.has_native_async == None)
    assert(ActionModule(None, None)._task.async_val == None)
    assert(ActionModule(None, None)._supports_check_mode == True)
    assert(ActionModule(None, None)._supports_async == True)

# Generated at 2022-06-13 10:16:14.317246
# Unit test for constructor of class ActionModule
def test_ActionModule():
  a = ActionModule()

# Generated at 2022-06-13 10:16:15.822176
# Unit test for constructor of class ActionModule
def test_ActionModule():

    class ActionModuleTest(ActionModule):
        pass

    test = ActionModuleTest()
    assert True

# Generated at 2022-06-13 10:16:17.346142
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am._supports_checkmode
    assert am._supports_async

# Generated at 2022-06-13 10:16:27.228189
# Unit test for constructor of class ActionModule
def test_ActionModule():
	# Create a global variable "None"
	hostvars = None
	# Create an instance of class ActionBase()
	amodule = ActionBase()
	# Create an instance of class ActionModule()
	action_module = ActionModule()
	# Create an instance of class Task()
	task = Task()
	# Create an instance of class TaskExecutor()
	executor = TaskExecutor()
	# Create an instance of class Connection()
	connection = Connection()
	# Create an instance of class PlayContext()
	play_context = PlayContext()
	# Create an instance of class Playbook()
	playbook = Playbook()
	# Create an instance of class Play()
	play = Play()
	# Call method run on action_module object
	action_module.run(None, None)
	

# Generated at 2022-06-13 10:16:28.591971
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert isinstance(am, ActionBase)

# Generated at 2022-06-13 10:16:35.506979
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test ActionModule run()

    # Test 1: test fixture is loading correctly - run() should return nothing
    action_module = ActionModule(task=ModuleTest.task, connection=ModuleTest.connection,
                                 play_context=ModuleTest.play_context, loader=ModuleTest.loader,
                                 templar=ModuleTest.templar, shared_loader_obj=ModuleTest.shared_loader_obj)
    result = action_module.run(task_vars=ModuleTest.task_vars)
    assert result == None

# Generated at 2022-06-13 10:16:36.233636
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:16:40.725698
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class TmpModule:
        def __init__(self):
            self.argument_spec = dict()

    module = TmpModule()
    action_module = ActionModule(module, dict())
    assert action_module is not None

# Generated at 2022-06-13 10:16:47.424426
# Unit test for constructor of class ActionModule
def test_ActionModule():
   action_module_test = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, share_lock=None)
   assert action_module_test is not None


# Generated at 2022-06-13 10:16:48.692960
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module != None

# Generated at 2022-06-13 10:16:55.789679
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import unittest.mock as mock

    from ansible.plugins.action.normal import ActionModule as action_module
    from ansible.plugins.action.normal import ActionBase as action_base
    from ansible.utils.vars import merge_hash

    # expected result from action_base.run
    result = {
        'failed': False,
        'invocation': {
            'module_args': 'a_module_args',
            'module_name': 'a_module_name'
        }
    }

    # expected result from action_module.run
    result_2 = {
        'failed': False,
        'invocation': {
            'module_name': 'a_module_name'
        }
    }

    # expected result from action_module._execute_module

# Generated at 2022-06-13 10:17:08.573949
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.utils.vars import merge_hash
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    variable_manager = VariableManager()
    loader = DataLoader()
    results_callback = lambda x: None
    task = TaskResult(
        host=dict(name='test_host'),
        task=dict(
            role=dict(name=''),
            action=dict(name='debug'),
            args=dict(
                msg='test_message',
            ),
        ),
    )
    # Create an action object
    am = ActionModule(task, variable_manager=variable_manager, loader=loader, results_callback=results_callback)


# Generated at 2022-06-13 10:17:18.011514
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible
    task_vars = dict()
    tmp = None
    module = action_module.ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    module._configure_module = lambda: None
    module._display = lambda x, y: (x, y)
    module._execute_module = lambda x, y: {"abc": "def"}
    try:
        result = module.run(tmp, task_vars)
    except Exception as e:
        raise AssertionError("ActionModule_run method failed due to %s" % e)

# Generated at 2022-06-13 10:17:20.369681
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(connection=None,
                     task_vars=None,
                     disable_lookup=None)
    assert a is not None

# Generated at 2022-06-13 10:17:22.060060
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, None, None)
    assert action is not None

# Generated at 2022-06-13 10:17:28.053746
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._task = DummyTask()
    module._connection = DummyConnection()
    module._shared_loader_obj = DummySharedLoaderObj()
    module._loader = module._shared_loader_obj
    module._templar = DummyTemplar()
    module.runner_supports_async = False
    result = module.run(None, None)
    assert result == {'_ansible_verbose_override': True, 'changed': False, 'failed': False}


# Generated at 2022-06-13 10:17:33.085578
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Construct a class ActionModule object and pass possible
    arguments to the constructor.
    '''

    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module
    print(module)

# Generated at 2022-06-13 10:17:33.654855
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 1

# Generated at 2022-06-13 10:17:53.449483
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test 1
    n = ActionModule()
    assert n.module_args == {}
    assert n.module_name == 'command'
    assert n.async_val == 0
    assert n.async_seconds == 60
    assert n.module_name == 'command'
    assert n.module_args is None
    assert n.module_lang == 'python'
    assert n.become == False
    assert n.become_user == 'root'
    assert n.become_method == 'sudo'
    assert n.become_exe == None
    assert n.become_flags == ''
    assert n.become_ask_pass == True
    assert n.no_log_messages == ['become_password']
    assert n.delegate_to == None
    assert n.delegate_facts == False

# Generated at 2022-06-13 10:17:54.126697
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 10:17:59.282916
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup
    action_module = ActionModule()
    task_vars = {'surf': 'awesome', 'other': 'stuff'}
    action_module._task.async_val = '3600'
    action_module._task.action = 'setup'
    action_module._task.async_val = None
    
    action_module._task.action = 'ping'
    action_module._supports_check_mode = False
    action_module._supports_async = False
    action_module._connection.has_native_async = True
    result = {'skipped': False, 'invocation': {'module_args': 'surf'}}

    # expect
    result_execute_module = {'skipped': False, 'invocation': {}}

# Generated at 2022-06-13 10:18:00.716890
# Unit test for constructor of class ActionModule
def test_ActionModule():

    assert callable(ActionModule)


# Generated at 2022-06-13 10:18:02.704024
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    assert module.run() == None

# Generated at 2022-06-13 10:18:08.021864
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action
    actmod = ansible.plugins.action.ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert actmod is not None

# Generated at 2022-06-13 10:18:19.159815
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """test_ActionModule: constructor of class ActionModule"""
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.process.result import ResultProcess
    from ansible.executor.job_result import JobResult
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-13 10:18:20.040121
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action is not None

# Generated at 2022-06-13 10:18:28.248184
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    from ansible.utils.vars import merge_hash

    from ansible.module_utils._text import to_text
    from ansible.plugins.action.normal import ActionModule as Normal
    from ansible.plugins.action.normal import ActionModule as ActionModule
    from ansible.playbook.conditional import Conditional
    from ansible.playbook.task import Task
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from units.mock.executor import MockExecutor
   

# Generated at 2022-06-13 10:18:38.318768
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.utils.plugin_docs as plugin_docs
    import ansible.errors as errors

    am = ActionModule()
    assert am
    assert isinstance(am, ActionBase)

    # This test is only interesting with plugins compiled in, just skip
    # if that's not the case
    if not plugin_docs.HAS_BUILTIN_DOCUMENTATION:
        pytest.skip("no plugins compiled in, skipping")

    # Assert we get an exception for a non existent plugin
    with pytest.raises(errors.AnsibleError):
        am.__class__._load_action_plugin('not_there')


# Generated at 2022-06-13 10:19:00.371723
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # set up the basics needed for the task executor
    loader = action_loader
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()
    play_context.verbosity = 0
    play_context.connection = 'local'

    # create a task with a local action
    task = Task()
    task.action = 'setup'

# Generated at 2022-06-13 10:19:03.042348
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    t = Task()
    assert ActionModule(t, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:19:11.690038
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.normal import ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.parsing.dataloader import DataLoader

    # Create a mock task queue manager
    tqm = TaskQueueManager(loader=DataLoader(), inventory=None, variable_manager=None, loader_callback=None, results_callback=None, options=None, passwords=None, stdout_callback=None)
    # Create a mock playbook executor
    pe = PlaybookExecutor(playbooks=None, inventory=None, variable_manager=None, loader=None, options=None, passwords=None)
    # Create a mock task executor

# Generated at 2022-06-13 10:19:21.682975
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text
    import json
    import os
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    mock_loader = DataLoader()
    mock_connection = object()
    mock_play_context = PlayContext()
    mock_action = ActionModule('/path/to/action/plugins', object(), mock_loader, mock_play_context, '/dev/null', '/dev/null', connection=mock_connection)
    mock_module_args = dict(arg1='arg1value', arg2='arg2value')

    mock_action._task.async_val = 0

# Generated at 2022-06-13 10:19:22.333043
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a

# Generated at 2022-06-13 10:19:22.714045
# Unit test for constructor of class ActionModule
def test_ActionModule():
  am = ActionModule()

# Generated at 2022-06-13 10:19:24.449671
# Unit test for constructor of class ActionModule
def test_ActionModule():
    p = ActionModule()
    assert p._supports_check_mode is True
    assert p._supports_async is True

# Generated at 2022-06-13 10:19:25.768564
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == 'ActionModule'

# Generated at 2022-06-13 10:19:30.592949
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module = ActionModule()

    # Testing with async_val not set
    task = dict(
        async_val = False,
        async_timeout = 1
    )

    module._task = task

    module._connection = dict(native_async = True)

    module.run()

# Generated at 2022-06-13 10:19:35.721337
# Unit test for constructor of class ActionModule
def test_ActionModule():

    task = dict(
        action=dict(
            module=dict(
                name="a_module", 
                args=dict(arg1="1", arg2="2")
            )
        )
    )
    task_vars = dict()

    print("\nTest 1: Constructor:")
    am = ActionModule(task, task_vars)
    print("{}".format(vars(am)))

# Generated at 2022-06-13 10:20:01.864076
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    ActionModule.run()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # test_ActionModule_run()

# Generated at 2022-06-13 10:20:02.543567
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:20:17.010249
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    from ansible.plugins.action.normal import ActionModule
    from ansible.module_utils.basic import AnsibleModule

    class FakeModule(object):
        def __init__(self,**kwargs):
            self.__dict__.update(kwargs)
            FakeModule.called_args = kwargs

        def __call__(self, *args, **kwargs):
            FakeModule.called_args.update(kwargs)
            return FakeModule.result

    result = dict(changed=False, msg='failed')
    FakeModule.result = result
    C._MODULE_CACHE = {}
    C._TASK_PATH_CACHE = {}

# Generated at 2022-06-13 10:20:19.204076
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None

# Generated at 2022-06-13 10:20:20.462771
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:20:26.497675
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.plugins.action.normal as normal

    module_mock = AnsibleModule(
        argument_spec=dict(
            username=dict(type='str', required=True)
        )
    )

# Generated at 2022-06-13 10:20:34.159520
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Pick up from ansible/plugins/action/copy.py
    from ansible.plugins.action import clear_dir_nonexistent, ActionModule
    mod = ActionModule()
    # mod = ActionModule(connection=None, task_vars=None, tmp=None, delegate_to=None)
    assert mod is not None

    # Test _execute_module
    from ansible.plugins.action import ActionModule
    from ansible.compat.tests import mock
    from ansible.executor import module_common
    from ansible.executor.task_result import TaskResult
    from ansible. execution import context
    from ansible.executor.process.worker import WorkerProcess
    from ansible.vars import combine_vars
    from ansible.vars import VariableManager

    # Test constructor
    mod = ActionModule()
   

# Generated at 2022-06-13 10:20:35.506121
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    assert True


# Generated at 2022-06-13 10:20:46.081076
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play import Play
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import action_loader
    import ansible.constants as C
    import sys
    import os

    C.HOST_KEY_CHECKING = False
    loader = action_loader
    inv_mgr = InventoryManager(loader=loader, sources='localhost,')
    task_executor = TaskExecutor(inventory=inv_mgr, loader=loader)
    task_queue_manager = TaskQueueManager(inventory=inv_mgr, loader=loader, task_executor=task_executor, variable_manager=None, shared_loader_obj=None)
   

# Generated at 2022-06-13 10:20:46.664227
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:21:42.247818
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock task
    task = BaseTask()
    # Create a mock connection
    connection = BaseConnection()
    # Create a mock play
    play = BasePlay()
    # Create a mock loader
    loader = BaseLoader()
    # Create a mock VariableManager
    variable_manager = BaseVariableManager()
    # Create a mock templar
    templar = BaseTemplar()

    # Create mock action module
    action_module = ActionModule(task, connection, play, loader, variable_manager, templar)
    action_module.set_loader(loader)
    action_module.set_task(task)
    action_module.set_variable_manager(variable_manager)
    action_module.set_loader(loader)
    action_module.set_connection(connection)

    # Create mock task vars
   

# Generated at 2022-06-13 10:21:45.462541
# Unit test for constructor of class ActionModule
def test_ActionModule():
    foo = ActionModule()
    assert foo is not None

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:21:50.610423
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test for constructor of class ActionModule.
    """
    action = ActionModule("task", "connection", "play_context", "loader", "templar", "shared_loader_obj")
    assert action is not None

# Generated at 2022-06-13 10:22:00.788285
# Unit test for constructor of class ActionModule
def test_ActionModule():

    import ansible.playbook
    import ansible.inventory
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.executor.playbook_executor import PlaybookExecutor

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins.callback import CallbackBase

    # Create data load for ansible
    loader = DataLoader()

    # Create inventory and pass to var manager
    inventory = ansible.inventory.Inventory(loader=loader, variable_manager=VariableManager(), host_list=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # create datastructure that represents our play, including tasks, this is basically what our Y

# Generated at 2022-06-13 10:22:07.800431
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test with params
    a = ActionModule({'a':1},
                     frozenset(),
                     False,
                     'setup',
                     False,
                     None,
                     None,
                     'copy',
                     None,
                     True,
                     1,
                     'copy',
                     'copy',
                     'copy',
                     {'a':1},
                     None)
    assert a.action == 'copy'

# Generated at 2022-06-13 10:22:12.102596
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("TESTING ActionModule")
    # mock task to avoid running any code and use the constructor
    task = {"action":"ping"}
    connection = None
    newActionModule = ActionModule(task,connection)
    assert newActionModule != None
    print("PASSED ActionModule")

# Generated at 2022-06-13 10:22:20.445309
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C
    import sys
    
    if sys.version_info[:2] <= (2, 6):
        import unittest2 as unittest
    else:
        import unittest
        
    class TestActionModule(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_ActionModule_run(self):
            from ansible.playbook.play import Play
            from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-13 10:22:21.413540
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:22:22.191717
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass



# Generated at 2022-06-13 10:22:23.553135
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    if __name__ == "__main__":
        pass

# Generated at 2022-06-13 10:24:20.148086
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print(ActionModule())

# Generated at 2022-06-13 10:24:22.339849
# Unit test for method run of class ActionModule
def test_ActionModule_run():


    # test no arguments
    a = ActionModule()
    assert a.run() == {}

    # test empty arguments
    a = ActionModule()
    assert a.run(tmp="", task_vars={}) == {}

# Generated at 2022-06-13 10:24:27.048866
# Unit test for constructor of class ActionModule
def test_ActionModule():

    old_env = dict(os.environ)
    os.environ = dict()

    import ansible.plugins.action.normal

    mod = ansible.plugins.action.normal.ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())

    mod.run()
    assert mod.argspec
    assert mod.argument_spec
    assert mod.create_message
    assert mod.load_name
    assert mod.method

    x = ansible.plugins.action.normal.ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())

# Generated at 2022-06-13 10:24:27.835527
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None)
    assert a

# Generated at 2022-06-13 10:24:38.570108
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import ansible.plugins.action.normal
    assert ActionModule.run is not None
    assert ansible.plugins.action.normal.ActionModule.run is not None

    # create action_module instance
    action_module = ansible.plugins.action.normal.ActionModule(
        task=dict(action=dict(module_name='setup', module_args=dict())),
        connection=dict(host=dict(name='localhost')),
        play_context=dict(check_mode=False)
    )
    # run action_module method run
    result = action_module.run(tmp=os.path.join('/tmp', 'ansible'), task_vars={'test variable': 'test variable value'})
    # validate result
    assert result is not None
    assert isinstance(result, dict)
    assert result

# Generated at 2022-06-13 10:24:43.442684
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = 'ping'
    mock_task = {'action': 'ping'}
    mock_task_vars = {}
    mock_inject = {}
    mock_connection = 'local'
    action_module = ActionModule(task=mock_task, task_vars=mock_task_vars, inject=mock_inject, connection=mock_connection)
    assert action_module._task == mock_task
    assert action_module._task_vars == mock_task_vars
    assert action_module._inject == mock_inject
    assert action_module._connection == mock_connection
    assert action_module._module_name == module

# Generated at 2022-06-13 10:24:50.469904
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.module_utils.facts import Facts
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence
    from ansible.plugins.action.normal import ActionModule as ActionModuleNormal
    from ansible.utils.vars import merge_hash

    # Create a play context
    play_context = PlayContext()
    play_context.network_os = "ios"
    play_context.remote_addr = "10.0.0.1"
    play_context.accelerate = False
    play_context.passwords = {}
    play_context.port = 22
    play_context.remote_user = "vagrant"
    play_context.connection = "ssh"

# Generated at 2022-06-13 10:25:00.037656
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible
    from ansible import constants as C
    from ansible.utils.vars import merge_hash
    from ansible.plugins.action import ActionBase

    class ActionModule(ActionBase):
        def run(self, tmp=None, task_vars=None):

            result = super(ActionModule, self).run(self,tmp, task_vars)
            del tmp  # tmp no longer has any effect
            if not result.get('skipped'):

                if result.get('invocation', {}).get('module_args'):
                    # avoid passing to modules in case of no_log
                    # should not be set anymore but here for backwards compatibility
                    del result['invocation']['module_args']

                # FUTURE: better to let _execute_module calculate this internally?
                wrap_async = self._task

# Generated at 2022-06-13 10:25:07.220964
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    options = {'connection': 'local'}
    loader = None
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=None)
    play_context = PlayContext()
    task = Task(name='test_action_module', action=dict(module='win_ping'))
    action_module = ActionModule(task, play_context, variable_manager, loader, options=options)

    assert action_module._task.name == 'test_action_module'
    assert action_module._task.action['module'] == 'win_ping'

# Generated at 2022-06-13 10:25:16.454151
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class MockConnection():
        def __init__(self):
            self.has_native_async = False

    class MockTask():
        def __init__(self):
            self.async_val = False
            self.action = None
            self.async_val = False

    class MockVars():
        def __init__(self):
            self.vars = {}

    c = MockConnection()
    t = MockTask()
    v = MockVars()

    # call actionmodule with task and connection
    # FIXME: Make this test more robust
    a = ActionModule(c, t, 'module_name', 'module_path', v.vars)
    assert isinstance(a, ActionModule)