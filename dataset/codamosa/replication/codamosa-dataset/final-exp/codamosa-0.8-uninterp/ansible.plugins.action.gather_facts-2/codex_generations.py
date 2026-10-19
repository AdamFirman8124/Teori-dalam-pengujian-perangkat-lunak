

# Generated at 2022-06-13 09:55:36.207154
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import find_plugin_by_name, action_loader
    from ansible.vars.manager import VariableManager

    ActionModuleVar = find_plugin_by_name('setup', action_loader)
    assert isinstance(ActionModuleVar, type)

    fake_loader = object()

    fake_play_context = PlayContext()
    fake_play_context.become = False
    fake_play_context.become_method = None
    fake_play_context.become_user = None
    fake_play_context.connection = 'local'
    fake_play_context.deprec

# Generated at 2022-06-13 09:55:46.302846
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # import pytest
    # pytest.set_trace()
    td = tmpdir()
    ansible_module_paths = td.mkdir('ansible_module_paths')
    fact_module_paths = td.mkdir('fact_module_paths')

    # Mock the constants
    C.DEFAULT_MODULE_PATH = ansible_module_paths
    C.DEFAULT_FACT_CACHE = fact_module_paths

    # Create a temporary file for results
    tmp = td.mkdir('tmp')
    result_file = tmp.join('ansible_facts.result')

    # Create a temporary file for module args
    module_args = tmp.join('ansible_facts.args')

    # Create a temporary file for the call to the ansible.legacy.async_status module


# Generated at 2022-06-13 09:55:54.568441
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.functional import module_args_runner
    fail = False
    module_args = {
        'filter': 'f5_virtual_server',
        'gather_subset': ['all'],
        'gather_timeout': '5',
        'parallel': 'False'
    }
    results = module_args_runner(module_args, module_name='setup', module_klass=ActionModule)
    if results['msg'] == 'The following modules were skipped: ansible.legacy.setup\n':
        pass
    else:
        fail = True
    assert not fail

# Generated at 2022-06-13 09:55:55.180768
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()
    assert mod is not None

# Generated at 2022-06-13 09:56:06.852072
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # fake task
    import json
    import tempfile
    task_data = """{
            "environment": {"ANSIBLE_MODULE_ARGS": {"one": "two"}},
            "vars": {"a": "b", "c": "d"},
            "module_defaults": {
                "ten": "eleven",
                "twelve": "thirteen"
            },
            "no_log": false,
            "args": {
                "seven": "eight",
                "nine": "ten"
            },
            "type": "module"
        }"""

    # Fake runner data
    runner_data = """{
            "changed": false,
            "facts": {
                "ten": "eleven",
                "twelve": "thirteen"
            }
        }"""

    # fake AnsibleModule


# Generated at 2022-06-13 09:56:12.025644
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.setup
    import ansible.plugins.action.network
    import ansible.plugins.modules
    import ansible.plugins.loader

    class TestConnection(object):
        def __init__(self):
            self._load_name = 'network_cli'

    class TestConfig(object):
        def get_config_value(self, value, variables=None):
            data = {'FACTS_MODULES': ['ansible.legacy.setup', 'ansible.legacy.network']}
            return data.get(value)

    class TestModuleLoader(object):
        def find_plugin_with_context(self, value, collection_list=None):
            return TestModulePlugin(value)


# Generated at 2022-06-13 09:56:24.181200
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionmodule = ActionModule(connection=None, task=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    actionmodule._task.args = {'module_defaults': {'gather_subset': '!all'}, 'gather_subset': '!all', 'ansible_facts_parallel': None, 'parallel': 'True'}
    actionmodule._task._parent._play._action_groups = {'all': {'runtime_group': 'all'}}
    actionmodule._task.module_defaults = {'filter': '!all'}
    

# Generated at 2022-06-13 09:56:36.090760
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m_task = MagicMock()
    m_task.args = {}
    m_connection = create_autospec(Connection)
    m_connection._shell = create_autospec(ShellModule)
    m_shared_loader_obj = create_autospec(SharedPluginLoaderObj)
    m_shared_loader_obj.plugin_loader = create_autospec(PluginLoader)
    m_shared_loader_obj.plugin_loader.find_plugin_with_context = MagicMock(side_effect=iter(['TestPlugin', 'TestPlugin2']))
    m_task._parent = MagicMock()
    m_task._parent._play = create_autospec(Play)
    m_task._parent._play._action_groups = {'group1': {'action_name': 'setup'}}
    m_

# Generated at 2022-06-13 09:56:40.269460
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task_queue_manager=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)
    assert(action_module is not None)

# Generated at 2022-06-13 09:56:49.190880
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize task object
    class Task:
        def __init__(self):
            self._parent = None
            self.args = None
            self.module_defaults = None
            self.collections = None
    task_obj = Task()

    # Initialize playbook object
    class Playbook:
        def __init__(self):
            self._action_groups = []
    playbook_obj = Playbook()

    # Initialize connection object
    class Connection:
        def __init__(self):
            self._load_name = None
            self._shell = None
    connection_obj = Connection()

    action_module_obj = ActionModule(task=task_obj, connection=connection_obj, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module_obj

# Generated at 2022-06-13 09:57:04.617965
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    result = action_module.run()
    assert 'ansible_facts' in result
    assert result['ansible_facts']['_ansible_facts_gathered'] == True

# Generated at 2022-06-13 09:57:09.954381
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    mock_task_vars = {
        'ansible_facts': {
            'variable_name': 'variable_value'
        },
        'ansible_network_os': 'network_os_value',
        'ansible_connection': 'connection_value'
    }

    def _load_plugin_name(plugin_name, *args, **kwargs):
        return plugin_name

    def _execute_module(*arg, **kwargs):
        module_args = kwargs['module_args']
        return {
            'ansible_facts': {
                'fact_variable': module_args
            }
        }

    adhoc_args = {
        'module_arg_1': 'module_arg_value_1',
        'module_arg_2': 'module_arg_value_2'
    }



# Generated at 2022-06-13 09:57:10.475455
# Unit test for constructor of class ActionModule
def test_ActionModule():

    module = ActionModule()

    assert module is not None

# Generated at 2022-06-13 09:57:11.200423
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test ActionModule_run")

# Generated at 2022-06-13 09:57:22.432107
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test setup module.
    """


# Generated at 2022-06-13 09:57:33.419062
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import copy
    import sys
    import unittest

    from ansible.module_utils.facts.system.all import All as all_instance
    from ansible.module_utils.facts.network.base import Base as network_base_instance

    from ansible.module_utils._text import to_bytes, to_native

    from ansible.module_utils.facts.system.all import All as all
    from ansible.module_utils.facts.system.base import Base as base
    from ansible.module_utils.facts.system.distribution import Distribution as distribution
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgr as pkg_mgr
    from ansible.module_utils.facts.system.platform import Platform as platform

    from ansible.plugins.action import ActionBase


# Generated at 2022-06-13 09:57:42.732506
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for ActionModule class run method"""

    class ActionModuleTest(ActionModule):
        def get_action_args_with_defaults(fact_module, mod_args, md, tmplr, ag):
            return mod_args

        def get_config(key, variables=None, default=None, interpolate=True):
            if key == 'FACTS_MODULES':
                return ['ansible_local', 'ansible_remote']
            elif key == 'CONNECTION_FACTS_MODULES':
                return {'test_connection': 'ansible.test_local'}

        _shared_loader_obj = type('', (), {})

# Generated at 2022-06-13 09:57:57.262183
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock the config
    C.config = type('MockConfig', (), {
        'get_config_value': lambda self, key, variables=None: ['ansible.legacy.setup'] if key == 'FACTS_MODULES' else {}
    })()

    # some objects to build module with
    class MockActionBase(object):
        def __init__(self):
            self._supports_check_mode = False
            self._display = type('MockDisplay', (), {'vvvv': lambda s, x: None})()
            self._connection = type('MockConnection', (), {'_load_name': '', '_shell': type('MockShell', (), {'tmpdir': 'somedir'})})()

# Generated at 2022-06-13 09:57:59.290551
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, task=None, connection=None, ON_RESULT=None)
    assert bool(action_module)



# Generated at 2022-06-13 09:58:00.219526
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None


# Generated at 2022-06-13 09:58:22.063754
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:58:24.464150
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act_mod = ActionModule(
            task=Task(), connection='local',
            play_context=PlayContext(), loader=None, templar=None,
            shared_loader_obj=None)
    assert act_mod

# Generated at 2022-06-13 09:58:36.589969
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock invoker
    invoker = 'python /usr/bin/ansible-playbook -i inventory /home/user/playbook.yaml'
    # mock unserialized task_vars

# Generated at 2022-06-13 09:58:43.472896
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        connection=None,
        task=None,
        result=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    # check ActionModule creation
    assert action_module is not None



# Generated at 2022-06-13 09:58:45.424387
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None

# Generated at 2022-06-13 09:58:48.775928
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test public, class
    assert hasattr(ActionModule, 'run')
    assert hasattr(ActionModule, '_get_module_args')
    assert hasattr(ActionModule, '_combine_task_result')

# Generated at 2022-06-13 09:58:51.511711
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(connection=None, task=None, final_q=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:58:58.873214
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def _mock_execute_module(module_name, module_args, task_vars, wrap_async):
        return module_name, module_args, task_vars, wrap_async

    def _mock_combine_task_result(result, task_result):
        return result, task_result

    def _mock_remove_tmp_path(tmp):
        return tmp

    def _mock_display_vvvv(msg):
        return msg

    def _mock_set_play_context(var, val):
        return var, val

    def _mock_supports_check_mode(self):
        return True

    def _mock_load_name(self):
        return 'connection_name'


# Generated at 2022-06-13 09:59:07.719417
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.setup as setup
    import ansible.utils.vars as vars

    action = setup.ActionModule(None, None)
    assert isinstance(action, setup.ActionModule)
    assert isinstance(action, ActionBase)

    assert action._supports_check_mode is True

    assert action._shared_loader_obj is None
    assert action._loader is None
    assert action._connection is None
    assert action._play_context is None
    assert action._task_vars is None
    assert action._tmp is None
    assert action._templar is None

    assert action._task is None
    assert action._play is None
    assert action._playbook is None

    assert action._display is None

    tmp = 'tmp'
    task_vars = None

# Generated at 2022-06-13 09:59:08.826050
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None)
    assert type(action) == ActionModule

# Generated at 2022-06-13 10:00:03.396163
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:00:10.654173
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def _loader_run():
        return {}

    def _loader_exists(module):
        return False

    def _loader_get_basedir(module):
        return ''

    def _executor_exists(module):
        return True

    def _executor_get_module_path():
        return ''

    def _executor_get_plugin_type(plugin):
        return 'module'

    def _executor_load_plugin_from_file(module, plugin_type, plugin_name, module_args, prefix='', task_uuid=None):
        module_name = plugin_name
        mock_class = getattr(mock_modules, module_name)
        if not mock_class:
            mock_class = type(module_name, (object,), {})
        mod = mock_class()
       

# Generated at 2022-06-13 10:00:20.843974
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create a mock task object
    task = type('', (), {})()
    task.args = {'parallel': True}
    task.action = 'setup'
    task.action_args = {'module_setup': True}
    task.async_val = 1
    task.default_poll_interval = 15
    task.loop = '{{ test }}'
    task.kv = {'k': 'v'}
    task.module_vars = {'mod': 'var'}
    task.play_vars = {'play': 'var'}
    task.play = {'name': 'test_play'}
    task.role = {'name': 'test_role'}
    task.tags = ['tag1', 'tag2']

# Generated at 2022-06-13 10:00:23.266543
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Init parameters
    tmp = None
    task_vars = None

    # Init object
    action_module = ActionModule(None, None)

    # run()

# Generated at 2022-06-13 10:00:28.152069
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with job_id param
    action_module = ActionModule(job_id=1)
    assert action_module._task.job_id == 1
    assert action_module._supports_async == True
    assert action_module._supports_check_mode == True
    assert action_module.run() != None

# Generated at 2022-06-13 10:00:29.411875
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module is not None

# Generated at 2022-06-13 10:00:37.308241
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class FakeModule():
        def __init__(self, module_loader_obj, psuedo_loader_obj, psuedo_executor_obj):
            self._module_loader = module_loader_obj
            self._shared_loader_obj = psuedo_loader_obj
            self.templar = psuedo_executor_obj
            self.loader = psuedo_loader_obj
            self.connection = psuedo_executor_obj
            self.changes = {}

    class FakeModuleLoader():
        def __init__(self):
            self.module_loader = self

        def find_plugin(self, module_name, mod_type=None, ignore_deprecated=False):
            pass

        def find_plugin_with_context(self, module_name, collection_list=None):
            pass

   

# Generated at 2022-06-13 10:00:38.951276
# Unit test for constructor of class ActionModule
def test_ActionModule():
    t = ActionModule()
    assert t is not None

# Generated at 2022-06-13 10:00:43.596979
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {'ansible_network_os': 'ios'}
    set_module_args({'network_os': 'ios'})
    module = ActionModule(None, task_vars=task_vars)
    result = module.run(tmp=None, task_vars=task_vars)

    assert 'msg' not in result

# Generated at 2022-06-13 10:00:53.446146
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # set up the mock
    module = AnsibleModule(argument_spec=dict())

    # set up the mocks
    _task = MagicMock()
    _connection = MagicMock()
    _task.args = {'_ansible_check_mode': False, '_ansible_selinux_special_fs': ['fuse', 'nfs', 'vboxsf', 'ramfs', '9p'], '_ansible_no_log': False, '_ansible_verbosity': 0, '_ansible_python_interpreter': '/usr/bin/python', '_ansible_version': '2.3.2.0', '_ansible_syslog_facility': 'LOG_USER', '_ansible_verbosity_increased': False}

# Generated at 2022-06-13 10:02:43.625969
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test case of run

    # Creation of mock object
    mock_task_module = MagicMock()
    mock_task_module.args = {'filter': '*', 'gather_subset': 'all'}
    mock_task_module.collections = 'Dummy'
    mock_task_module.module_defaults = 'Dummy'
    mock_task_module.templar = 'Dummy'
    mock_task_module._parent._play._action_groups = ['Dummy']
    mock_action_base = ActionBase()

# Generated at 2022-06-13 10:02:44.557237
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action

# Generated at 2022-06-13 10:02:50.710595
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test run of class ActionModule
    """

    # test call to method _get_module_args of class ActionModule
    def test__get_module_args(fact_module, task_vars):
        args = {
            'gather_subset': ['all', 'min'],
            'gather_timeout': 10,
            'filter': '*eth0*',
            'gather_network_resources': 'all'
        }
        network_resource_fact_modules = C.config._fact_modules.get('network_resources', 'all')
        expected_args = dict(
            gather_subset='min',
            gather_timeout=10,
            filter='*eth0*',
            gather_network_resources=network_resource_fact_modules
        )
        assert expected_args == mod_args

   

# Generated at 2022-06-13 10:02:54.558110
# Unit test for constructor of class ActionModule
def test_ActionModule():

    #testing class construction
    actionModule = ActionModule(None,None)

    assert isinstance(actionModule,ActionModule)


# test _get_module_args()

# Generated at 2022-06-13 10:02:55.078126
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()

# Generated at 2022-06-13 10:03:01.942461
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # dummy run method
    def dummy_run(self, tmp, task_vars):
        return {'changes': {'task_vars': task_vars}}
    ActionModule.run = dummy_run

    # set up modules
    modules = ['module_1', 'module_2']
    C.config.set('FACTS_MODULES', modules)

    # set up task_vars
    task_vars = {'ansible_facts_parallel': True}

    # set up module args
    module_args = {}

    # set up the task
    task = {'args': module_args}

    # init module
    action_module = ActionModule()
    # set up task_executor
    action_module._task = task
    # set up connection

# Generated at 2022-06-13 10:03:16.520779
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule"""

    task_vars = dict()
    task_vars['ansible_facts'] = dict()
    task_vars['ansible_facts']['ansible_all_ipv4_addresses'] = ['192.168.1.1', '172.16.1.1', '10.0.0.1']
    task_vars['ansible_facts']['ansible_architecture'] = 'arm'
    task_vars['ansible_facts']['ansible_bios_date'] = '08/13/2014'
    task_vars['ansible_facts']['ansible_bios_version'] = 'VBOX'
    task_vars['ansible_facts']['ansible_machine'] = 'armv6l'


# Generated at 2022-06-13 10:03:24.482635
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Need to create the fake module
    import collections
    import sys
    import ansible.plugins.action

    ActionModule = ansible.plugins.action.ActionModule

    class my_action(ActionModule):
        def run(self, tmp=None, task_vars=None):
            return super(my_action, self).run(tmp, task_vars)

    # Create the mock runner
    class Runner(object):
        def __init__(self):
            self.stdout = '{"ansible_facts_gathered": true}'
            self.return_value = 123
            self.pid = 123
            self.path = 'path'
            self.args = 'args'
            self.changed = True
            self.failed = False
            self.created = True
            self.skipped = True
            self.invocation

# Generated at 2022-06-13 10:03:34.195226
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # class MockActionBase(object):
    #     pass
    module = ActionModule(task={}, connection='local', templar=None, shared_loader_obj=None)


# import mock
# import pytest
# from ansible.executor.task_result import TaskResult
# from ansible.executor.play_context import PlayContext
# from ansible.utils.vars import combine_vars

# from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import dict_to_set, get_diff
# from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.config import NetworkConfig, dumps
# from ansible_collections.ansible.netcommon.plugins.action.network import ActionModule as network_action_module
# from ansible

# Generated at 2022-06-13 10:03:34.759661
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not ActionModule()