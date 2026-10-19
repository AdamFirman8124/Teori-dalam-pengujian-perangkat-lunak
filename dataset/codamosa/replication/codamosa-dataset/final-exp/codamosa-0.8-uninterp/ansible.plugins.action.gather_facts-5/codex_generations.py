

# Generated at 2022-06-13 09:55:37.129773
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Define test parameters and run test"""
    test_host = "testhost"
    test_loader = "test_loader"
    test_templar = "test_templar"
    test_shared_loader_obj = "test_shared_loader_obj"
    test_play_context = "test_play_context"
    test_task_keys = "test_task_keys"
    test_connection = "test_connection"
    test_tmp = "test_tmp"
    test_task_vars = "test_task_vars"
    test_tmp_path = "test_tmp_path"
    test_modules = ['aix']
    test_parallel = True
    test_result = dict()
    test_result['ansible_facts'] = dict()


# Generated at 2022-06-13 09:55:38.729675
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod_action = ActionModule()
    assert mod_action is not None

# Generated at 2022-06-13 09:55:49.918151
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Execution module test
    module = ActionModule()
    module_path = 'ansible/test/test_ActionModule_run.py'

    # Update values of module object.

# Generated at 2022-06-13 09:55:56.188717
# Unit test for constructor of class ActionModule
def test_ActionModule():

    class ShellMock():
        tmpdir = '/some/tmp/dir'
    class ConnectionMock():
        _shell = ShellMock()
        _load_name = 'a_load_name_mock'
    class TaskMock():
        _parent = {'_play': {'_action_groups': []}}
        module_defaults = None
        def __init__(self):
            self.args = {'a_mock_arg': 'a_mock_value'}
        collections = []
    class SharedMock():
        module_loader = None

    ActionModule(TaskMock(), ConnectionMock(), SharedMock())

# Generated at 2022-06-13 09:55:57.314862
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert len(vars(ActionModule)) > 0

# Generated at 2022-06-13 09:56:08.680848
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_case = {
    'ansible_facts': {},
    'ansible_facts_gathered': True,
    'ansible_verbose_override': True,
    'failed': True,
    'failed_modules': {'test_module': {'failed': True, 'invocation': {'module_args': {'test_arg': 'test'}}, 'msg': 'This is a test failure'}},
    'msg': 'The following modules failed to execute: test_module\n'
    }

    # Note that the method is tested indirectly by calling setup_facts in connection/__init__.py:
    # C.config.get_config_value(...) in BaseConnection._load_name resolves to 'smart'
    # For this test, we use the 'smart' return value as the input
    # Alternatively, we can

# Generated at 2022-06-13 09:56:15.373518
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    task_vars = dict()

    set_module_args(dict())

    my_obj = ActionModule(load_fixture('setup_module.yaml'), task_vars=task_vars)

    with pytest.raises(Exception) as excinfo:
        my_obj.run(task_vars=task_vars)
    assert '_ansible_facts_gathered' in str(excinfo.value)

# Generated at 2022-06-13 09:56:16.271516
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:56:16.904449
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:56:27.379817
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a Fake task
    task = dict(
        name = "Gather Facter facts",
        action = dict(
            module = "setup",
            args = dict()
        ),
        async_val = 0,
        delegate_to = None,
        delegate_facts = None,
        environment = None,
        local_action = None,
        run_once = None,
        tags = ["_raw_params"]
    )
    task_vars = dict()

    # Create object for class ActionModule with parameter task and task_vars
    actmod = ActionModule(task, task_vars)

    # Check if instance variable _task is properly set
    assert actmod._task == task
    
    # Create a Fake task

# Generated at 2022-06-13 09:56:43.137980
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor of class AnsibleModule
    action_module = ActionModule(None, None)
    assert action_module.__class__.__name__ == 'ActionModule'
    assert action_module.__module__ == 'ansible.plugins.action.setup'


# Generated at 2022-06-13 09:56:44.431062
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, None, None)
    assert a is not None

# Generated at 2022-06-13 09:56:45.404709
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert callable(ActionModule)


# Generated at 2022-06-13 09:56:54.824691
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    from ansible.plugins.action import ActionModule
    from ansible.plugins.loader import cli
    import ansible.utils.plugin_docs
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import merge_hash
    import ansible.utils.vars
    from ansible.executor.module_common import get_action_args_with_defaults
    import ansible.plugins.action.setup as action_setup
    import ansible.plugins.action.copy as action_copy
    import ansible.plugins.action.file as action_file
    import ansible.plugins.action.template as action_template
    import ansible.plugins.action.win_get_url as action_win_get_

# Generated at 2022-06-13 09:56:59.208744
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ansible_module = ActionModule()

    # Check if ansible_facts_parallel is None and modules is more than 1. Check whether parallel is true or not
    result = ansible_module.run(None, {"ansible_facts_parallel": None, "modules": ["test1", "test2"]})
    assert result['ansible_facts']['_ansible_facts_gathered']

# Generated at 2022-06-13 09:57:12.613420
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Runner():
        def __init__(self):
            self.tqm = sys.modules["ansible.utils.display"].Display()
            self.plugins = AnsiblePluginCollection()
            self.connection = Connection()


# Generated at 2022-06-13 09:57:23.668495
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    # class TaskQueueManager():
    # def __init__(self, hosts, inventory, variable_manager, loader, options, passwords, stdout_callback=None, run_additional_callbacks=True, run_tree=False, settings=None, stdout_callback=None, run_additional_callbacks=True, run_tree=False, settings=None, **kwargs
    hosts = ""
    inventory = ""
    variable_manager = VariableManager()
    loader = ""

# Generated at 2022-06-13 09:57:34.672550
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule()
    dict_test = {'ansible_facts': {},
                 'deprecations': [],
                 'failed': False,
                 'failed_modules': {},
                 'msg': '',
                 'skipped': True,
                 'skipped_modules': {'setup': {'ansible_facts': {},
                                               'ansible_job_id': '7223797520001586300',
                                               'changed': False,
                                               'failed': False,
                                               'results_file': '/home/test/.ansible/tmp/ansible-local-23890H8MAt/ansible-tmp-1584186613.7769755-2615-103568775401092/setup',
                                               'warnings': []}},
                 }
   

# Generated at 2022-06-13 09:57:37.268393
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    os.environ["ANSIBLE_CONFIG"] = "../examples/ansible.cfg"

    am = ActionModule()
    assert am is not None



# Generated at 2022-06-13 09:57:45.804726
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_self = MockActionModule()
    facts_module = ['smart', 'a', 'b', 'c']
    task_vars = dict(ansible_facts_parallel=True, ansible_network_os='ios')
    result = dict()
    result['ansible_facts'] = dict()
    result['ansible_facts']['_ansible_facts_gathered'] = True
    result['_ansible_verbose_override'] = True
    mock_self._task.args = dict(network_os='ios', network_os_vendor='cisco')
    mock_self._connection._load_name = 'test_network_os'

# Generated at 2022-06-13 09:58:10.085287
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 09:58:20.931498
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Mock values to build up a test "ActionModule" object
    mock_task_vars = {
        '_ansible_no_log': False,
        'ansible_check_mode': False,
        'ansible_facts': {'_ansible_facts_gathered': True},
        'ansible_loop_var': 'item',
        'ansible_module_name': 'setup',
        'ansible_module_args': 'filter=*',
        'ansible_module_name': 'setup',
        'ansible_module_name': '',
        'ansible_module_name': '',
        'ansible_module_name': '',
        'ansible_module_name': '',
    }


# Generated at 2022-06-13 09:58:22.610780
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts import FactCollector
    fact_collector = FactCollector(None, None)
    assert fact_collector.get_facts() is None

# Generated at 2022-06-13 09:58:34.252439
# Unit test for constructor of class ActionModule
def test_ActionModule():

    args = {
        'a': 1,
        'b': 2,
    }

    test_task = object()
    test_task_args = object()
    test_task_vars = object()

    test_all_vars = object()

    test_connection = object()
    test_play_context = object()
    test_loader = object()
    test_templar = object()
    test_shared_loader_obj = object()

    test_task_copy = {
        'async': 42,
        'notify': [],
        'poll': 0,
        'other': 'value',
    }

    # create the original action and then create a new ActionModule from it

# Generated at 2022-06-13 09:58:41.785694
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # NOTE: these tests are specific to the default 'setup' module, not to any
    # specific plugin, to test the core functionality of setup modules.
    from ansible.plugins.loader import action_loader

    import pytest  # noqa: F401

    # test invalid runner tasks
    action = action_loader.get('setup', class_only=True)
    action = action()
    action.datastructure = {'ansible_facts': {}}
    assert action.run() == {'ansible_facts': {}, 'failed': True, 'msg': "Invalid task given, the 'setup' action cannot be run directly"}

    # test valid runner tasks
    action = action_loader.get('setup', class_only=True)
    action = action()
    action._task.action = 'setup'

# Generated at 2022-06-13 09:58:42.556804
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    m.run()

# Generated at 2022-06-13 09:58:45.424196
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, '_get_module_args')
    assert hasattr(ActionModule, '_combine_task_result')
    assert hasattr(ActionModule, 'run')

# Generated at 2022-06-13 09:58:54.146849
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create mock of class ActionBase
    AB_obj = ActionBase()
    # set attributes of object AB_obj
    AB_obj.task = Mock()
    AB_obj.task_vars = {}
    # create mock of class AnsibleOptions
    AO_obj = Mock()
    # set attributes of object AO_obj
    AO_obj.module_defaults = {}
    
    # mock default options
    C.DEFAULT_MODULE_DEFAULTS = {}
    # mock config
    C.config = Mock()

    # call method run of object AB_obj
    AB_obj.run(tmp=None, task_vars=None)


# Generated at 2022-06-13 09:58:57.431068
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run")
    tmp = None
    task_vars = None
    action = ActionModule(tmp, task_vars)
    print(action.run())


test_ActionModule_run()

# Generated at 2022-06-13 09:59:06.169721
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Unit test for method run of class ActionModule

    # Set up and test data
    import ansible.plugins.action as action
    import ansible.plugins.action.setup as setup
    import ansible.plugins.action.setup_legacy as setup_legacy
    import ansible.plugins.action.copy as copy
    import ansible.plugins.action.file as file
    import ansible.plugins.action.yum as yum
    import ansible.plugins.action.package as package
    import ansible.plugins.action.seboolean as seboolean
    import ansible.plugins.action.win_reboot as win_reboot
    import ansible.plugins.action.script as script
    import ansible.plugins.action.service as service
    import ansible.plugins.action.raw as raw
    import ansible.module_

# Generated at 2022-06-13 09:59:59.718199
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mdl = ActionModule(None, None)
    mdl._shared_loader_obj.module_loader.find_plugin_with_context('ping', collection_list=['ansible.legacy'])
    mdl._task.args = {'data': 'value'}
    mdl.run({}, {})

# Generated at 2022-06-13 10:00:02.908943
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Arrange
    from ansible.executor.task_result import TaskResult

    t_mock = TaskResult()
    am_mock = ActionModule()

    # Act
    # nothing to do, just check no error is raised

    # Assert
    assert (am_mock.run(tmp=None, task_vars=None) == t_mock)

# Generated at 2022-06-13 10:00:03.537527
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:00:05.079771
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    m.C = C
    m.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:00:12.215719
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test constructor of ActionModule with default values of all arguments
    module = ActionModule(
        task=dict(name='test task',
                  action=dict(module='test_action_module',
                              args=dict(test='test value'),
                              )
                  )
    )
    # Test constructor of ActionModule with static values of all arguments
    assert module._task.action == dict(module='test_action_module',
                                       args=dict(test='test value'),
                                       )
    assert module._task.args == dict(test='test value')
    assert module._task._role is None
    assert module._task._role_params is None
    assert module._task._role_path is None
    assert module._task._play is None
    assert module._task._play_context is None
    assert module._task._parent is None


# Generated at 2022-06-13 10:00:22.425554
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Comparative validation of the output of run() method for ActionModule class
    obj = ActionModule()
    result = obj.run()
    assert result.get('ansible_facts') == {'_ansible_facts_gathered': True}
    assert result.get('msg') == 'The following modules failed to execute: ansible.legacy.setup\n'
    assert result.get('failed') == True

# Generated at 2022-06-13 10:00:29.540750
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create instance of class ActionModule
    action_module = ActionModule(
        task=dict(
            args={'ansible_facts_parallel': None, 'parallel': None, 'network_os': None}
        ),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    # return the result of method run
    return action_module.run()



# Generated at 2022-06-13 10:00:37.388400
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Mocking the load_module
    import sys
    import collections
    sys.modules['ansible.plugins.action'] = collections.Mock()

    # Mocking the _supports_check_mode
    sys.modules['ansible.plugins.action'].ActionBase = collections.Mock()
    sys.modules['ansible.plugins.action'].ActionBase._supports_check_mode = collections.Mock()

    # Mocking the _execute_module
    sys.modules['ansible.plugins.action'].ActionBase._execute_module = collections.Mock()
    sys.modules['ansible.plugins.action'].ActionBase._execute_module.return_value = {'msg': 'Execute_module has ran'}

    from ansible.plugins.action.setup import ActionModule

    # Getting the instance for ActionModule class
   

# Generated at 2022-06-13 10:00:42.505930
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.setup import ActionModule
    action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )
    assert action_module

# Generated at 2022-06-13 10:00:44.921176
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    result = ActionModule(Task(), None, None)
    assert result is not None

# Generated at 2022-06-13 10:02:29.954212
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act = ActionModule()
    assert act is not None



# Generated at 2022-06-13 10:02:36.701780
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = 'testhost.example.com'
    connection = 'ansible.netcommon.network_cli'
    play_context={'verbosity': 0, 'check_mode': False, 'network_os': 'junos'}
    play_source={'play': 'play', 'name': 'name',
                 'hosts': 'hosts', 'become': True, 'become_method': 'become_method',
                 'become_user': 'become_user', 'remote_user': 'remote_user',
                 'vars': 'vars'}
    loader = 'loader'
    templar = 'templar'
    shared_loader_obj = 'shared_loader_obj'

# Generated at 2022-06-13 10:02:45.551421
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._add_cleanup_file = MagicMock()
    action_module._task = MagicMock()
    action_module._task.args = {'filter': None, 'gather_subset': 'all',
                                'gather_timeout': None}
    action_module._task.action = 'setup'
    action_module._task.async_val = 0
    action_module._play_context = MagicMock()
    action_module._play_context.connection = 'network_cli'
    action_module._play_context.become = False
    action_module._play_context.become_method = None
    action_module._play_context.become_user = None
    action_module._connection = MagicMock()
    action_module._connection._shell

# Generated at 2022-06-13 10:02:52.232271
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # init the variables needed to create an ActionModule
    # temp_loader is not being used for anything
    temp_loader = None
    # shared_loader is not being used for anything
    shared_loader = None
    # variable_manager is not being used for anything
    variable_manager = None
    # display is not being used for anything
    display = None
    # Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check'])
    # options is not being used for anything
    options = None
    # action_base = ActionBase(temp_loader, shared_loader, variable_manager, display, options)
    # action_base is not being used for anything
    action_base = None
    # task_executor = TaskExecutor(temp

# Generated at 2022-06-13 10:03:00.685390
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Create an inclusion task
    task = TaskInclude()
    task._role = None

    module_result = {'ansible_facts': {'fact1': 'value1'}, 'changed': True}

    # Create a TaskQueueManager
    tqm = TaskQueueManager(inventory=None, variable_manager=None, loader=None, options=None, passwords=None, stdout_callback=None, run_additional_callbacks=None, run_tree=False, callback_plugins=None, result_callback_whitelist=[], result_callback=None)

    # Check that facts were gathered

# Generated at 2022-06-13 10:03:04.218161
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'ActionModule' in globals(), "ActionModule is not defined"
    assert callable(globals()['ActionModule']), "ActionModule is not a class"
    assert issubclass(ActionModule, object), "ActionModule is not a subclass of object"



# Generated at 2022-06-13 10:03:08.404171
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert not action_module.run()

# Generated at 2022-06-13 10:03:18.150138
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule(
        task=dict(
            action=dict(
                args=dict(
                    gather_subset=[],
                    gather_timeout=10,
                    filter=dict(),
                    ansible_facts_parallel=None,
                    parallel=None,
                ),
                module='setup',
            ),
        ),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict(),
    )

# Generated at 2022-06-13 10:03:22.281132
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(
            args=dict(),
        ),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert module is not None


# Generated at 2022-06-13 10:03:35.455546
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create mock object
    class MockModule:
        def __init__(self, module_loader, templar):
            self.module_loader = module_loader
            self.templar = templar

    # create mock object
    class MockTask:
        def __init__(self, module_defaults, connection):
            self.module_defaults = module_defaults
            self._parent = self
            self._play = self
            self._connection = connection

    # create mock object
    class MockTaskVars:
        def __init__(self, connection, task):
            self._connection = connection
            self._task = task

    # create mock object
    class MockConnection:
        def __init__(self, shell):
            self._shell = shell

    # create mock object