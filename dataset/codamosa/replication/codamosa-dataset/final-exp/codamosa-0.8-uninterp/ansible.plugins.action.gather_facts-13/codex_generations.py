

# Generated at 2022-06-13 09:55:36.253007
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 09:55:42.125662
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_queue_manager import TaskQueueManager
    execution_vars = dict(transport='local')
    task_vars = dict()
    task_queue_manager = TaskQueueManager(result_callback=None)
    action_base = ActionModule(execution_vars, task_vars, task_queue_manager)

# Generated at 2022-06-13 09:55:51.197248
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.utils.vars import load_extra_vars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils import basic

    play_context = PlayContext()
    play_context.become = False
    play_context.become_method = None

    play_context._succeeded = True
    play_context._failed = False

    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 09:55:53.496944
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module  = ActionModule({})
    assert action_module.__class__.__name__ == 'ActionModule'


# Generated at 2022-06-13 09:56:05.006242
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager

    task = Task()
    task._role = None
    task.action = 'setup'
    task.args = {'filter': '*'}
    task.deprecation_warnings = []
    task._parent = None
    task._play = None
    task._role = None
    task._loader = None
    task.collections = []

    # mock the action base class
    from ansible.plugins.action import ActionBase
    action_base = ActionBase()
    action_base._display = {'verbosity': 2}
    action_base._task = task
    action_base._templar = None
    action_base._shared_loader

# Generated at 2022-06-13 09:56:06.532645
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    mod.finalize()



# Generated at 2022-06-13 09:56:07.607873
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass


# Generated at 2022-06-13 09:56:16.387614
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Setup all of the test objects and stubs
    tmp = '/tmp/test'
    setup_action = ActionModule()
    setup_action._make_tmp_path = Mock()
    setup_action._make_tmp_path.return_value = tmp
    setup_action._remove_tmp_path = Mock()
    setup_action._execute_module = Mock()
    setup_action._execute_module.return_value = {
        'changed': False,
        'failed': False,
        'msg': 'Success',
        'results': [],
        'ansible_facts': {'ansible_distribution': 'Ubuntu'}
    }

    # Run the method under test
    setup_action.run()

    # Ensure the method calls are as expected
    setup_action._make_tmp_path.assert_called_once_with

# Generated at 2022-06-13 09:56:17.062525
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:56:18.371290
# Unit test for method run of class ActionModule
def test_ActionModule_run():
   action_module = ActionModule()
   assert True

# Generated at 2022-06-13 09:56:32.007691
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, {})
    a._get_module_args('setup', {})

# Generated at 2022-06-13 09:56:37.437085
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    task_vars = []
    result = action_module.run(task_vars=task_vars)
    assert result is not None
    assert result['failed'] is not None
    assert 'The following modules failed' in result['msg']
    assert 'FACTS_MODULES' in action_module._task.args

# Generated at 2022-06-13 09:56:47.422707
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    connection_mock = ConnectionMock()
    loader_mock = CollectionLoaderMock(collection_list=None)

    im = InventoryManager(loader=loader_mock, sources=[])
    vs = VariableManager()

    task = TaskMock(
        args={'parallel': None, 'gather_subset': None, 'gather_timeout': None, 'filter': None},
        module_defaults={},
        collections=None,
        connection=connection_mock,
        _parent=PlaybookMock(),
        _task=TaskMock(),
    )


# Generated at 2022-06-13 09:56:57.350320
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ansible_mock = AnsibleMock()
    ansible_mock.config.setting = 'setting'
    ansible_mock.config.facts_module = 'FACTS_MODULES'
    ansible_mock.config.connection_facts_modules = 'CONNECTION_FACTS_MODULES'
    ansible_mock.task.args = {'parallel': True}
    ansible_mock.task.collections = []
    ansible_mock.task.module_defaults = {}
    templar_mock = TemplarMock()
    action_module_mock = ActionModule(ansible_mock, templar_mock)
    result = action_module_mock.run('', {})

# Generated at 2022-06-13 09:57:05.491583
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class FakeActionBase(object):
        def __init__(self):
            self._supports_check_mode = None
            self._task = FakeTask()
            self._shared_loader_obj = FakeLoader()
            self._connection = FakeConnection()
            self._display = FakeDisplay()
            self._templar = FakeTemplar()

        def run(self, tmp, task_vars):
            return {}

        def _remove_tmp_path(self, path):
            pass

        def _execute_module(self, **kw):
            return {}


    class FakeConnection(object):
        def __init__(self):
            self._shell = FakeShell()
            self._load_name = "network_cli"


    class FakeTask(object):
        def __init__(self):
            self._parent = Fake

# Generated at 2022-06-13 09:57:06.441322
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

    assert module.run()



# Generated at 2022-06-13 09:57:08.647189
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Run a constructor test for ActionModule.
    :return:
    """

    assert isinstance(ActionModule(), ActionBase)

# Generated at 2022-06-13 09:57:15.663609
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_path = os.path.join(os.getcwd(), 'setup.py')
    # test to see if module is present at module path
    assert os.path.exists(module_path) is True
    # create an instance of ActionModule
    action_module = ActionModule()
    # set _execute_module function for testing
    action_module._execute_module = lambda module_name, module_args, task_vars, wrap_async: {'msg': 'MODULE_LOG_MSG'}
    action_module._task.args = {'parallel': True}
    action_module._task.module_defaults = dict()
    action_module._connection = MockConnection()
    action_module._shared_loader_obj = object()
    action_module._supports_check_mode = True
    action_module

# Generated at 2022-06-13 09:57:21.347110
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import connection_loader
    from ansible.vars.manager import VariableManager
    from units.mock.loader import DictDataLoader

    host = 'example.com'
    loader = DictDataLoader({
        host: dict(
            ansible_facts={},
            ansible_facts_parallel=None,
        ),
    })

    inventory = InventoryManager(loader=loader, sources='localhost')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = dict()


# Generated at 2022-06-13 09:57:21.737597
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 09:57:54.213799
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest

    actionModule = ActionModule(
        task = {
            'args': {
                'b': 'c'
            }
        },
        connection = None,
        play_context = None,
        loader = None,
        templar = None,
        shared_loader_obj = None
    )

    # test with arguments: tmp=None, task_vars=None
    # expected result: result = super(ActionModule, self).run(tmp, task_vars)
    result = actionModule.run(None, None)

    assert result == None

# Generated at 2022-06-13 09:58:01.914222
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader

    action = action_loader.get('setup')
    assert action.__class__.__name__ == 'ActionModule'
    assert action._supports_check_mode is True

    manager = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback=None
    )
    assert action._shared_loader_obj == manager._task_cache['loader']
    assert action._templar._available_variables == manager._task_cache['shared_loader_obj']._available_variables
    assert action._templar.environment == manager._task_cache['shared_loader_obj'].environment

# Generated at 2022-06-13 09:58:11.768250
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Testing ActionModule::run() ...'),

    # SETUP
    import ansible.plugins.action.setup as setup
    a = setup.ActionModule('setup', 'setup', True)
    a._task = MockTask()
    a._task._ds = {
        'other_variables': { 'ansible_facts': { 'fact1': 'some_data' } },
        'vars': { 'ansible_facts': { 'fact2': 'some_data2' } },
        'ansible_facts': { 'fact3': 'some_data3' }
    }
    a._supports_check_mode = True

    # TEST
    result = a.run(None, None)

    # VERIFY

# Generated at 2022-06-13 09:58:22.361824
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test to check whether method run of class ActionModule
    is working as expected.
    """

    from units.mock.loader import DictDataLoader

    from ansible.executor.task_result import TaskResult
    from ansible.executor.module_result import ModuleResult
    from ansible.executor.process.result import ResultProcessor
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    from units.mock.plugins.action import ActionBaseMock

    modules = ['ansible.legacy.smart_facts', 'ansible.legacy.setup']

    mock_task_vars = dict(
        ansible_facts=dict(
            network_os='junos'
        )
    )

   

# Generated at 2022-06-13 09:58:23.488391
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # assert for constructor of class ActionModule
    assert 1 == 1

# Generated at 2022-06-13 09:58:30.184612
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    runtime_data = {'groups': {'all': 'all'}, 'hostvars': {'all': 'all', 'localhost': {}}}

    # Test with no module set in FACTS_MODULES
    setup = ActionModule({'setup': 'setup'}, {'task': {'args': {}, 'action': 'setup', 'collections': ['col1', 'col2'], 'module_defaults': {'param1': 'param1'}}, '_ansible_parsed': True, '_ansible_no_log': True, '_ansible_verbosity': 0, 'task_vars': runtime_data})
    module = setup.run(tmp=None, task_vars=runtime_data)
    assert module['failed'] == True

    # Test with modules set in FACTS_MODULES
    # Test

# Generated at 2022-06-13 09:58:30.824290
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 09:58:32.130251
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("NOT TESTED")

# Generated at 2022-06-13 09:58:40.538779
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Arrange
    # params passed to method run
    tmp = None
    task_vars = {}

    # used by side_effect of mocked methods
    # return_value of mocked methods
    # expected_value of assert statements

# Generated at 2022-06-13 09:58:41.921723
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run(ActionModule, tmp=None, task_vars=None)

# Generated at 2022-06-13 09:59:36.478620
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping
    class FakeModule:
        def __init__(self):
            self.params = {}
        def exit_json(self, **kwargs):
            pass
        def fail_json(self, **kwargs):
            pass

    class FakeLoader:
        def find_plugin_with_context(self, *args):
            return FakePluginWithContext()

    class FakePluginWithContext:
        def __init__(self):
            pass
        def resolved_fqcn(self, *args):
            return 'ShowCommand'

# Generated at 2022-06-13 09:59:37.976340
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("ActionModule")
    ActionModule()

# Generated at 2022-06-13 09:59:43.952711
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("in test_ActionModule_run")
    # create an instance of the Ansible stub module argspec
    argspec = AnsibleArgumentSpec()
    # create an instance of the Ansible test module
    am = ActionModule(argument_spec=argspec, supports_check_mode=True)
    am.ASK_PASS = False
    am.DEFAULT_VAULT_ID_MATCH = '.*$'
    am.RUN_ONCE = False
    # execute the run() method
    result = am.run()
    print(result)
    assert result['ansible_facts']['_ansible_facts_gathered'] == True



# Generated at 2022-06-13 09:59:51.451392
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task

    def return_test_results(task_args, task_vars, wrap_async=False):
        return dict(
            ansible_job_id='123456',
            finished=0,
            results_file='/tmp/results.json',
            runner_ident='local/13272356/ansible_hostname',
            start_time='2016-02-15T11:22:33',
            verbose_always=False,
            warnings=[]
        )


# Generated at 2022-06-13 09:59:52.411775
# Unit test for constructor of class ActionModule
def test_ActionModule():
    constr = ActionModule()
    assert constr != None


# Generated at 2022-06-13 09:59:58.663399
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor with empty parameters
    dummy_task = None
    dummy_connection = None
    dummy_play_context = None
    dummy_loader = None
    dummy_templar = None
    dummy_shared_loader_obj = None

    action_module_instance = ActionModule(dummy_task, dummy_connection, dummy_play_context, dummy_loader, dummy_templar,
                                          dummy_shared_loader_obj)
    print(action_module_instance)

    # Constructor with the parameters
    action_module_instance = ActionModule(dummy_task, dummy_connection, dummy_play_context, dummy_loader, dummy_templar,
                                          dummy_shared_loader_obj)
    print(action_module_instance)



# Generated at 2022-06-13 09:59:59.278887
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:00:06.648144
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_task = MagicMock()
    mock_task.run_once = False
    mock_task.args = {}
    mock_task.action = 'setup'
    mock_task.action_args.add_warnings = True
    mock_task.action_args.add_deprecated_warnings = True
    mock_task.action_args.gather_subset = 'all'
    results = ActionModule(mock_task).run({}, {'ansible_facts': {'_ansible_facts_gathered': False, 'ansible_all_ipv4_addresses': ['192.168.1.1', '192.168.1.2']}})

# Generated at 2022-06-13 10:00:13.501823
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.loader import action_loader

    conn_loader, conn_path = action_loader._get_connections('local_connection')
    conn_cls = conn_loader.get('local_connection', class_only=True)
    shared_loader_obj = action_loader._shared_loader_obj

    config_data = dict(FACTS_MODULES=["ansible.legacy.setup", "parsed_setup"])
    config = C.Config(config_data)
    conn = conn_cls(task=None, connection=None)

    task_vars = {}
    task_vars['ansible_facts'] = {}

# Generated at 2022-06-13 10:00:22.221718
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule('setup')
    tmp = '/tmp'
    task_vars = {'ansible_facts_parallel': None, 'ansible_facts': {}}
    result = action_module.run(tmp, task_vars)
    assert result['msg'] == 'The following modules failed to execute: ansible.legacy.setup\n'
    assert result['failed'] == True
    assert result['failed_modules'] == {'ansible.legacy.setup': {'failed': True, 'warnings': ['No handlers could be found for '
                                                                                           'logging "ansible.utils.module_docs_fragments".']}}

# Generated at 2022-06-13 10:02:22.559712
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    from ansible.utils.vars import merge_hash
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    '''
    Testing the run method in ansible.plugins.action.setup.py
    '''

    class TestTaskResult(TaskResult):
        def __init__(self, inv_data, play_context, task_vars):
            super(TaskResult, self).__init__()
            self.invocation = inv_data
            self.play_context = play_context
            self.task_vars = task_vars
            self.task

# Generated at 2022-06-13 10:02:23.650011
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:02:33.790647
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.vars import merge_hash
    _task = None
    _display = None
    _loader = None
    _variable_manager = None
    _shared_loader_obj = None
    _action = ActionModule(_task, _loader, _shared_loader_obj, _variable_manager)
    _tmp = None

# Generated at 2022-06-13 10:02:42.309009
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:02:50.586530
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {'ansible_verbosity': 3, 'ansible_network_os': 'ios'}
    tmp = '$HOME/.ansible/tmp'
    task = {'args': {'parallel': None}}
    config = {'FACTS_MODULES': ['smart', 'ansible_network_os', 'ansible_system', 'ansible_processor', 'ansible_network_resources']}
    connection = {'_shell': {'tmpdir': tmp}}
    m = ActionModule({'task': task, 'connection': connection, 'config': config})
    m._display = {'vvvv': print}

# Generated at 2022-06-13 10:03:00.230221
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test method run of class ActionModule
    """
    # Setup some test values
    tmp = '/var/tmp'
    task_vars = {'ansible_check_mode': False, 'ansible_facts': {'network_os': 'IOS'}, 'ansible_network_os': 'IOS'}

    # Create an instance of ActionModule
    am = ActionModule(task=dict(action=dict(module='setup', args=dict())), connection='local', play_context=dict())

    # Call method run of class ActionModule
    result = am.run(tmp, task_vars)

    assert result['skipped'] == True
    assert result['skipped_modules']['ansible.legacy.setup']['skipped'] == True

# Generated at 2022-06-13 10:03:01.481792
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_action_module = ActionModule()
    assert my_action_module is not None

# Generated at 2022-06-13 10:03:16.031753
# Unit test for constructor of class ActionModule
def test_ActionModule():
    gv = {'ANSIBLE_CONFIG': '/etc/ansible/ansible.cfg'}
    ac = dict(ActionModule(play_context=dict(verbosity=2),
                           task=dict(action=dict(module='ping', args=dict(data='hello world')))))
    assert ac['_task'] == dict(action=dict(module='ping', args=dict(data='hello world')))
    assert ac['_play_context'] == dict(verbosity=2)
    assert ac['_loader'] == None
    assert ac['_shared_loader_obj'] == None
    assert ac['_connection'] == None
    assert ac['_templar'] == None
    assert ac['_supports_check_mode'] == False
    assert ac['_supports_async'] == False

# Generated at 2022-06-13 10:03:21.056645
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:03:27.256077
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task="", connection="network_cli", play_context={}, loader=None, templar=None, shared_loader_obj=None)
    module = action.run()
    assert module.get('ansible_facts')
    assert module.get('ansible_facts').get('_ansible_facts_gathered')