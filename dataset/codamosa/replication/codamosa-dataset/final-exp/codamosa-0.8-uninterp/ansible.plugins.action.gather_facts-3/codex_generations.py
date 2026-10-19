

# Generated at 2022-06-13 09:55:25.625898
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module.configure()
    assert module.run() == {}

# Generated at 2022-06-13 09:55:37.997140
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit tests for method run of class ActionModule."""
    import sys
    import unittest
    from unittest import mock

    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves import StringIO

    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.action import ActionBase

    class TestActionModule(ActionModule):
        def __init__(self, *args, **kwargs):
            super(TestActionModule, self).__init__(*args, **kwargs)


# Generated at 2022-06-13 09:55:47.618105
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    at = MockAction()

# Generated at 2022-06-13 09:55:49.043520
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 09:56:00.167026
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {
        'ansible_network_os': 'ios'
    }
    modules = ['ios_facts', 'ios_commands']
    result = {
        'ansible_facts': {
            '_ansible_facts_gathered': True,
            'ansible_network_os': 'ios'
        }
    }
    config = {
        'FACTS_MODULES': [
            'ansible.legacy.basic_facts',
            'ansible.legacy.network_facts',
            'smart',
            'ansible.legacy.local_facts',
        ],
        'CONNECTION_FACTS_MODULES': {
            'ios': 'ios_facts',
            'ios_commands': 'ios_commands'
        }
    }

# Generated at 2022-06-13 09:56:01.361173
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise NotImplementedError

# Generated at 2022-06-13 09:56:11.232591
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.errors
    import ansible.playbook.task

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    # create test object
    am = ActionModule()

    # create mock objects
    # create mock config and set it to C.config for testing
    config = {'FACTS_MODULES': ['setup']}

# Generated at 2022-06-13 09:56:11.929577
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    pass

# Generated at 2022-06-13 09:56:24.028601
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    # hosts = [
    #     '123.123.123.123',
    #     'localhost',
    #     'server1',
    # ]

    # inventory = Inventory(loader=None, variable_manager=None, host_list='/tmp/hosts')

    # play_source = {'name': 'facts',
    #                'hosts': 'all',
    #                'gather_facts': 'no',
    #                'tasks': [
    #                    {
    #                        'name': 'setup',
    #                        'action': {
    #                                'module': 'setup',
    #                        }
    #

# Generated at 2022-06-13 09:56:36.045855
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display

    class FakeV2Task():
        def __init__(self, test_args):
            self.args = test_args
            self.module_defaults = {}
            self._parent = self
            self._action_groups = {}
            self.collections = {}

    class FakeV2Play():
        def __init__(self):
            self._action_groups = {}

    class FakeV2PlayContext():
        def __init__(self):
            pass

    class FakeV2Loader():
        def __init__(self):
            self.module_loader = FakeV2ModuleLoader

# Generated at 2022-06-13 09:56:57.205763
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # set up test environment
    tmp = tempfile.mkdtemp()
    task_vars = {'ansible_facts': {'network_os': None}}

    # set up module args
    args = {
        'ansible_facts': 'default',
        'parallel': True,
    }

    # set up mocks
    def _execute_module(module_name, module_args, task_vars, wrap_async):
        module_name == 'smart'
        module_args == '{}'
        task_vars == {'ansible_facts': {}}
        wrap_async == False

        res = {}
        return res

    am = ActionModule()
    am._task = mock.MagicMock()
    am._task.args = args
    am._task.module_defaults = {}


# Generated at 2022-06-13 09:57:05.434567
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    import ansible.utils.vars as vars

    play_context = PlayContext()
    task = Task()
    task._parent = Play()
    task_executor = TaskExecutor(play=task._parent, task=task, connection='connection', play_context=play_context, loader=None, templar=None)
    result = ActionModule(task_executor, 'some_action', 'my_arg=3', '/some/path/to/file', 'foo', 'some_value', 'some_other_value=4')

    assert result._supports_check_mode == True

   

# Generated at 2022-06-13 09:57:11.776519
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.executor import module_executor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = variable_manager.loader
    variable_manager._extra_vars = ImmutableDict(
        {u'hostvars': {u'127.0.0.1': {u'ansible_winrm_server_cert_validation': u'ignore'}}})

# Generated at 2022-06-13 09:57:23.081021
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Failed modules
    f_m = dict(key1="value1", key2="value2")

    # Skipped modules
    s_m = dict(key1="value1", key2="value2")

    action = ActionModule()

    # Parallel is none and len(modules) >= 1
    # Result with finished == 1, failed == False, skipped == False
    result = dict(ansible_job_id="ansible_job_id_1", finished=1, _ansible_no_log="_ansible_no_log_1", results_file="results_file_1", key1="value1", key2="value2")

    # Result with finished == 0

# Generated at 2022-06-13 09:57:34.204454
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('\nTest01.test_ActionModule_run\n')

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    import ansible.executor.task_queue_manager
    import ansible.plugins.loader
    import ansible.utils.vars
    import copy

    # Load the playbook to test module
    loader = ansible.plugins.loader.PluginLoader()
    playbook = loader.load_from_file('/home/qb/Ansible/tasks/action_plugins/setup.yml')

    # Load the task to test module
    play = playbook[0]
    loader = ansible.plugins.loader.ActionModuleLoader()

# Generated at 2022-06-13 09:57:35.688122
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Create a test action plugin module."""
    mod = ActionModule()

    assert mod._supports_check_mode is True

# Generated at 2022-06-13 09:57:44.904197
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(None, None)

    def _execute_module(module_name, module_args, task_vars, wrap_async):
        return {
            'ansible_facts': {
                '_ansible_fact_async_dir': '/some/path/ansible_fact_gathering_setup_1',
                '_ansible_fact_gathering_setup_time': 15.66,
            },
            'ansible_job_id': '229695523528.4016',
            'changed': False,
            'results_file': '/some/path/ansible_fact_gathering_setup_1/229695523528.4016',
            'task_args': {
            },
        }

    def _remove_tmp_path(tmp_path):
        pass

    action

# Generated at 2022-06-13 09:57:50.840453
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    module_name = 'setup'
    module_args = {}
    result = {'ansible_facts': dict(), 'warnings': list(), 'deprecations': list()}
    task_vars = dict()
    res = dict()
    res['failed'] = False
    res['skipped'] = False
    task_result = {'ansible_facts': dict(), 'warnings': list(), 'deprecations': list()}
    result = action_module._combine_task_result(result, task_result)
    print(result)
    task_vars['ansible_facts_parallel'] = True
    modules = ['setup']

# Generated at 2022-06-13 09:57:51.951557
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()

# Generated at 2022-06-13 09:57:54.916190
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = module_executor.ActionModule(name='test', task=1)
    assert m.task == 1
    assert m.task_vars == {}
    assert m.tmp == ''
    assert m._templar == None
    assert m._name == 'test'

# Generated at 2022-06-13 09:58:28.012613
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    adict = dict(
        ansible_facts={},
        ansible_facts_parallel=None,
        msg=None,
        skipped=None,
        skipped_modules=None,
        failed=None,
        failed_modules=None,
    )

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    foo = AnsibleUnsafeText(b"foo")
    bar = AnsibleUnsafeText(b"bar")

    task_vars = dict(
        ansible_facts=dict(
            network_os=bar,
        ),
    )

    task = dict(
        args=dict(),
    )

    from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-13 09:58:38.579106
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # This causes a stack trace, unable to access class member variables
    # from pytests
    # C.config.ANSIBLE_CACHE_PLUGIN_TIMEOUT = 0
    src = '127.0.0.1'
    play_context = dict(
        become=False,
        become_user='',
        become_method='sudo',
        connection='netconf',
        diff=False,
        forks=100,
        remote_port=None,
        transport='ssh',
        verbosity=True,
        port=0,
    )
    display = dict(
        verbosity=True,
    )
    # task_vars = dict(
    #     ansible_connection='netconf',
    #     ansible_network_os='iosxr',
    #     ansible_user='cisco',


# Generated at 2022-06-13 09:58:47.052319
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock objects - removed for now

    # Test function with valid args / params.
    for parallel in (True, False):
        for fact_module in ('setup', 'fetcher'):
            result = am.run(task_vars={'ansible_facts_parallel': parallel},
                            tmp={},
                            task_vars={'ansible_facts': {}})
            # The test below is the only one I can think of.
            assert isinstance(result, dict)
            assert 'ansible_facts' in result
            assert '_ansible_facts_gathered' in result['ansible_facts']
            assert '_ansible_verbose_override' in result
            assert 'skipped' not in result
            assert 'skipped_modules' not in result
            assert 'failed' not in result

# Generated at 2022-06-13 09:58:55.734833
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fake_task = dict(
        module_defaults=dict(gather_subset=None, gather_network_resources=None, filter=None)
    )
    task_vars = dict(
        ansible_local=dict(
            ansible_facts=dict(
                ansible_facts_dir=None,
                ansible_facts_gathered=None
            )
        )
    )
    action_module = ActionModule(fake_task, None)
    result = action_module.run(task_vars=task_vars)
    assert result['ansible_facts']['_ansible_facts_gathered']

# Generated at 2022-06-13 09:58:56.849472
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert(am is not None)


# Generated at 2022-06-13 09:58:58.460643
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ This is a sample test to show that the constructor is working """
    am = ActionModule()
    assert am is not None


# Generated at 2022-06-13 09:59:04.878443
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # set up for testing the constructor and properties of class ActionModule
    action = ActionModule(None, None)

    assert action.module_name == 'setup'
    assert action._supports_check_mode is True
    assert action._supports_async is True
    assert action._connection is None
    assert action._task is None
    assert action._loader is None
    assert action._templar is None
    assert action._shared_loader_obj is None
    assert action._display is None
    assert action._task_keys is None
    assert not action._supports_async

# Generated at 2022-06-13 09:59:12.501904
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = {'args': {'test_arg': 'test'}}
    test_connection = {'_shell': {'tmpdir': 'test'}}
    test_task_vars = {'test_var': 'test'}
    test_inject = {'test_inject': 'test'}
    test_plugin_class = 'test'
    test_plugin_deps = ['test', 'test']
    test_templar = 'test'
    test_shared_loader_obj = 'test'

    # test constructor with default values
    action_module = ActionModule(task, test_connection, test_templar, test_shared_loader_obj)
    assert action_module._task == task
    assert action_module._connection == test_connection
    assert action_module._templar == test_templar

# Generated at 2022-06-13 09:59:18.769709
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    loader = DictDataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'ansible_facts':{'ansible_network_os': 'cisco_ios'}}
    tasks = [{"action":{"__ansible_module__": "cisco_ios_facts"}, "name": "test", "async": 1, "poll": 10}]
    task_results = [{'ansible_job_id': 1, 'finished': 1, '_ansible_parsed': True, 'results_file': '/home/foo/test'}]
    connection_results = [{'ansible_facts': {}}]
    inventory = Inventory([], loader=loader, variable_manager=variable_manager)
    connections = MockConnection(task_results, connection_results)

# Generated at 2022-06-13 09:59:32.284867
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.vars import merge_hash
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.action.setup import ActionModule as Setup

    fake_task_vars = dict(ansible_connection='local', connection='local', module_name='setup', module_defaults=dict(gather_timeout=10))
    fake_task = Setup(plugin_loader = PluginLoader(), task=dict(name='setup'))
    assert fake_task._supports_check_mode == True
    fake_result = super(Setup, fake_task).run('', fake_task_vars)
    assert fake_result['ansible_facts'] == {}


# Generated at 2022-06-13 10:00:30.414212
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(action=dict(module_name='debug', module_args=dict(msg='Hello World'))),
        connection=dict(module_name='local', host=dict(name='localhost')),
        play_context=dict(check_mode=False, diff=False),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    assert action_module is not None



# Generated at 2022-06-13 10:00:36.797578
# Unit test for constructor of class ActionModule
def test_ActionModule():

    action_module = ActionModule()

    class_name = 'ActionModule'
    assert class_name in str(action_module), 'class_name not in str(action_module)'

    assert isinstance(action_module._supports_check_mode, bool)
    assert isinstance(action_module._connection, ActionBase)
    assert isinstance(action_module._task, ActionBase)
    assert isinstance(action_module._loader, ActionBase)
    assert isinstance(action_module._templar, ActionBase)
    assert isinstance(action_module._shared_loader_obj, ActionBase)
    assert isinstance(action_module._display, ActionBase)

# Generated at 2022-06-13 10:00:41.014115
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Tests for `ActionModule` class"""

    # Run unit test for constructor of class ActionModule
    try:
        test = ActionModule()
        print("Success")
    except Exception:
        print("Error: Instantiation of class ActionModule failed")

# Generated at 2022-06-13 10:00:45.677602
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:00:47.319156
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create instance of ActionModule
    myTest = ActionModule.test()


test_ActionModule()

# Generated at 2022-06-13 10:00:48.117116
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule, object)

# Generated at 2022-06-13 10:00:57.091176
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    connection = {
        "network_os": "network_os_not_defined",
        "persistent_connection": True,
        "remote_addr": "8.8.8.8",
        "remote_user": "ansible",
        "become_method": "None",
        "become_user": "None"
    }
    task = {
        "action": "my.custom.action",
        "delegate_to": "localhost",
        "tags": [],
        "run_once": True,
        "environment": {},
        "args": {
            "gather_subset": "all",
            "filter": "filter_is_not_defined"
        }
    }

# Generated at 2022-06-13 10:01:07.234050
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # As documented in the ActionBase class, the constructor of an action plugin
    # will only accept 2 parameters, a task and a connection.

    # As part of the initialization of the ActionModule, it will set the task_vars,
    # templar and the _supports_check_mode flags, so we need to make sure that there
    # is a TaskExecutor instance in the task to get the needed variables and flags.
    task_executor = TaskExecutor()

    # The same goes for the connection, we need to have a Connection object to set
    # _shell and _shell_type for the ActionModule constructor to not fail.
    connection = Connection(MagicMock())

    # As the constructor of the ActionModule class will call the super constructor
    # of the parent class, that is, the ActionBase class, we need to pass a task and
    #

# Generated at 2022-06-13 10:01:10.952001
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of the ActionModule class
    action_module = ActionModule()

    # Test attributes of ActionModule
    assert action_module._supports_check_mode is True


# Generated at 2022-06-13 10:01:11.731947
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:03:29.232689
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.utils.vars
    import ansible.executor.module_common
    from ansible.utils.vars import merge_hash
    from ansible.executor.module_common import get_action_args_with_defaults

    am = ActionModule()
    assert am
    assert isinstance(am, ActionModule)
    assert callable(am.run)
    assert isinstance(am._display, ansible.utils.display.Display)
    assert isinstance(am._shared_loader_obj, ansible.parsing.dataloader.DataLoader)
    assert isinstance(am._templar, ansible.parsing.yaml.objects.AnsibleTemplar)
    assert merge_hash
    assert get_action_args_with_defaults

test_ActionModule()

# Generated at 2022-06-13 10:03:41.989696
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # First test case: test run with a single module
    test_result1 = {}
    test_result1['changed'] = False
    test_result1['ansible_facts'] = {'_ansible_facts_gathered': True, 'ansible_facts': {'test_fact': 'test_value'}, '_ansible_verbose_override': True}
    module1 = 'test_module1'

    async_poll_result = {'finished': 1, 'ansible_facts': {'test_fact_2': 'test_value_2'}}

    test_task = {}
    test_task['args'] = {'test_arg': 'test_value'}

    class MockTask(object):
        def __init__(self):
            self.args = {}

    test_task_obj = MockTask()



# Generated at 2022-06-13 10:03:52.946635
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class FakeTask(object):
        def __init__(self, args={}):
            self.args = args
            self.action = 'setup'
            self.fail_json = True

    class FakeModuleLoader():
        def __init__(self, collection_list):
            self.collection_list = collection_list

        def find_plugin_with_context(self, fact_module, collection_list):
            class FakeModule(object):
                def __init__(self, resolved_fqcn):
                    self.resolved_fqcn = resolved_fqcn

            return FakeModule('fake_module')

    class FakeConnection(object):
        _load_name = 'fake'

        def __init__(self):
            self.tmpdir = 'fake_tmp'


# Generated at 2022-06-13 10:03:57.626103
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import sys
    import unittest
    from ansible.errors import AnsibleAction, AnsibleActionFail
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins.action import ActionBase
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.path import mock_unfrackpath_success

    class AnsibleModule_Mocked(object):
        def __init__(self, argument_spec, bypass_checks=False):
            self.argument_spec = argument_spec
            self

# Generated at 2022-06-13 10:04:04.453517
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create a mock task to hold the module def
    # and the args to present to the module
    class Task(object):
        def __init__(self):
            self.module_defaults = {}
        args = {}

    class MockedModule(object):
        def __init__(self):
            self.task = Task()

    class MockedExecutor(object):
        class MockedConnection(object):
            def __init__(self):
                self.tmpdir = "/tmp/ansible-tmp"
                self._shell = None
                self._shell_obj = MockedShell()
                self._connection_plugin_name = 'mocked_connection'

            def _shell_plugin_name(self):
                return 'mocked_shell'

        connection = MockedConnection()

        def __init__(self):
            self._

# Generated at 2022-06-13 10:04:06.645375
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    action = ActionModule()
    action.tmp = '/tmp/'
    action.task_vars = {}
    action.tmpdir = '/tmp/'

    action.run()

# Generated at 2022-06-13 10:04:16.595583
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("")
    # Instantiate mock module
    module = MockModule()

    # instantiate action plugin
    action = ActionModule()

    # Imitate injection of a connection to handle all the network_cli and network_os processing
    action._connection = connection = MockConnection()
    connection._shell = MockShell()

    # instantiate shared loader obj for action plugin
    shared_loader = module._shared_loader_obj = MockSharedLoader()

    # instantiate display for capturing output
    display = action._display = MockDisplay()

    # Instantiate AnsibleConfig for connection options processing
    config = MockConfig()

    # Instantiate AnsibleRunner for running modules
    runner = MockRunner()

    # Instantiate TaskExecutor for the running the tasks
    executor = MockTaskExecutor()

    # Instantiate Templer for template processing
    templer = Mock

# Generated at 2022-06-13 10:04:23.003036
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import module_loader
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_bytes
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.process.worker import WorkerProcess
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from collections import namedtuple
    from ansible.utils.vars import combine_vars

# Generated at 2022-06-13 10:04:28.652238
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = {}
    task_vars = {}
    templar = None
    loader = None
    task = None
    connection = None
    play_context = None
    new_stdin = None
    handler = None
    action = ActionModule(task, connection, play_context, loader, templar, 
                          module_args, new_stdin, handler)
    assert action

# Generated at 2022-06-13 10:04:29.099972
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass