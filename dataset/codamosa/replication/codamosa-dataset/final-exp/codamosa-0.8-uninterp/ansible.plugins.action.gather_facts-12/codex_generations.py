

# Generated at 2022-06-13 09:55:27.678953
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule('test', 'Setup', True, [1, 2, 3], {})
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:55:29.692923
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert isinstance(a, ActionBase)

# Generated at 2022-06-13 09:55:38.833791
# Unit test for constructor of class ActionModule
def test_ActionModule():
  am = ActionModule()
  assert am.name == "setup"
  assert am.max_retries == 0
  assert hasattr(am, 'id')
  assert hasattr(am, 'cacheable')
  assert hasattr(am, 'shared_loader_obj')
  assert hasattr(am, 'module_loader')
  assert hasattr(am, '_supports_async')
  assert hasattr(am, '_connection')
  assert hasattr(am, '_task')
  assert hasattr(am, '_loader')
  assert hasattr(am, '_templar')
  assert hasattr(am, '_shared_loader_obj')
  assert hasattr(am, '_display')
  assert hasattr(am, '_options')

# Generated at 2022-06-13 09:55:46.740943
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_context import PlayContext
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import merge_hash
    import ansible.plugins.loader as plugin_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.compat import mock
    import copy
    import json
    import os
    import pytest
    from io import StringIO


# Generated at 2022-06-13 09:55:57.628223
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import shutil
    from ansible import context
    from ansible.cli.adhoc import AdHocCLI
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.vars.manager import VariableManager

    # Create temp dir
    tempdir = tempfile.mkdtemp()

    # Create paths to test files
    playbook_path = os.path.join(tempdir, 'playbook.yml')

# Generated at 2022-06-13 09:55:59.130040
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    myaction = ActionModule({}, {})
    assert myaction.run()

# Generated at 2022-06-13 09:56:03.016206
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize the class object with required values
    action_plugin = get_action_plugin('setup')
    action_plugin.parse_cli()

    # call run() method and set the result
    result = action_plugin.run()

# Generated at 2022-06-13 09:56:13.303826
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest

    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    from ansible.playbook.block import Block

    from ansible.plugins.callback import CallbackBase

    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader

    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath

# Generated at 2022-06-13 09:56:25.189949
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_args = dict()

    # create a generic task
    task = dict()
    task['action'] = 'setup'
    task['args'] = module_args

    # create a generic task which not the most basic action module
    task_not_basic = dict()
    task_not_basic['action'] = 'command'
    task_not_basic['args'] = dict()
    task_not_basic['args']['_raw_params'] = 'ls -la'

    # create dummy display
    display = dict()

    # create dummy connection
    connection = dict()
    connection['_shell'] = dict()
    connection['_shell']['tmpdir'] = 'tmpdir'
    connection['_load_name'] = 'network_cli'

    # create dummy templar
    templar = dict()

    #

# Generated at 2022-06-13 09:56:28.797201
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # We don't really need to be testing _get_module_args since it's
    # unmodified from the prior action module
    # Enabling this test will cause it to fail though due to the different
    # execution path

    assert 1 == 2

# Generated at 2022-06-13 09:56:48.735298
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    import os
    import shutil
    import tempfile
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    from ansible.plugins.action import ActionBase
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import merge_hash


# Generated at 2022-06-13 09:56:49.916527
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)
    assert action_module

# Generated at 2022-06-13 09:56:50.725414
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 09:56:52.677716
# Unit test for constructor of class ActionModule
def test_ActionModule():

    module = ActionModule({}, {})

    assert module.run()['failed'] == True

# Generated at 2022-06-13 09:56:54.547529
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a_m = ActionModule()
    assert a_m is not None

# Generated at 2022-06-13 09:57:09.872707
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # arguments for ActionModule constructor
    action_base = ActionBase(task=None, connection=None, templar=None, loader=None, shared_loader_obj=None,
                             config=None)
    action_module = ActionModule(action_base)
    assert action_module._connection is None
    assert action_module._loader is None
    assert action_module._templar is None
    assert action_module._task is None
    assert action_module._config is None
    assert action_module._has_pipelining is None
    assert action_module._has_module_tools is None
    assert action_module._shell.current_lang == 'default'
    assert action_module._shell.current_shell is None
    assert action_module._supports_async is False
    assert action_module._supports_check_mode

# Generated at 2022-06-13 09:57:16.390307
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    import sys
    import os
    from ansible.plugins.action.setup import ActionModule
    from ansible.utils.vars import merge_hash
    from ansible.module_utils.parsing.convert_bool import boolean

    runner = ActionModule()

    _tmp = '''name: test_setup_module
connection: local
hosts: localhost
tasks:
- name: test without option
  setup:
    gather_subset:
    - network_resources
    gather_timeout: 10

- name: test without option
  setup:

- name: test without option
  setup:
    gather_subset:
    - smart'''


# Generated at 2022-06-13 09:57:26.221500
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    temp = False

    class FakeActionModule:
        def __init__(self, temp):
            self.tmp = temp
            self.path = os.path.dirname(temp)
            self.args = []
            self.action = 'facts'
            self.task_vars = {'ansible_facts_parallel': None,
                              'ansible_facts': {'network_os': 'IOS-XR'},
                              'ansible_network_os': 'IOS-XR'}

    class FakeObject:
        def __repr__(self):
            return '<FakeObject>'

    class FakeExecutor:
        def __init__(self, connection, task, shell):
            self.connection = connection
            self.task = task
            self.shell = shell

# Generated at 2022-06-13 09:57:36.095712
# Unit test for constructor of class ActionModule
def test_ActionModule():

    try:
        from ansible.plugins.loader import find_action_plugin, get_all_plugin_loaders
    except ImportError:
        from ansible.utils.plugins import find_action_plugin, get_all_plugin_loaders

    # get the action plugin loader
    action_loader = find_action_plugin('action')

    # get the connection plugin loader
    connection_loader = get_all_plugin_loaders()['connection']

    # get the shell connection
    shell_obj = connection_loader.get('shell')

    # Build up a task_vars dict

# Generated at 2022-06-13 09:57:40.636433
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionBase = ActionBase()
    actionBase._task = _Task()
    actionBase.connection = _Connection()
    actionBase._connection = actionBase.connection
    actionBase.display = _Display()
    actionBase._display = actionBase.display
    actionBase._shared_loader_obj = _Shared_loader_obj()
    actionBase._templar = _Templar()
    actionBase._task.module_defaults = {'module_defaults': _Module_defaults()}


# Generated at 2022-06-13 09:58:00.687801
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 09:58:07.572923
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create class obj
    obj = ActionModule()

    # create test vars
    tmp = '/tmp/ansible-tmp-1372526223.8-282673901036431/'
    task_vars = dict()
    task_vars['ansible_facts'] = dict()
    task_vars['ansible_facts']['_ansible_facts_gathered'] = True

    # run method
    result = obj.run(tmp, task_vars)

    # assert result is correct
    assert result['ansible_facts'] == dict({
        '_ansible_facts_gathered': True,
    })
    assert result['failed'] == False
    assert result['_ansible_verbose_override'] == True

# Generated at 2022-06-13 09:58:11.138267
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(
        task = dict(),
        connection = dict(),
        play_context = dict(),
        loader = dict(),
        templar = dict(),
        shared_loader_obj = dict()
    )
    assert mod._supports_check_mode == True

# Generated at 2022-06-13 09:58:14.785942
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # check results for default value
    a = ActionModule()

    # test parallelize to be true
    a.run(parallel=True)

    # test parallelize to be false
    a.run(parallel=False)

# Generated at 2022-06-13 09:58:18.922789
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert type(module._task) is dict, "Module should contain a dict for task"
    assert type(module._shared_loader_obj) is dict, "Module should contain a dict for loader"
    assert module._templar is None, "Module should be empty for templar"

# Generated at 2022-06-13 09:58:23.721893
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Unit test for method run of class ActionModule
    #
    # This is a very basic test just to cover basic execution (and later
    # exploration of the results). The test passes if no exception is
    # thrown and it's not marked as failed.

    # Create a mock templar that returns the vebatim input unchanged
    from ansible.template import Templar
    templar = Templar(loader=None, variables={}, shared_loader_obj=None)

    # Create a mock task with a module name
    class MockTaskBase(object):
        def __init__(self, module_name, module_args, col_list=[]):
            self.action = module_name
            self.args = module_args
            self.collections = col_list
            self.module_defaults = {}

    # A minimal module object to be used as

# Generated at 2022-06-13 09:58:24.659011
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 09:58:31.170048
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    This is the unit test for constructor of class ActionModule
    """
    action_module = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:58:40.140105
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins#, ansible.plugins.action#, ansible.plugins.action.setup#, ansible.plugins.connection#
    #import ansible.executor#, ansible.executor.module_common#, ansible.module_utils#, ansible.module_utils.parsing#
    #import ansible.utils#, ansible.utils.vars#
    #import ansible.utils.unsafe_proxy#, ansible.utils.unsafe_proxy.AnsibleUnsafeText#
    #ansible.plugins.action.setup.SETUP_CACHE = None
    #action = ansible.plugins.action.setup.ActionModule('localhost', ansible.plugins.connection.Connection('.', '.'), 'test', 'test', 'test', 'test', 'test', 'test')

# Generated at 2022-06-13 09:58:41.322138
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    run = ActionModule.run
    assert run == run

# Generated at 2022-06-13 09:59:32.553628
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a connection for the module to use
    from ansible.plugins.connection.network_cli import Connection as NetworkCliConnection
    from ansible.plugins.connection.network_cli import Connection
    connection = Connection(play_context=None, new_stdin=None)
    connection_info = dict(
        network_os='cisco',
        ansible_network_os='cisco'
    )
    network_cli_connection = NetworkCliConnection(play_context=None, new_stdin=None, connection_info=connection_info)


# Generated at 2022-06-13 09:59:33.034541
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:59:37.332677
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_result import TaskResult

    features = C.config.get_config_value('DEFAULT_MODULE_UTILS', variables={})
    action_plugin = ActionModule(TaskResult(dict(action='setup', task_args={'foo': 'bar'})), features=features)

    assert action_plugin._supports_check_mode is True

# Generated at 2022-06-13 09:59:52.396374
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create mock
    mock_get_tmp_path = MagicMock()
    mock_get_tmp_path.return_value = '/path/to/tmp'
    mock_load_name = MagicMock()
    mock_load_name.return_value = 'mock_loader'
    mock_job_id = MagicMock()
    mock_job_id.return_value = 'mock_job_id'
    mock_job_id.__str__.return_value = 'mock_job_id'
    mock_resolved_fqcn = MagicMock()
    mock_resolved_fqcn.return_value = 'mock_resolved_fqcn'
    mock_check_mode = MagicMock()
    mock_check_mode.return_value = True

# Generated at 2022-06-13 09:59:55.742048
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an object of class ActionModule with required arguments
    action_module_obj = ActionModule(
        task=dict(action=dict()),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )

    assert action_module_obj._supports_check_mode is True

# Generated at 2022-06-13 10:00:02.195853
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock = {
        "verbosity": 5,
        "version_added": "2.2",
        "module_options": {},
        "module_defaults": {},
        "lib_version": "2.2.0.0",
        "action": "setup",
        "changed": False,
        "invocation": {
            "module_name": "setup",
            "module_args": {
                "filter": "ansible_distribution"
            }
        },
        "no_log": False,
        "ansible_loop_var": "item"
    }

    t = ActionModule(mock, 'local')

# Generated at 2022-06-13 10:00:03.014879
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 10:00:03.916495
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 10:00:05.635665
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Just instantiate and call it once to ensure there are no errors
    am = ActionModule()
    am.run()


# Generated at 2022-06-13 10:00:06.191898
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:01:54.032896
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars

    am = ActionModule({})
    am.task = {'args': {}}
    am.connection = {'_load_name':'network_cli'}
    am._shared_loader_obj = {'module_loader': {'find_plugin_with_context': lambda x, y: 'ansible.legacy.setup'}}
    am._task = {'_parent': {'_play': {'_action_groups': [{}]}}}
    am._play_context = {'become': False}

# Generated at 2022-06-13 10:01:54.640437
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 10:02:04.451709
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.plays.play import Play
    from ansible.executor.play_iterator import PlayIterator
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager

    loader = None
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 10:02:16.798079
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup
    fake_task = dict(
        args = dict(),
        module_defaults=dict(),
        module_vars=dict(),
        _action_groups=dict(),
        _play_context=dict(),
        _play=dict(
            _action_groups=dict(),
        )
    )
    fake_self = dict(
        _task = fake_task,
        _supports_check_mode = True
    )

# Generated at 2022-06-13 10:02:17.423459
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run()

# Generated at 2022-06-13 10:02:29.920516
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test of action module run
    """
    action = ActionModule('test_action', {'test_key': 'test_value'}, {'test_fact': 'test_fact_value'})

# Generated at 2022-06-13 10:02:36.677965
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test load
    fact_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # mock constants
    config = dict()
    config['CONNECTION_FACTS_MODULES'] = dict()
    config['CONNECTION_FACTS_MODULES']['aos'] = 'ansible_aos_facts'
    config['CONNECTION_FACTS_MODULES']['eos'] = 'ansible_eos_facts'
    config['CONNECTION_FACTS_MODULES']['nxos'] = 'ansible_nxos_facts'

# Generated at 2022-06-13 10:02:38.011824
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert isinstance(am, ActionBase)



# Generated at 2022-06-13 10:02:39.153798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run is yet to be implemented")
    assert False

# Generated at 2022-06-13 10:02:40.864777
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_args = {}
    set_module_args(module_args)
    action_module = ActionModule()
    action_module.run()