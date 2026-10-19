

# Generated at 2022-06-13 09:55:30.052262
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # This method is tested via the integration test here:
    # https://github.com/ansible/ansible/blob/stable-2.9/test/integration/targets/module_defaults/tasks/test.yml
    # See F264
    pass

# Generated at 2022-06-13 09:55:32.196680
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of ActionModule class
    actionModule = ActionModule()

    #TODO:
    pass

# Generated at 2022-06-13 09:55:37.237675
# Unit test for constructor of class ActionModule
def test_ActionModule():
    local_facts = {
        'ansible_os_family': 'RedHat',
    }
    task_vars = {
        'ansible_facts': local_facts
    }

    am = ActionModule('mock_action', {}, tmp='mock_tmp', task_vars=task_vars, loader=None, templar=None)

    assert am is not None
    assert am._templar is not None
    assert am._task_vars is not None

# Generated at 2022-06-13 09:55:47.023607
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.strategy.linear import StrategyModule

    # Setup
    my_loader = DummyLoader()
    my_results_callback = DummyResultsCallback()
    my_inventory = InventoryManager(loader=my_loader)
    variable_manager = VariableManager(loader=my_loader, inventory=my_inventory)
    variable_manager._extra_vars = {'hostvars': {'host1': {}}}
    variable_manager._vars_per_host = {'host1': variable_manager.get_vars(play=None, host=my_inventory.get_host('host1'))}

    execute_module_func = D

# Generated at 2022-06-13 09:55:53.689585
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('start the test')

    my_task_vars = {
        'ansible_facts_parallel': 'False',
        'ansible_network_os': 'a10'
    }

    with ActionModule(task={'args': {'network_os': 'a10'}}, task_vars=my_task_vars) as my_action_module:
        result = my_action_module.run(tmp='', task_vars=my_task_vars)

    print('here is the result')
    print(result)

test_ActionModule_run()

# Generated at 2022-06-13 09:55:59.712668
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import module_loader
    from ansible.vars.manager import VariableManager
    from ansible.vars.persistent import PersistentVars

    class TestTaskResult(TaskResult):

        def __init__(child):
            super(child.__class__, child).__init__(host=None, task=None, task_fields=dict())
            child.host = 'host1'

# Generated at 2022-06-13 09:56:10.850841
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # it is not possible to run this method without some pytest fixtures so I'm just writing these simple test with random values
    task = {
        'id': 'a1e6667d-1722-4bcb-8b81-a8a7f2e9c973',
        'name': 'setup',
        'action': 'setup',
        'args': {},
        'local_action': 'setup',
        'playbook_parser': 'YAML',
        'version_added_major': 2,
        'version_added_minor': 3,
        'version_added_revision': 0
    }
    ans_action_module = ActionModule(task=task, connection=None, out_callback=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 09:56:23.196036
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest

    class TestActionModule(unittest.TestCase):
        def test_ActionModule(self):
            from ansible import constants as C

            # set constants so we can skip actually running the module
            C._MODULE_COMMON_SKIP_MSG = 'skip_message'
            C._MODULE_COMMON_SKIPPED = True
            task_vars = fetch_vars()
            task_vars.update({'ANSIBLE_NET_USERNAME': 'dummy_user', 'ANSIBLE_NET_PASSWORD': 'dummy_pass'})
            inject = {'ansible_facts_kind': 'default',
                      'ansible_facts': {'network_os': 'iosxr'}}
            result = {}
            task_vars.update(inject)
            instance = ActionModule

# Generated at 2022-06-13 09:56:30.760611
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.common.parameters import ModuleParameters
    from ansible.executor.module_common import get_action_args_with_defaults
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.network.common.utils import get_module_resource
    from ansible.plugins.action import ActionBase
    from ansible.utils import vars
    modules = ['ping', 'setup']

# Generated at 2022-06-13 09:56:36.288083
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict(connection="network_cli", gather_subset="all")
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = am.run(tmp=None, task_vars=task_vars)
    assert result["ansible_facts"] == {}

# Generated at 2022-06-13 09:56:56.600618
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import modules
    from ansible.plugins.action import ActionModule
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.vars import combine_vars

    # For test case we will use the modules we have in our library
    # to test the run method of class ActionModule
    module_loader = AnsibleCollectionLoader()
    module_loader.set_options(config={}, context={}, collections_paths=['/usr/share/ansible/collections/ansible_collections'] )
    module_utils_loader = module_loader._get_loader([os.path.abspath('/usr/share/ansible/collections/ansible_collections/ansible/utils')])

    # Create an instance of ActionModule

# Generated at 2022-06-13 09:56:59.971633
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(None, None)
    result = action_module.run(None, None)

    assert result['ansible_facts']['_ansible_facts_gathered'] == True

# Generated at 2022-06-13 09:57:06.738433
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m_ActionBase_run = actionbase.ActionBase._run
    m_execute_module = actionbase.ActionBase._execute_module

    class FakeActionBase(actionbase.ActionBase):
        def __init__(self):
            self._task_vars = {}
            self._display = None
            self._task = MagicMock()
            self._task.args = {}
            self._task.module_defaults = {}
            self._templar = MagicMock()
            self._connection = MagicMock()
            self._connection._shell.tmpdir = '/tmp'
            self._connection._load_name = 'network_cli'
            self._shared_loader_obj = MagicMock()
            self._shared_loader_obj.module_loader.find_plugin_with_context.return_value.resolved_fqcn

# Generated at 2022-06-13 09:57:14.687070
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import os
    import re
    import tempfile
    import pytest

    from ansible.module_utils.facts.virtual.sysinfo import VirtualInfo
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import LinuxDistribution

    from ansible.module_utils.facts.system.distribution import get_distribution
    from ansible.module_utils.facts.system.distribution import Network

    from ansible.plugins.action.setup import ActionModule

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext

# Generated at 2022-06-13 09:57:24.919696
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    This method is used to unit test method run of class ActionModule.
    """
    task_vars = {'test': 'test'}
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    module._supports_check_mode = True
    module._connection = {'_shell': {'tmpdir': None}}
    module._shared_loader_obj = {'module_loader': {'find_plugin_with_context': {'resolved_fqcn': None}}}

    module._task = {'args': {'parallel': None, 'network_os': 'network_os'}, 'collections': ['collections'], 'module_defaults': None}

# Generated at 2022-06-13 09:57:35.336736
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Mock up a task, action and connection
    task = dict()
    action = dict(module_defaults=dict(),
                  failures=dict(),
                  retries=dict())
    task_vars = dict()
    connection = dict()
    connection['_shell'] = dict(tmpdir=dict(path=dict(name='/tmp')))

    action_module = ActionModule(task, action, connection,
                                 constants=dict(), module_loader=dict(),
                                 loader=dict(), templar=dict(), shared_loader_obj=dict())
    assert action_module is not None
    assert action_module._supports_check_mode is True

    task = dict()
    action = dict(module_defaults=dict(),
                  failures=dict(),
                  retries=dict())
    task_vars = dict()
    connection

# Generated at 2022-06-13 09:57:44.613217
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    conn = MagicMock()
    conn._load_name = 'network_cli'
    _shared_loader_obj = Mock()
    task_vars = {'ansible_connection': 'netconf'}
    _task_vars = dict()
    _loader = None
    _wrapped_task = Mock()
    _templar = MagicMock()
    _display = MagicMock()
    _task = Mock()
    _task.args = dict()
    _task.module_defaults = dict()
    _task._parent = Mock()
    _task._parent._play = Mock()
    _task._parent._play._action_groups = dict()

# Generated at 2022-06-13 09:57:52.372290
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # Patch super class
  mock_ActionBase_run = MagicMock()
  with patch.object(ActionModule, 'run', mock_ActionBase_run):
    mock_ActionModule_run = MagicMock()
    with patch.object(ActionModule, '_get_module_args', mock_ActionModule_run):
      mock_ActionModule_run = MagicMock()
      with patch.object(ActionModule, '_combine_task_result', mock_ActionModule_run):
        mock_ActionModule_run = MagicMock()
        with patch.object(ActionModule, '_execute_module', mock_ActionModule_run):
          mock_tmp=None
          mock_task_vars=None
          action_module = ActionModule()
          action_module.run(mock_tmp, mock_task_vars)



# Generated at 2022-06-13 09:57:54.483605
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()

    expected_result = {
        'ansible_facts': {
            '_ansible_facts_gathered': True
        },
        '_ansible_verbose_override': True,
    }

    result = mod.run(tmp=None, task_vars={})

    assert result == expected_result

# Generated at 2022-06-13 09:58:02.164501
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock the action module
    mock = ActionModule()
    # create a mock object for args
    class Args:
        parallel = None
        network_os = None
    # create a mock object for task
    class Task:
        args = Args()
    # create a mock object for task_vars
    task_vars = {'ansible_facts': {'network_os': 'junos' }, 'ansible_network_os': 'junos'}
    # mock the result

# Generated at 2022-06-13 09:58:24.545646
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act = ActionModule()
    assert act is not None

# Generated at 2022-06-13 09:58:31.645382
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        # Test to create an ActionModule object
        am = ActionModule()
        assert (str(type(am)) == "<class 'ansible.plugins.action.setup.ActionModule'>")

    except Exception as e:
        print('Failed to create ActionModule object: %s' % str(e))
        return False

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 09:58:40.305007
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible import context
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    context.CLIARGS = context.CLIARGS._replace(verbosity=3, connection='local')

    setting_up_task_manager = TaskQueueManager(
        inventory=None,
        variable_manager=VariableManager(),
        loader=None,
        options=context.CLIARGS,
        passwords=None,
        stdout_callback='default',
    )

    MODULE_ARGS = {'gather_subset': ['!all', 'min'], 'gather_network_resources': ['interfaces', 'vlans', 'facts']}

# Generated at 2022-06-13 09:58:40.981885
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:58:45.110235
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def __new__(arg1):
        return None

    def __init__(arg1):
        pass

    # Set up class mock.
    ActionModule = __new__
    ActionModule.__new__ = __new__
    ActionModule.__init__ = __init__
    ActionModule.run = run

    action_module = ActionModule()
    action_module.run()

# Generated at 2022-06-13 09:58:55.833168
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:59:02.626160
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(
            action=dict(
                module_name='ping',
                module_args=dict(
                    foo='bar',
                ),
                module_defaults=dict(
                    args=dict(
                        default=dict(
                            foo='bar',
                        ),
                    ),
                ),
            ),
            task_vars=dict(
                foo='bar',
            ),
            args=dict(
                foo='bar',
            ),
        ),
        connection=dict(),
        play_context=dict(
            gather_facts='no',
            verbosity=10,
        ),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict(),
    )
    print(module)

# Generated at 2022-06-13 09:59:10.927292
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import pytest
    import os
    import pprint
    import sys
    import ansible.constants as constants
    import ansible.executor.task_result as tr
    import ansible.module_utils.common.collections as collections
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.task.setup_facts_cache import ActionModule as Am
    from ansible.utils.vars import merge_hash
    from ansible.executor.action_plugins.setup import ActionModule as Am1

    class FakeConnection:
        class Shell:
            def __init__(self, tmpdir):
                self.tmpdir = tmpdir

        def __init__(self, load_name):
            self._load_name = load_name

# Generated at 2022-06-13 09:59:11.655421
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()


# Generated at 2022-06-13 09:59:18.150925
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import sys

    # This is just a stub that returns a fixed result.
    class StubConnection:
        class _shell:
            def __init__(self, tmpdir):
                self.tmpdir = tmpdir

        def __init__(self, load_name):
            pass

        def _load_name(self):
            return 'network_cli'

        def get_options(self):
            return {'_shell': self._shell('/tmp')}

    class StubTask:
    
        def __init__(self, args, module_defaults, _parent=None, _play=None, collections=None):
            self._parent = _parent or StubParent()
            self._play = _play or StubPlay()
            self.args = args
            self.module_defaults = module_defaults
            self.collections = collections

# Generated at 2022-06-13 10:00:13.194411
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = 'host'
    connection = 'connection'
    task_vars = dict()
    inject = dict()
    shared_loader_obj = None
    play_context = None
    loader = None
    tmp_path = 'tmp_path'
    module_executor = 'module_executor'
    async_timeout = 'async_timeout'
    connect_timeout = 'connect_timeout'
    become_method = 'become_method'
    become_user = 'become_user'
    become_exe = 'become_exe'
    become_flags = 'become_flags'
    become_pass = 'become_pass'
    become_info = 'become_info'
    no_log = 'no_log'
    action_plugins = 'action_plugins'

# Generated at 2022-06-13 10:00:23.460505
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {}
    tmp = None
    self_a = ActionModule()
    args = {'parallel': False, 'data': {'ansible_facts': {'network_os': 'nxos'}}, 'disable_run': True}

    # make sure it doesn't fail on a non-conformant module
    args.update(module_name='does_not_exist', wrapped=False, no_log=False)
    result = _ActionModule__execute_module(self_a, tmp, task_vars, args)
    assert result.get('failed') == True
    assert result.get('msg') == 'No module named does_not_exist'

    # make sure it doesn't fail on a conforming module
    args.update(module_name='setup', wrapped=False, no_log=False)
   

# Generated at 2022-06-13 10:00:27.886116
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #for testing purpose, import the class locally
    import sys
    sys.path.append("..")
    from ansible_collections.ansible.general.plugins.actions import setup
    impl = setup.ActionModule('test_data')
    assert(impl != None)

# Generated at 2022-06-13 10:00:36.479141
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actions = {
        'setup': 'ansible.legacy.setup',
        'ping': 'ansible.legacy.ping',
        'facter': 'ansible.legacy.plugins.modules.facter',
        'ohai': 'ansible.legacy.plugins.modules.ohai',
        'uname': 'ansible.legacy.plugins.modules.uname'
    }
    default_action = 'setup'
    cli_args = []
    connection = 'local'
    become_connection = 'local'
    become_method = 'sudo'
    become_user = 'root'
    check = False
    diff = False
    remote_user = 'stack'
    path_exists = True
    task_uuid = '1'
    task_vars = dict()
    templar = None

# Generated at 2022-06-13 10:00:43.091060
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor import module_common
    mdl = module_common.ModuleReplacer()
    mdl.replace = True
    mdl.modify_module()

    assert(ActionModule is not None)
    assert(ActionModule._get_module_args is not None)
    assert(ActionModule._combine_task_result is not None)
    assert(ActionModule.run is not None)

    module_common.revert_module()

# Generated at 2022-06-13 10:00:46.130968
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(loader=dict(), connection=None, templar=None, shared_loader_obj=None)
    assert action_module
    assert action_module._supports_check_mode is True



# Generated at 2022-06-13 10:00:54.576409
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # generate fake values for argument of run
    tmp = 'module'
    task_vars = 'module'

    # initialize class
    setup = ActionModule()
    setup.is_playbook = True
    setup._shared_loader_obj = 'module'
    setup._task = 'module'
    setup._task_vars = 'module'
    setup._tmp_path = 'module'
    setup._connection = 'module'
    setup._play_context = 'module'
    setup._loader = 'module'
    setup._display = 'module'

    # make the call to run
    setup.run(tmp, task_vars)

# Generated at 2022-06-13 10:00:55.615881
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: generate unit test for ActionModule.run
    pass

# Generated at 2022-06-13 10:00:58.134838
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.setup import ActionModule
    ansible_module = ActionModule()
    ansible_module.run()
    return 0

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:01:07.995384
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.setup as setup
    import ansible.playbook.task as task
    import ansible.playbook.play as play
    import ansible.playbook.play_context as play_context
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import AnsibleVars
    from ansible.template import Templar

    setup_obj = setup.ActionModule()
    setup_obj._supports_check_mode = True
    test_dict = dict(
        ansible_connection='network_cli',
        ansible_network_os="test_os",
        ansible_facts=dict(
            another_fact="another_fact_data",
            test_fact="test_fact_data",
        )
    )
    test_vars = Ansible

# Generated at 2022-06-13 10:03:20.303838
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def make_fact_module_result(failed=False, skipped=False, ansible_facts=None, warnings=None, deprecations=None):
        res = {
            'failed': failed,
            'skipped': skipped,
            'warnings': warnings or [],
            'deprecations': deprecations or []
        }
        if ansible_facts:
            res['ansible_facts'] = ansible_facts
        return res

    def make_tmp():
        return {
            'path': '/tmp/test_tmp'
        }

    def make_task_run(task_args, task_vars):
        task_run = {
            'args': task_args,
            'vars': task_vars,
        }
        return task_run

    # Helpers

# Generated at 2022-06-13 10:03:33.313699
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # pylint: disable=protected-access
    _task = object()
    _connection = object()
    _play_context = object()
    _loader = object()
    _templar = object()
    _shared_loader_obj = object()

    action_module = ActionModule(
        _task=_task,
        _connection=_connection,
        _play_context=_play_context,
        _loader=_loader,
        _templar=_templar,
        _shared_loader_obj=_shared_loader_obj)

    assert action_module._task is _task
    assert action_module._connection is _connection
    assert action_module._loader is _loader
    assert action_module._templar is _templar
    assert action_module._shared_loader_obj is _shared_loader

# Generated at 2022-06-13 10:03:40.570373
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test with missing params
    action_mod = ActionModule(task={'name': 'setup'}, connection={'_shell': {'tmpdir': ''}, '_load_name': 'ansible.legacy.setup'}, play_context={'check_mode': True}, loader=None, templar=None, shared_loader_obj=None)
    action_mod._supports_check_mode = True
    action_mod._supports_async = True
    action_mod._task = {'args': {}, '_ansible_parsed': True}
    action_mod._task_vars = {}
    action_mod._task_vars['ansible_facts_parallel'] = None
    action_mod._task.args['parallel'] = None
    assert action_mod.run({}, {}) is not None

   

# Generated at 2022-06-13 10:03:45.885768
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_action_module = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict(),
    )
    assert isinstance(my_action_module, ActionModule)

# Generated at 2022-06-13 10:03:56.112482
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test to assert the class constructor for ActionModule
    """
    # Create a fake task
    task = {
        'action': 'FACT.MODULE',
        'args': {},
        'action_args': {},
        'module_defaults': {},
        'no_log': False,
        'collections': [],
    }

    # Create a fake connection
    fake_loader, connection, tmp, task_vars = {}, {}, {}, {}

    # And a fake display
    fake_display = {
        'v': 3,
    }

    # Create my action module
    my_action = ActionModule(task, connection, tmp, task_vars, fake_display)

    # Assert the constructor
    assert my_action._task == task
    assert my_action._connection == connection
   

# Generated at 2022-06-13 10:04:00.655510
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import add_all_plugin_dirs
    add_all_plugin_dirs()

    def module_func(modpath, module_args, check_mode=False, **kwargs):
        return {
            'ansible_facts': {
                'fact_module': modpath.split('.')[-1],
                'test_arg': module_args['test_arg'],
            }
        }

    # Mock module_loader and module_utils
    from ansible.plugins.loader import module_loader
    from ansible.module_utils import basic

    def import_module(name):
        return basic

    module_loader.add_directory(None, 'library')
    module_loader._module_cache['library.test_setup'] = type('module', (), {'run': module_func})
   

# Generated at 2022-06-13 10:04:02.444934
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor test to see if it's created properly
    am = ActionModule(Task(), Connection('network_cli'))
    assert am != None

    assert am.timeout == 10

# Generated at 2022-06-13 10:04:10.250703
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = {'token': 'wkskkskw',
            'host': '1.2.3.4', 'aliases': [],
            'username': 'kdowkd',
            'path': 'kdokdk', 'network_os': 'junos',
            'become': False, 'no_log': False,
            'validate_certs': True, 'port': 80}

    tmp = None
    task_vars = {'ansible_facts_parallel': 10, 'ansible_network_os': 'ios'}

    act = ActionModule(None, args, tmp, task_vars)
    act.run(tmp, task_vars)

# Generated at 2022-06-13 10:04:19.185093
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # constructor can take in a task and connection
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader

    class PlaybookTask:
        def __init__(self):
            self.action = 'setup'
            self.args = {}
            self.module_defaults = {}
            self.collections = []

    class PlaybookPlay:
        def __init__(self):
            self._action_groups = []

    class Playbook:
        def __init__(self):
            self._play = PlaybookPlay()
            self.vars = {}

    class Host:
        def __init__(self):
            self.name = 'localhost'


# Generated at 2022-06-13 10:04:29.908996
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import DistroInfo
    from ansible.module_utils.facts.system.distribution import LinuxDistribution
    import pkg_resources
    fake_dist = Distribution()
    fake_dist.distro_name = 'fake'
    fake_dist.version_parts = [1, 2, 3]
    fake_dist.major_version = 1
    fake_dist.minor_version = 2
    fake_dist.not_a_number_version = 0
    fake_dist.codename = 'codename'

    # Simulate a case where ansible_facts.distribution exists, but not ansible_distribution_version.
    # This can occur when ansible_facts.distribution is set by a