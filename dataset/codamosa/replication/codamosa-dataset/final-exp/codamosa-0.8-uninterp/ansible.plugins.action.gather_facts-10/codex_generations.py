

# Generated at 2022-06-13 09:55:29.256015
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, '', '', {}, {}, {}, {}, '', '', '', '', '', True, None, None, None)

    assert type(action._supports_check_mode) == bool, "assertion failed" == "asserts"
    assert type(action._task_vars) == dict, "assertion failed" == "asserts"
    assert repr(action._loader) == '<AnsibleLoader object at 0x032FB350>', "assertion failed" == "asserts"
    assert repr(action._shared_loader_obj) == '<AnsibleLoader object at 0x032FB350>', "assertion failed" == "asserts"

# Generated at 2022-06-13 09:55:38.626893
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.setup import ActionModule
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.network.common.utils import FactsBase
    from ansible.module_utils.network.common.utils import load_provider
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils._text import to_text
    from ansible.plugins.loader import add_all_plugin_dirs
    import json
    import io
    import pytest
    import sys

    module_name = 'setup'
    current_dir = os.path.dirname(os.path.realpath(__file__))
    module_path = os.path.join(current_dir, '../../../modules/network/{}.py'.format(module_name))

# Generated at 2022-06-13 09:55:45.321222
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Testing a custom class to create an instance
    class Conn():
        def __init__(self):
            self._shell = None

    class Mod():
        def __init__(self):
            self.args = {}

    class Exec():
        def __init__(self):
            self._task = Mod()
            self._task._parent = Exec()
            self._connection = Conn()

    class Context():
        def __init__(self):
            self.CLIARGS = {}

    class Play():
        def __init__(self):
            self._action_groups = {}

    act = ActionModule()
    act._debug = True
    act._connection = None
    act._shared_loader_obj = Exec()
    act._shared_loader_obj._task._parent._play = Play()
    act._shared_loader_obj

# Generated at 2022-06-13 09:55:56.249709
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of the module test class
    action_module = ActionModule()

    # Create a test task to set the self._task variable for the ActionModule
    test_task = dict()

    # Set the arguments for the test task
    test_task['args'] = dict()
    test_task['args']['parallel'] = True
    test_task['args']['filter'] = 'smart'

    # Set the name for the test task
    test_task['name'] = 'gather_facts'

    # Set the action_name for the test task
    test_task['action_name'] = 'gather_facts'

    # Set the registered variable for the test task
    test_task['registered_var'] = 'ansible_facts'

    # Set the action of the test task

# Generated at 2022-06-13 09:56:05.629742
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test object creation and legacy module loading
    action_mod = ActionModule(loader=None, task=None, connection=None, play_context=None, loader_plg=None, templar=None, shared_loader_obj=None)

    # Test loading of a specific module from a collection
    fqmn = action_mod._shared_loader_obj.module_loader.find_plugin_with_context("setup", collection_list=("ansible_collections.ansible.builtin", "ansible_collections.not.a.collection"))
    assert fqmn == 'ansible_collections.ansible.builtin.setup'

# Generated at 2022-06-13 09:56:14.970579
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_task = MockAnsibleTask()
    mock_task.args = {'fact_name': 'value', 'parallel': 'False', 'network_os': 'some_value'}
    mock_task.action = 'setup'

    mock_task_vars = {'ansible_facts': {'network_os': 'some_value'}}

    # Instantiate our class
    action_module = ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # mock the actual run method on the module object
    mock_action_module_run = MockAnsibleActionModuleRun()
    action_module._execute_module = mock_action_module_run.run

# Generated at 2022-06-13 09:56:26.229019
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockTask(object):
        def __init__(self):
            self.args = {'parallel': 'no'}
    task = MockTask()

# Generated at 2022-06-13 09:56:36.826490
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock task
    task = mock.MagicMock()
    task.collections = mock.MagicMock()

    module_args = {'test': None}

    # Create a mock module
    module = mock.MagicMock()
    module.run.return_value = {'failed': False}
    module.resolved_fqcn = 'module.resolved_fqcn'

    # Create a mock module_loader
    module_loader = mock.MagicMock()
    module_loader.find_plugin_with_context.return_value = module

    # Create a mock loader
    loader = mock.MagicMock()
    loader.module_loader = module_loader

    # Create a mock shared_loader_obj
    shared_loader_obj = mock.MagicMock()
    shared_loader_obj._shared_loader

# Generated at 2022-06-13 09:56:46.964727
# Unit test for constructor of class ActionModule
def test_ActionModule():
    os.environ[str('ANSIBLE_NET_PASSWORD')] = str('password')

    config = {
        'ANSIBLE_NET_USERNAME': 'username',
        'ANSIBLE_NET_AUTH_PASS': 'password',
        'ANSIBLE_NET_AUTH_USERNAME': 'username',
        'ANSIBLE_NET_AUTH_PASSWORD': 'password',
        'ANSIBLE_NET_PASSWORD': 'password'
    }


# Generated at 2022-06-13 09:56:56.751030
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.action import ActionBase
    from ansible.utils.vars import merge_hash

    import pytest
    import os
    import time
    import inspect
    import json

    # HostVars object to mock Host object of ansible
    class HostVars:
        def __init__(self, ansible_facts=None):
            self._ansible_facts = ansible_facts

    # Host object to mock Host object of ansible

# Generated at 2022-06-13 09:57:12.955306
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Tests that a simple initialization of the class works
    #
    # Args:
    #     none
    #
    # Returns:
    #     none
    #
    # Raises:
    #     none
    try:
        # action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
        assert True
    except Exception:
        assert False, "An exception was raised during the initialization of ActionModule"

# Generated at 2022-06-13 09:57:23.706857
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook import Play
    from ansible.playbook.play import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    def task_executor(host, task, task_vars):
        task_results = dict(changed=False, skipped=False, failed=False,
                            success_result=dict(ansible_facts=dict()))
        task_result = task_vars['result'].copy()
        task_results.update(task_result)
        task_results.pop('ansible_facts', None)
        return task_results

    inventory = InventoryManager(host_list='')
    variable_manager = VariableManager(loader="", inventory=inventory)

   

# Generated at 2022-06-13 09:57:25.118592
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    pass

# Generated at 2022-06-13 09:57:35.439691
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test case for the ActionModule.run method.
    """

    # modules parameter missing in config
    C.config = ConfigParser()
    C.CONFIG = C.config
    C.config.initialize_config()
    C.config.set_config_value('FACTS_MODULES', None, None)
    C.config.set_config_value('CONNECTION_FACTS_MODULES', None, None)

    # create the ActionModule object
    action_module = ActionModule(loader=None, task=None, connection=None, play_context=None, loader_cache=None, templar=None, shared_loader_obj=None)

    # temporary directory is needed during the
    # execution of the run method
    tmp_directory = 'tmp/'
    tmp = os.path.realpath

# Generated at 2022-06-13 09:57:44.678987
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    mock_module_utils_path = 'ansible_collections.ansible.netcommon.plugins.modules.utils'

    facts_module = ('ansible_collections.ansible.netcommon.plugins.modules.'
                    'network_cli.basics.get_default_route_facts')
    action_module = __name__ + '.ActionModule'
    module_loader = 'ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils'

    mock_connection = 'ansible_collections.ansible.netcommon.tests.unit.test_plugins.test_network_plugin.test_action_module.MockConnection'

    mock_ds = {'name': 'mock_ds'}

# Generated at 2022-06-13 09:57:52.374267
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run")
    task_vars = {
        'ansible_facts': {},
        'ansible_play_hosts': {
            'dark': {}
        },
        'ansible_hostname': 'dark',
    }
    task_vars['ansible_network_os'] = 'aos'
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action._task.args = { 'gather_subset': 'all' }
    action._task.args.pop('gather_subset', None)
    action._templar = None
    action._connection = None
    action._task = None

# Generated at 2022-06-13 09:57:59.994935
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    spec = {'args': {'filter': '*INTERFACE_NAME'}}
    task = MagicMock(name='task', spec_set=spec)

    config = MagicMock(name='config', spec_set=C.Config)
    config.DEFAULT_SUDO_USER = "root"
    config.DEFAULT_REMOTE_USER = "test"
    config.DEFAULT_SUBSET = "all"
    config.DEFAULT_TIMEOUT = 10
    config.ANSIBLE_CALLBACK_WHITELIST = []

    tmp = tempfile.mkdtemp()

# Generated at 2022-06-13 09:58:01.102020
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()

# Generated at 2022-06-13 09:58:07.594399
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.network import Facts
    mod_kwargs = {'gather_subset': 'all', 'gather_network_resources': ['interfaces']}
    module_mock = Facts()
    module_mock.run.return_value = {'ansible_interfaces': ['eth0', 'eth1']}

    set_module_args(mod_kwargs)
    am = ActionModule(module_mock, {})
    result = am.run(task_vars={'ansible_facts_parallel': True})
    assert result == {'ansible_facts': {'ansible_interfaces': ['eth0', 'eth1'], '_ansible_facts_gathered': True}, '_ansible_verbose_override': True}

# Generated at 2022-06-13 09:58:08.826803
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: not implemented
    assert False


# Generated at 2022-06-13 09:58:44.791406
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.executor.task_result
    import ansible.plugins.loader
    import ansible.template
    import ansible.vars

    task_result = ansible.executor.task_result.TaskResult()
    task_exec = ansible.executor.task_executor.TaskExecutor()
    action_module = ansible.plugins.action.ActionModule(task_exec, task_result)

    assert isinstance(action_module, object)
    assert isinstance(action_module, ansible.plugins.action.ActionBase)
    assert not hasattr(action_module, '_supports_check_mode')
    assert not hasattr(action_module, '_supports_async')
    assert not hasattr(action_module, '_shared_loader_obj')
    
    # test _get_module

# Generated at 2022-06-13 09:58:55.491208
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Play(object):
        def __init__(self, task_vars, connection):
            self._task = task_vars
            self._connection = connection

    from ansible.playbook.play_context import PlayContext

    pc = PlayContext()
    pc._connection = 'local'

    from collections import namedtuple

    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='local', module_path=None, forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
    templar = None

    from ansible import constants as C


# Generated at 2022-06-13 09:58:56.673484
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test for run of class ActionModule")

# Generated at 2022-06-13 09:58:59.872947
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test in class ActionModule the instantiation of variables.
    """
    # Test1: Create an instance of ActionModule
    action_module = ActionModule()

    # Test2: Test instantiation of variable self._supports_check_mode
    assert action_module._supports_check_mode is True


# Generated at 2022-06-13 09:59:08.681095
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    This is a test of the method _run of class ActionModule.
    It creates an object of the class and tests its execution on
    examples provided by the plugin builder in the action module.
    '''

    def get_connection():
        '''
        Create a mock connection to replace the connection
        of the action module.
        '''

        class MockConnection(object):
            '''
            Mock connection with attributes matching the real connection.
            '''

            def __init__(self, load_name):
                self._load_name = load_name

            def _shell(self):
                return _shell

            @property
            def transport(self):
                return "mock"

            @property
            def socket_path(self):
                return "/path/to/connection/socket"


# Generated at 2022-06-13 09:59:11.093730
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = {}
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module._supports_check_mode

# Generated at 2022-06-13 09:59:17.365809
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # instantiate
    module = ActionModule()

    # As there is no real ansible connection we need to mock the execute_module
    module._execute_module = lambda *_, **__: dict(ansible_facts=dict())

    # We need to mock the result of find_plugin_with_context as well
    class fake_plugin(object):
        def __init__(self):
            self.resolved_fqcn = 'fake_plugin'
    module._shared_loader_obj.module_loader.find_plugin_with_context = lambda module, collection_list: fake_plugin()

    # No specific test_run implementation for now.
    # Just test that it does not make the whole testsuite explode
    module.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 09:59:18.407895
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)


# Generated at 2022-06-13 09:59:32.014798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of ActionModule
    am = ActionModule()

    # Create a mock object
    m = MagicMock()

    # Cast it as a ResultCallback
    rc = cast(ResultCallback, m)

    # Tell the mock to return a pre compeleted job
    rc._job_results.append({
        'finished': 1,
        'ansible_job_id': '93412673-50b7-4455-a969-7d3d1614d6c1',
        'ansible_facts': {'fact_module_version': '0.0'}
    })

    # Assing the mock object to results_callback
    am.results_callback = rc

    # Create a task and set the arguments
    task = Task()

# Generated at 2022-06-13 09:59:40.237325
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    # unit test without facts
    action_mod = ActionModule()
    result = action_mod.run()
    assert result['ansible_facts'] == {}
    assert result['ansible_facts']['_ansible_facts_gathered'] == True

    # unit test with simple list of facts
    action_mod = ActionModule()
    action_mod._task = {'args': {'gather_subset': ['all']}}
    result = action_mod.run()
    assert result['ansible_facts'] != {}
    assert result['ansible_facts']['_ansible_facts_gathered'] == True
    assert 'ansible_distribution' in result['ansible_facts']

    # unit test with smart facts
    action_

# Generated at 2022-06-13 10:00:37.187228
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None, None)  # noqa: F841

# Generated at 2022-06-13 10:00:41.468775
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule().run(tmp=None, task_vars=None) == {'ansible_facts': {}, 'ansible_facts_raw': {}, 'skipped': True}  # tests if ansible.module_utils is imported

# Generated at 2022-06-13 10:00:48.886645
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Unit test needs to import some of the deprecated modules in order to test them.
    # Using ignore because these modules are not used by the plugin.
    # pylint: disable=import-error,unused-import
    import ansible.modules.legacy.setup
    import ansible.modules.legacy.system
    import ansible.modules.system.setup
    import ansible.modules.network.cli.setup
    import ansible.modules.network.network_cli.setup
    import ansible.modules.network.httpapi.setup

    # Mock the available modules.
    def _fqcn(x):
        return x
    ansible.modules.legacy.setup.__resolved__ = _fqcn
    ansible.modules.legacy.system.__resolved__ = _fqcn
    ansible.modules.system

# Generated at 2022-06-13 10:00:50.075584
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()

# Generated at 2022-06-13 10:00:58.013314
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display

    loader = DataLoader()

    test_task = Task()
    test_task._role = None
    test_task.action = 'setup'
    test_task.args = {'filter': 'ansible_distribution', 'gather_subset': ['all']}
    test_task.task

# Generated at 2022-06-13 10:01:01.815568
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule()
    tmp = None
    task_vars = None
    result = actionModule.run(tmp, task_vars)
    assert(result['ansible_facts']['_ansible_facts_gathered'])

# Generated at 2022-06-13 10:01:10.411540
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule({'name': 'setup', 'module_defaults': dict()})
    module.HOST_VARS.update({'ansible_module_generated': False})
    module._supports_async = True

# Generated at 2022-06-13 10:01:16.271863
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    mod.set_loader()
    mod._shared_loader_obj.module_loader.find_plugin_with_context = lambda module_name, collection_list: ('TestModule', 'TestCollection')

    mod._task.args = {'testarg1': 'arg1', 'testarg2': 'arg2'}
    mod._task.module_defaults = {'testarg1': 'arg1', 'testarg2': 'arg2'}
    mod._task._parent = None
    mod._task._parent._play = None
    mod._task._parent._play._action_groups = None
    res = mod.run()

    assert '_ansible_facts_gathered' in res['ansible_facts']

# Generated at 2022-06-13 10:01:18.433687
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule._get_module_args('ping', {'ping': {'a': '1'}}) == {'a': '1'}

# Generated at 2022-06-13 10:01:23.313887
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    a = {'a': 1, 'b': 2, 'c': "3"}
    b = {'c': 3, 'd': 4, 'e': "5"}
    assert mod._combine_task_result(a, b) == {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': "5"}

# Generated at 2022-06-13 10:03:40.128275
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import connection_loader

    class TestPlaybookExecutor(PlaybookExecutor):

        def __init__(self, inventory, variable_manager, loader, options, passwords, stdout_callback=None):
            super(TestPlaybookExecutor, self).__init__(inventory, variable_manager, loader, options, passwords)
            self._stdout_callback = stdout_callback
            self._prompt = None

        def get_host_list(self):
            return ['localhost']

        def get_hosts_remaining(self, play):
            return ['localhost']


# Generated at 2022-06-13 10:03:40.918851
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:03:53.041082
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    class ActionModule(object):
        def __init__(self):
            self.async_val = None
            self.job_id = 1

    class TestVars(object):
        def get(self, value, default=None):
            return default

    def match_hostname(pattern, name=None):
        if not pattern:
            pattern = 'all'
        return name == "test"

    def find_plugin_with_context(self, name, collection_list=None):
        class ResolvedFqcn(object):
            def __init__(self):
                self.resolved_fqcn = "resolved fqcn"

        return Resolved

# Generated at 2022-06-13 10:03:53.590289
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 10:04:01.944006
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod_args = {'my_param': 'my_value'}
    tmp_path = '/path/to/tmp'

    # simple test to see if the class can be instantiated
    action_module = ActionModule(None, dict(), mod_args)

    # check if the run method is executing properly
    task_vars = {'ansible_facts': {}, 'ansible_facts_parallel': None, 'ansible_facts_gathered': True}
    res = action_module.run(tmp_path, task_vars)
    assert 'ansible_facts' in res
    assert res['ansible_facts'] == {}

    # check if the run method is executing properly in the case of legacy facts modules

# Generated at 2022-06-13 10:04:07.002293
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    mod._supports_check_mode = True

    res = mod.run(C, {})
    assert res['ansible_facts'] == {'_ansible_facts_gathered': True}

    # Test with a real task_vars
    res = mod.run(C, {'test': 'test'})
    assert res['ansible_facts'] == {'_ansible_facts_gathered': True}


# Generated at 2022-06-13 10:04:17.064198
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult

    # Setup for the test
    tmp = '/tmp/ansible-tmp'
    task_vars = dict()
    task_vars['ansible_facts'] = dict()
    connection_load_name = 'network_cli'
    # task_vars['ansible_facts']['network_os'] = 'cisco_ios'
    task_vars['ansible_facts']['network_os'] = 'aruba_os'
    modules = ['smart']
    connection_map = dict()
    connection_map['cisco_ios'] = 'cisco.ios.setup'
    connection_map['aruba_os'] = 'arubaoss.arubaoss_facts'

    C.CON

# Generated at 2022-06-13 10:04:18.196345
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    c = ActionModule()
    c.run()
    assert False


# Generated at 2022-06-13 10:04:28.914455
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {'ansible_facts': {}}
    task_vars['ansible_facts']['network_os'] = "junos"

    modules = ['ansible.legacy.setup']
    parallel = True
    message = "The following modules were skipped: %s\n" % (', '.join(modules.keys()))
    connection_map = {}
    connection_map["junos"] = 'ansible.legacy.setup'
    connection_map["ios"] = 'ansible.legacy.setup'
    connection_map["ios-xr"] = 'ansible.legacy.setup'
    connection_map["juniper_junos"] = 'ansible.legacy.setup'


# Generated at 2022-06-13 10:04:40.227100
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = AnsibleModule(
        argument_spec={
            'parallel': {'type': 'bool', 'default': False},
            'network_os': {'type': 'str', 'default': None}
        }
    )

    # mock connection plugins
    class MockConnectionPlugin(object):
        def __init__(self):
            self._shell = None
        def get_name(self):
            return 'ssh'
        def get_connection_info(self):
            return None
        def get_shell(self):
            if self._shell == None:
                self._shell = MockShell()
            return self._shell
        def get_option(self, name):
            return None
