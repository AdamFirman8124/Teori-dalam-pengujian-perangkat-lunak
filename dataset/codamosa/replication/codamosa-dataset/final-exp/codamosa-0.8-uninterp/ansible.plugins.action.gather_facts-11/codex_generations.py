

# Generated at 2022-06-13 09:55:23.128311
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(ActionModule, '/etc/ansible/roles/role_under_test/tasks/main.yml', dict(), False, False, False)
    return am

# Generated at 2022-06-13 09:55:36.159401
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 09:55:46.276930
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #Implementation tests.
    fake_templar = mock.Mock()
    fake_templar.template.return_value = "template_test"
    fake_templar.template._templar = fake_templar

    # test of method run
    fake_command = Mock()
    fake_command.run = MagicMock(return_value=dict(failed=False))
    fake_loader = Mock()
    fake_loader.action_loader = Mock()
    fake_loader.action_loader.get.return_value = fake_command
    fake_loader.path_loader = Mock()
    fake_loader.path_loader.get.return_value = fake_command

    tmp = Mock()
    tmp.name = "/tmp/some/path"

    fake_task = Mock()

# Generated at 2022-06-13 09:55:54.942339
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Instantiation of the action plugin object and its method run
    # ActionBase._configure_play_context(play_context)
    # is called before the run method
    # This method will set the member variables of the action plugin
    # object which are needed in the run method.
    # TODO: Create a common test class which includes the
    # _configure_play_context(play_context) call and make
    # test_<method name> class methods which can be reused by
    # test classes inheriting from the common test class
    # and set the member variables accordingly in setUp(self)
    # method
    # NOTE: The action plugin class being tested needs to be
    # passed as first argument to the common test class
    pass


# Generated at 2022-06-13 09:56:06.585603
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.connection import Connection

    runner_path = os.path.join(C.DEFAULT_LOCAL_TMP, 'test_action_module.py')
    with open(runner_path, 'w') as f:
        f.write('#!/usr/bin/python')

    os.chmod(runner_path, 0o755)

    class Task:
        def __init__(self):
            self.task_vars = {}
            self._parent = self
            self._play = self

        def _get_vars(self):
            return self.task_vars

        def get_vars(self):
            return self.task_vars

        def set_vars(self, vars):
            self.task_vars = vars


# Generated at 2022-06-13 09:56:08.825565
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Constructing ActionModule object to run method
    mod = ActionModule()

    # Calling the method under test
    result = mod.run()

    # Expected success result
    success_result = {'ansible_facts': result['ansible_facts']}
    assert result == success_result

# Generated at 2022-06-13 09:56:12.929096
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None

# Unit test to test private function _get_module_args()

# Generated at 2022-06-13 09:56:15.589330
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils.facts.system.distribution import Distribution
    action = ActionModule(TaskQueueManager([], 0), Distribution, {}, {})
    assert(action)

# Generated at 2022-06-13 09:56:19.211687
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=dict())
    assert am._task_vars_pruned is None
    assert am._templar is None
    assert am._task_vars_for_task_blocks is None

# Generated at 2022-06-13 09:56:26.051061
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # All required and expected values are hardcoded here, except for those that cannot be hardcoded.
    # Like tmp, task_vars, and connection.
    import module_utils.basic
    tmp = None
    task_vars = {'variable_name': 'value_here'}
    connection = module_utils.basic.AnsibleConnection(None)

    # Constructor of class ActionModule
    test_obj = ActionModule(tmp, task_vars, connection)
    assert test_obj != None

# Generated at 2022-06-13 09:56:47.657253
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from units.mock.loader import DictDataLoader
    from units.mock.playbook import Playbook

    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager

    from ansible.plugins import module_loader
    module_loader.add_directory(os.path.join(os.path.dirname(__file__), 'units'))

    variables = VariableManager()

    inventory = Inventory(loader=DictDataLoader({'group': {
        'hosts': ['localhost'],
        'vars': {'ansible_connection': 'local'}
    }}
    ))
    inventory.add_group('group')
    inventory.add_

# Generated at 2022-06-13 09:56:57.520230
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockModule(object):
        def __init__(self, module_name):
            self.__name__ = module_name
    class MockTask(object):
        def __init__(self, module_name, module_args):
            self.action = MockModule(module_name)
            self.args = module_args
    class MockPlayContext(object):
        def __init__(self, connection):
            self.connection = connection
    class MockPlay(object):
        def __init__(self, connection):
            self.context = MockPlayContext(connection)
    class MockLoader(object):
        def __init__(self, module_name):
            self.module_name = module_name
            self.module_loader = MockModuleLoader(module_name)

# Generated at 2022-06-13 09:57:05.518308
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 09:57:10.628696
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    tmp = None
    task_vars = None
    action_module = ActionModule()
    result = action_module.run(tmp, task_vars)
    print(result)

if __name__ == "__main__":
    test_ActionModule_run()

# Generated at 2022-06-13 09:57:12.440584
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test ActionModule constructor
    module = ActionModule()
    assert isinstance(module, ActionBase)
    assert isinstance(module, ActionModule)



# Generated at 2022-06-13 09:57:23.667820
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task as AnsibleTask
    from ansible.plugins.loader import action_loader
    from ansible.module_utils.common._collections_compat import Sequence
    modules = []

    # create mock task object
    mock_task = AnsibleTask()
    mock_task._role = None
    mock_task._role_context = None
    mock_task.action = "setup"
    mock_task.args = {}
    mock_task.module_defaults = {}
    mock_task.collections = Sequence()
    mock_task._parent = None
    mock_task.new_fail_q = False
    mock_task.new_run_once = False
    mock_task.notified_by = []
    mock_task.notify = []
    mock_task._block = None



# Generated at 2022-06-13 09:57:25.946590
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_ActionModule = ActionModule(None, None)
    assert test_ActionModule is not None

# Generated at 2022-06-13 09:57:26.595173
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run()

# Generated at 2022-06-13 09:57:36.419530
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    from ansible import constants as C
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.plugins.loader import action_loader
    from ansible.plugins.action.setup import ActionModule
    # Mock the module
    # Python 3 import
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 09:57:41.168786
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action
    task_vars={'ansible_network_os':'iosv'}
    am = ansible.plugins.action.ActionModule(None, None, None, None)
    am.get_action_args_with_defaults = lambda x: {}
    am.run(tmp=None, task_vars=task_vars)

# Generated at 2022-06-13 09:58:04.272585
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:58:08.120346
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""

    # create an object of class ActionModule without any argument
    obj = ActionModule()

    # TODO: Write more test cases to cover all lines of code
    
    # get content of the object
    #obj.getvalue()

# Generated at 2022-06-13 09:58:15.701461
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module_obj = ActionModule(task={"args": {}, "module_defaults": {}, "module_vars": {}}, connection=None,
                                     play_context=None, loader=None, templar=None, shared_loader_obj=None)
    for attr in (action_module_obj._task, action_module_obj._play_context, action_module_obj._loader,
                 action_module_obj._shared_loader_obj):
        assert attr is not None, 'Failed to instantiate ActionModule object'

# Generated at 2022-06-13 09:58:20.182198
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # set up test
    import unittest
    from ansible.plugins.action.setup import ActionModule
    class test_ActionModule_run(unittest.TestCase):
        def test_test_test(self):
            pass

    test_class = test_ActionModule_run()
    test_class.test_test_test()

# Generated at 2022-06-13 09:58:28.006750
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    task_vars['ansible_facts'] = None
    mock_task_vars = MagicMock()
    mock_task_vars.get.side_effect = lambda x: task_vars.get(x)
    mock_task_vars.__getitem__.side_effect = task_vars.__getitem__
    mock_task_vars.__contains__.side_effect = task_vars.__contains__

    mock_task = MagicMock()
    mock_task.args = dict()
    mock_task._parent = None
    mock_task._parent._play = MagicMock()
    mock_task._parent._play._action_groups = dict()

    mock_templar = MagicMock()

    mock_shared_loader_obj = MagicM

# Generated at 2022-06-13 09:58:29.446353
# Unit test for constructor of class ActionModule
def test_ActionModule():

    action_module = ActionModule()

    assert action_module

# Generated at 2022-06-13 09:58:39.189072
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import context
    from ansible.cli.playbook import PlaybookCLI
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    import ansible.constants as C
    import json
    import pytest

    setattr(C, 'DEFAULT_DEBUG', True)
    context.CLIARGS = PlaybookCLI(['test.yml']).parse()
    playbook = Play.load('test.yml', variable_manager=None, loader=None)
    playbook._tqm = TaskQueueManager(inventory=None, variable_manager=None, loader=None)

    task = playbook.get_tasks()[0]
    module_name = task.action
    action = action_

# Generated at 2022-06-13 09:58:45.221649
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of ActionModule
    obj = ActionModule()

    # Create an instance of AnsibleLoader
    ansible_loader_obj = AnsibleLoader()

    # Get the results of function _get_module_args
    result = obj._get_module_args('platform', ansible_loader_obj)

    # Creating expected result
    exp_result = {
        'filter': '*',
        'gather_subset': 'all'
    }

    assert result == exp_result



# Generated at 2022-06-13 09:58:46.678279
# Unit test for constructor of class ActionModule
def test_ActionModule():
    runner_execution = ActionModule()
    assert runner_execution

# Generated at 2022-06-13 09:58:49.240094
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    result = m.run(tmp=None, task_vars=None)
    print(result)


# Generated at 2022-06-13 09:59:37.017485
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    actionmodule = ActionModule()
    assert actionmodule is not None

# Generated at 2022-06-13 09:59:52.054812
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import os
    import json

    import unittest.mock as mock


    class MockConfig:

        def __init__(self):
            self.data = {
                'FACTS_MODULES': ['smart'],
                'CONNECTION_FACTS_MODULES': {'network_cli': 'ansible.legacy.network_cli'},
            }

        def get_config_value(self, name, variables=None):
            return self.data[name]

        def __setitem__(self, name, value):
            self.data[name] = value


    class MockTemplar:

        def __init__(self, facts={}):
            self.facts = facts
            self.vars = {
                'ansible_facts': self.facts,
            }


# Generated at 2022-06-13 09:59:58.498501
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #
    # Tests ActionModule.run (no parallel, connection network_cli)
    #
    # Args:
    #  - tmp: temporary directory created for the test
    #  - task_vars: variables for the test
    #
    # Returns:
    #  Nothing
    #
    # Raises:
    #  Nothing
    #
    from .mock_executor_connection import MockConnection
    from ansible.plugins.action.setup import ActionModule as SetupActionModule
    from ansible.module_utils.facts import FactsModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils.facts import NetworkFactsModule
    import os
    import tempfile
    import shutil


# Generated at 2022-06-13 09:59:59.394857
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise NotImplementedError

# Generated at 2022-06-13 10:00:00.565564
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = ActionModule()
    assert isinstance(result, ActionModule)

# Generated at 2022-06-13 10:00:06.862871
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    mock_loader = action_loader._create_directory_structure()
    mock_loader = action_loader._add_all_plugin_dirs(mock_loader)
    task = Task()
    task.args = {}
    task.action = 'setup'
    task.action = 'setup'
    host = Host()
    host.name = 'nested_host'

# Generated at 2022-06-13 10:00:13.641432
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:00:14.980517
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule('', '')

# Generated at 2022-06-13 10:00:25.498195
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Method run of class ActionModule
    '''
    global FAILURE_COUNT
    result = {}
    result['ansible_facts'] = {}
    result['changed'] = False
    result['skipped'] = False
    result['skipped_modules'] = {}
    result['failed'] = False
    result['failed_modules'] = {}

    # test case 1
    # all modules are skipped
    print("Testing setup with all modules skipped.")
    # for skipped
    assert result['skipped'] == False
    assert result['skipped_modules'] == {}
    assert result['ansible_facts']['_ansible_facts_gathered'] == True
    assert result['failed'] == False
    assert result['failed_modules'] == {} 

    # test case 2
    # when some modules are skipped

# Generated at 2022-06-13 10:00:26.669020
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:02:15.384640
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ac = ActionModule(None, None, None, None, None)
    assert ac._supports_async is True

# Generated at 2022-06-13 10:02:19.321945
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    runner = RunnerMock()
    pm = ActionModule(runner)
    pm.run(tmp=None, task_vars=dict(ansible_facts_parallel=None, ansible_verbose_override=None, ansible_facts_gathered=None, ansible_network_os=None, ansible_facts=None))

# Generated at 2022-06-13 10:02:30.893473
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import copy
    task_vars = {'ansible_facts_parallel': True, 'ansible_network_os': 'ios'}
    tmp = None
    action_module = ActionModule(connection=None, task=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module._task.args = {'network_os': 'ios'}
    action_module._task.args = {'parallel': False}
    modules = ['ansible.legacy.setup']
    args = {'gather_subset': 'all', 'gather_timeout': 100}
    action_module._task.args = args
    cmd = copy.deepcopy(action_module)
    cmd.run(tmp=tmp, task_vars=task_vars)

# Generated at 2022-06-13 10:02:31.367283
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:02:38.347807
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.plugins.strategy import StrategyBase

    class TestTaskQueueManager(TaskQueueManager):
        def _queue_task(self, host, task, task_vars, play_context):
            return dict(host=host, task=task, task_vars=task_vars, play_context=play_context)

        def _finalize_processed_tasks(self):
            pass

    class TestStrategy(StrategyBase):
        def get_hosts_remaining(self):
            return [1, 2]


# Generated at 2022-06-13 10:02:39.189034
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run')

# Generated at 2022-06-13 10:02:43.369251
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a class "constants" that contains C.RETRY_FILES_ENABLED = True
    # Call to method run of class ActionModule with constants as argument
    # and check for exception TypeError
    class constants:
        RETRY_FILES_ENABLED = True
    action_module = ActionModule()
    try:
        action_module.run(constants)
    except TypeError:
        pass



# Generated at 2022-06-13 10:02:51.031896
# Unit test for constructor of class ActionModule
def test_ActionModule():
    os.environ['ANSIBLE_CONFIG'] = "test/ansible.cfg"
    tmpfile = 'test.log'
    outfile = open(tmpfile, 'w')
    outfile.close()
    outfile = open(tmpfile, 'r')
    config = {"role_path": "..", "inventory": "test/hosts", "connection_plugins": "test/my_connection_plugins"}
    # "module_path": "test/my_modules", "module_utils": "test/my_module_utils"}
    path_name = "/usr/bin/ansible"
    task_vars = {}
    module_name = "setup"
    sleep_time = 1
    module_args = "ansible_verbosity=5"
    tmp_path = "/tmp/tmp_path"

# Generated at 2022-06-13 10:03:00.475142
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create mock modules
    import sys
    import unittest.mock as mock
    from ansible.plugins.action.setup import ActionModule as SetupActionModule

    # Create mock loader object
    from ansible.plugins.loader.action_plugin import ActionModuleLoader
    ActionModuleLoader_mod = mock.MagicMock()
    mock_action_loader = mock.MagicMock(spec=ActionModuleLoader)
    mock_action_loader.connection = mock.MagicMock()
    mock_action_loader.action_loader = ActionModuleLoader_mod
    mock_action_loader.action_loader.get_single_plugin = mock.MagicMock()

    # Create mock ActionModule object
    mock_action_module = mock.MagicMock(spec=ActionModule)
    mock_action_module.action_loader = mock.MagicMock()


# Generated at 2022-06-13 10:03:09.953789
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test module run
    """
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager

    module = action_loader.get('setup', class_only=True)
    task = {'args': {'filter': ['ansible_lsb.*'], 'gather_timeout': 5, 'gather_subset': ['network']}}
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory=None)
    variable_manager.set_variable('ansible_facts_parallel', True)
    variable_manager.set_variable('ansible_facts_gather_timeout', 10)
