

# Generated at 2022-06-13 09:55:28.031337
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_name = 'test_ActionModule_run'

    action_module = ActionModule()
    action_module._connection = type('connection', (object,), dict(
        _shell=type('shell', (object,), dict(tmpdir='/tmp/somedir'))
    ))

    task_vars = {"somevar": "somevalue"}
    setattr(action_module, "_task", type('task', (object,), dict(
        args=dict(a_string="this is a string")
    )))

    setattr(action_module, "_display", type('display', (object,), dict(
        warning=lambda x: print(x),
        vvvv=lambda x: print(x)
    )))


# Generated at 2022-06-13 09:55:31.436971
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)
    assert isinstance(action_module, ActionBase)
    assert isinstance(action_module, ActionModule)


# Generated at 2022-06-13 09:55:40.480641
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # defining variables to make the template syntax work
    C.config.get_config_value.side_effect = lambda x: C.config.parser.values[x]
    C.config.parser.values = {'FACTS_MODULES': ['facts'], 'CONNECTION_FACTS_MODULES': {}}
    ActionBase._configure_module.side_effect = lambda x: x
    ActionBase._low_level_execute_command.side_effect = lambda x, y: (0, 'fake_stdout', '')
    ActionBase._remote_expand_user.side_effect = lambda x: '/fake/host/' + x
    ActionBase._find_needle.side_effect = lambda x, y: (0, 'fake_needle')

# Generated at 2022-06-13 09:55:50.574256
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    mod._task = Task()
    mod._task.args = dict()
    mod._task.args['fact_module'] = 'ansible.legacy.setup'
    mod._task.args['fact_module_args'] = dict()
    mod._task.args['parallel'] = None
    mod._task.args['verbosity'] = 0
    mod._task.action = dict()
    mod._task.action['args'] = dict()
    mod._task.action['args']['fact_module'] = 'ansible.legacy.setup'
    mod._task.action['args']['fact_module_args'] = dict()
    mod._task.action['args']['parallel'] = None
    mod._task.action['args']['verbosity'] = 0

# Generated at 2022-06-13 09:56:01.942268
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # set up test environment
    role_path = os.path.join('test', 'support', 'test_action_module', 'roles', 'test')
    os.makedirs(role_path, exist_ok=True)
    assert os.path.exists(role_path)
    test_file = os.path.join(role_path, 'test.yml')
    with open(test_file, 'w') as f:
        f.write('---\n- hosts: localhost\n  tasks:\n    - name: test for ActionModule\n      ansible_facts:\n        test: '
                'test\n')
    assert os.path.exists(test_file)
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

# Generated at 2022-06-13 09:56:11.195562
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(None, None, None)
    action._supports_check_mode = True
    result = action.run(None, None)

    assert(result['ansible_facts'] == {})
    assert(not result['failed'])
    assert(result['skipped'] == True)
    assert(result['skipped_modules'] == {})
    assert(result['failed_modules'] == {})
    assert(result['msg'] == "The following modules were skipped: smart\n")
    assert(result['ansible_facts']['_ansible_facts_gathered'])
    assert(result['_ansible_verbose_override'])

# Generated at 2022-06-13 09:56:19.697250
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Init the class
    action = ActionModule()
    action._task.args = {}
    action._task.module_defaults = {}
    action._task.collections = []
    action._shared_loader_obj = None
    action._connection = None
    action._templar = None
    action._task._parent = None
    action._task._parent._play = None
    action._task._parent._play._action_groups = None
    # Run the method
    try:
        result = action.run()
    except:
        pass

# Generated at 2022-06-13 09:56:28.945944
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create a mock config
    class Config:
        FACTS_MODULES = ['setup']

    class Facts_Modules_Config(Config):
        def __init__(self, fact_module_list):
            self.FACTS_MODULES = fact_module_list

    class Connection(object):
        def __init__(self, connection):
            self._shell = connection

    class Shell(object):
        def __init__(self, tmpdir):
            self.tmpdir = tmpdir

    class Task_Vars(dict):
        def __init__(self):
            pass

    class Tmp:
        def __init__(self):
            self.message = 'message'

    # create a mock task
    class Task:
        def __init__(self):
            self.args = {}
            self.args

# Generated at 2022-06-13 09:56:40.172099
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    import shutil
    import os
    import sys
    import json
    import yaml
    import pytest
    from ansible.module_utils.facts import is_fact_module
    from ansible.module_utils.facts import is_local_fact_module
    from ansible.plugins.action.setup import ActionModule as setupActionModule
    from ansible.plugins.action.setup import ActionModule as setupActionModule
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_result import TaskResult
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 09:56:49.126682
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class MockTask:
        def __init__(self):
            self.args = None
            self.name = None
    class MockExecutor:
        def __init__(self):
            self.module_name = None
            self.module_args = None
            self.module_vars = None
        def run_module(self, module_name, module_args, tmp, task_vars=None, wrap_async_bool=None):
            self.module_name = module_name
            self.module_args = module_args
            self.module_vars = task_vars
            return None
    class MockTaskExecutor:
        def __init__(self):
            self.run_module = None
        def run_main(self):
            return True

# Generated at 2022-06-13 09:57:02.126206
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create an instance of ActionModule
    a = ActionModule()

# Generated at 2022-06-13 09:57:08.706732
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    task_vars = {}
    result = module.run(task_vars=task_vars)
    assert result['ansible_facts']['_ansible_facts_gathered'] == True
    assert result['_ansible_verbose_override'] == True

# Generated at 2022-06-13 09:57:15.495124
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock parameters taken by method
    tmp = None
    task_vars = dict()
    task_vars['ansible_facts_parallel'] = None
    task_vars['ansible_facts'] = dict()
    task_vars['ansible_facts']['network_os'] = 'eos'

    # mock module to be imported by plugin
    mock_module = __import__('ansible.plugins.action.setup')

    # setup the class object
    action = ActionModule(mock_module.ActionBase, tmp, task_vars)

    # call the run method
    result = action.run()

    # assert result
    assert isinstance(result, dict)
    assert result['ansible_facts'].get('_ansible_facts_gathered')

# Generated at 2022-06-13 09:57:25.632639
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._task = mock.MagicMock()
    action_module._task.args = mock.MagicMock()
    action_module._task.args.copy = mock.MagicMock()
    action_module._task.args.copy.return_value = {'key': 'value'}
    action_module._templar = mock.MagicMock()
    action_module._shared_loader_obj = mock.MagicMock()
    action_module._shared_loader_obj.module_loader = mock.MagicMock()
    action_module._shared_loader_obj.module_loader.find_plugin_with_context = mock.MagicMock()
    action_module._shared_loader_obj.module_loader.find_plugin_with_context.return_value = mock.MagicMock

# Generated at 2022-06-13 09:57:35.735910
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    t = ActionModule()
    t._shared_loader_obj = mock_loader
    t._connection = mock_connection
    t._task = mock_task
    t._task.args = {
        'gather_subset': 'network',
        'gather_timeout': 1,
        'filter': 'ansible.legacy.setup'
    }

    t._display = mock_display

    t._templar = mock_templar

    tmp = 'tmp'
    task_vars = {}

    res = t.run(tmp,task_vars)

# Generated at 2022-06-13 09:57:44.928769
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test with ansible_facts_parallel = False
    task = {'args': {'network_os': 'ios'}, 'action': 'setup', 'delegate_to': None, 'register': 'ansible_facts', 'name': 'ios'}
    action_module = ActionModule(task, {'playbook_dir': '/home/ansible/playbook3'}, C.DEFAULT_LOADER, C.DEFAULT_VARIABLE_MANAGER, C.DEFAULT_HOST_LIST)
    task_vars = {'ansible_connection': 'network_cli',
                 'ansible_facts': {'network_os': None},
                 'ansible_network_os': 'ios', 'ansible_facts_parallel': False}
    tmp = None

# Generated at 2022-06-13 09:57:59.075882
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:58:00.461027
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method ActionModule.run"""
    pass # TODO: implement

# Generated at 2022-06-13 09:58:01.033621
# Unit test for constructor of class ActionModule
def test_ActionModule():
  am = ActionModule()

# Generated at 2022-06-13 09:58:02.887436
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # return
    # print(ActionModule.__init__.__doc__)
    print(ActionModule.run.__doc__)

# Generated at 2022-06-13 09:58:38.264426
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:58:46.855382
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.connection import Connection
    from ansible.utils.vars import merge_hash

    m_module = AnsibleModule(argument_spec={'parallel': {'type': 'bool'}, 'network_os': {},
                                             '_ansible_facts_gathered': {'type': 'bool'}}, supports_check_mode=True)
    connection = Connection(m_module._socket_path)
    m_action = ActionModule(m_module, connection)

    # Unit test: run method with parallel=True
    m_action._task.args = {'parallel': True}
    m_action._task.vars = {'ansible_facts_parallel': False, 'ansible_hostname': 'dummyhost'}

# Generated at 2022-06-13 09:58:57.518617
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import unittest
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from ansible.plugins.loader import action_loader

    class TestActionModule(unittest.TestCase):
        def setUp(self):
            self.action_plugin = action_loader.get('setup', class_only=True)
            self.action_plugin.task_vars = {}
            self.action_plugin.connection = connection_loader.get('local', class_only=True)()
            self.action_plugin.task = MagicMock()
            self.action_plugin.task.args = {}
            self.action_plugin._connection._shell.run.return_value = ({}, 'out', 0)


# Generated at 2022-06-13 09:59:02.347360
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create object for class ActionModule
    action_module_obj = ActionModule()

    # unit test for method run of class ActionModule
    action_module_obj._shared_loader_obj = True
    action_module_obj._task = True
    action_module_obj._display = True
    action_module_obj._templar = True
    result = action_module_obj.run()

    # Test expected result
    assert result

# Generated at 2022-06-13 09:59:09.555512
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import ansible.utils.vars
    ansible.utils.vars.VarsModule = MockVars
    import ansible.plugins.action
    ansible.plugins.action.ActionBase = MockActionBase
    import ansible.executor.module_common
    ansible.executor.module_common.get_action_args_with_defaults = Mockget_action_args_with_defaults
    import ansible.plugins.action.setup
    ansible.plugins.action.setup.SetupModule = MockSetupModule

    am = ActionModule(None)
    am.execute_module = MockExecuteModule
    am.run(None, None)


# Generated at 2022-06-13 09:59:16.098699
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    from ansible.utils.vars import combine_hash
    from ansible.module_utils.parsing.convert_bool import boolean
    task_vars = {
        'ansible_facts': {},
        'ansible_facts_parallel': None,
        'ansible_facts_modules': ['ansible.legacy.setup', 'ansible.legacy.setup']
    }
    action_module = ActionModule(0, 0, 0, 0, 0, 0, 0, 0)
    result = action_module.run(None, task_vars)
    assert isinstance(result, dict)
    assert {'failed', 'ansible_facts', 'skipped', 'skipped_modules', '_ansible_verbose_override'}.issubset(set(result.keys()))


# Generated at 2022-06-13 09:59:16.535051
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:59:23.365023
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a mock variables object to use for testing
    class TestVarsModule:
        def __init__(self, dict):
            self.dict = dict

        def __getitem__(self, name):
            return self.dict[name]

    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Test that execute set 'setup run' to True
    action_module._execute_module = lambda module_name, module_args, task_vars, wrap_async: {'failed': False, 'changed': False, 'ansible_facts': {}, 'ansible_facts_gathered': True}

# Generated at 2022-06-13 09:59:24.142044
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:59:36.706074
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes

    # create our module object that we'll test
    am = ActionModule(
        task=dict(action=dict(module='setup', args=dict(filter='ansible_architecture'))),
        connection=dict(),
        play_context=dict(verbosity=2, check_mode=False),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict(),
    )

    # create a dummy task_vars with mocked special vars

# Generated at 2022-06-13 10:00:41.425778
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize ansible.module_utils.parsing.convert_bool
    C.config.load_config_file()
    # Setup args for ansible.module_utils.facts.get_facts
    assert isinstance(C.config.get_config_value('FACTS_MODULES'), list)

    assert C.config.get_config_value('CONNECTION_FACTS_MODULES') != {}

# Generated at 2022-06-13 10:00:44.098319
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(DummyTask(), connection=None, templar=None, shared_loader_obj=None)
    assert am.supports_check_mode is True, "action module constructor failed"

# Generated at 2022-06-13 10:00:53.825299
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext(remote_addr='127.0.0.1', remote_user='test', remote_pass='test')

# Generated at 2022-06-13 10:01:00.814864
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.setup import ActionModule as setup_ActionModule

    # Mock command 'ansible_facts_parallel' is defined and is not None
    task_mock = MagicMock()
    task_mock.args = {
        'filter': None,
        'gather_subset': ['network'],
        'gather_timeout': None,
        'parallel': None,
        'network_os': 'ios'
    }
    task_mock._parent = MagicMock()
    task_mock._parent._play = MagicMock()
    task_mock._parent._play._action_groups = ['all']

# Generated at 2022-06-13 10:01:01.931826
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global action_module
    action_module = ActionModule()

# Generated at 2022-06-13 10:01:03.086037
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2022-06-13 10:01:13.854709
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.task import Task
    t_mock = Task()
    t_mock._parent  = TaskQueueManager('/tmp')
    t_mock.module_defaults = {}
    t_mock._play = TaskQueueManager('/tmp')
    t_mock._play._action_groups = [{}]
    t_mock._parent._play._action_groups = [{}]
    t_mock.action = 'setup'
    t_mock.args = {}
    t_mock.async_val = 0
    t_mock.become = False
    t_mock.become_method = None
    t

# Generated at 2022-06-13 10:01:14.736262
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run')

# Generated at 2022-06-13 10:01:22.623281
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def _get_module_args(self, fact_module, task_vars):

        mod_args = self._task.args.copy()

        # deal with 'setup specific arguments'
        if fact_module not in C._ACTION_SETUP:
            # network facts modules must support gather_subset
            if self._connection._load_name not in ('network_cli', 'httpapi', 'netconf'):
                subset = mod_args.pop('gather_subset', None)
                if subset not in ('all', ['all']):
                    self._display.warning('Ignoring subset(%s) for %s' % (subset, fact_module))

            timeout = mod_args.pop('gather_timeout', None)

# Generated at 2022-06-13 10:01:29.587801
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock datas
    tmp = None
    task_vars = {'ansible_facts': {'gathered_facts': True}}
    # Mock modules
    modules = ["os", "distribution", "system"]
    parallel = True
    def _get_module_args(fact_module, task_vars):
        return {}
    def _combine_task_result(result, task_result):
        return {}
    def run(tmp, task_vars):
        return {}
    def _execute_module(module_name, module_args, task_vars, wrap_async):
        return {'finished': 1, 'failed': 0, 'skipped': 0}
    def _remove_tmp_path(self):
        return
    def _display(message):
        print(message)

    # Mock class

# Generated at 2022-06-13 10:03:50.040432
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = {
        'ansible_facts': {
            '_ansible_facts_gathered': True
        },
        'failed': True,
        'failed_modules': {
            'fact_module': {
                'msg': 'failed'
            }
        },
        'msg': 'The following modules failed to execute: fact_module',
        'skipped_modules': {
            'fact_module': {
                'msg': 'skipped'
            }
        }
    }
    action_module = ActionModule()
    class_object = action_module.__class__()

# Generated at 2022-06-13 10:03:59.236832
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.module_executor import LocalModuleExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    from ansible.utils.vars import combine_vars

    action = action_loader.get('setup', task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    setup_action_mod = action.action_plugin_class(action._task, action._connection, action._play_context, action._loader, action._templar, action._shared_loader_obj)
    setup_action_mod.loader.set_basedir(b"/home/test/ansible")

    hostv

# Generated at 2022-06-13 10:04:05.423845
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up mocks needed for this test
    import ansible.plugins.action.setup as action_setup
    import ansible.plugins.action.normal as action_normal
    import ansible.module_utils.facts.system.base as facts_module_base
    modules = {'ansible.plugins.action.setup': action_setup,
               'ansible.plugins.action.normal': action_normal,
               'ansible.module_utils.facts.system.base': facts_module_base}
    module_patcher = patch.dict('sys.modules', modules)
    module_patcher.start()
    from ansible.plugins.action.setup import ActionModule as setup_action_module
    from ansible.plugins.action.normal import ActionModule as normal_action_module

# Generated at 2022-06-13 10:04:15.505297
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import re
    import unittest
    import ansible.constants as C
    import ansible.plugins.action
    import ansible.utils.vars
    import ansible.module_utils.parsing.convert_bool
    import ansible.plugins.loader
    import ansible.executor.module_common
    import ansible.utils.vars
    import ansible.utils.display
    import ansible.utils.sentinel
    import ansible.errors
    import ansible.utils.plugin_docs
    import ansible.inventory.host
    import ansible.compat.six
    import ansible.utils.unsafe_proxy
    import ansible.compat.ipaddress
    import ansible.playbook.play_context
    import ansible.playbook.play
    import ansible.playbook.task_

# Generated at 2022-06-13 10:04:22.280051
# Unit test for constructor of class ActionModule
def test_ActionModule():

    import ansible.executor
    import ansible.plugins.action
    import ansible.executor.task_result
    import ansible.plugins.loader

    from ansible.executor.task_queue_manager import TaskQueueManager

    task = ansible.executor.task_result.TaskResult(dict(action=dict(module='run-tasks')))
    task_vars = dict(ansible_facts_parallel=True, ansible_vault_password='pass')
    variables = dict(ansible_vault_password='pass')
    # Creating ActionModule object
    module = ansible.plugins.action.ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:04:31.684105
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_module = "ansible_network.setup"

    # Test 0: If modules is not empty and parallel is None, parallel is set to true

# Generated at 2022-06-13 10:04:33.116487
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action.__class__.__name__ == 'ActionModule'

# Generated at 2022-06-13 10:04:33.788574
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:04:34.462412
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:04:41.588485
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    am.task = {}
    am.task_vars = {}
    am.connection = {}
    am.task_vars['ansible_facts_parallel'] = False
    fm = 'ansible.legacy.setup'
    ma = {'filter': '*'}
    ta = {}
    res = am._execute_module(fm, ma, ta, wrap_async=False)
    assert res
    result = am.run(tmp=None, task_vars=am.task_vars)
    assert result