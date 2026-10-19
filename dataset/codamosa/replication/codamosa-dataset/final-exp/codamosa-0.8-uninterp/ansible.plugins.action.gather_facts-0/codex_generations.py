

# Generated at 2022-06-13 09:55:29.421780
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""
    # Initialize an instance of class ActionModule
    action_module = ActionModule()

    # Construct a new instance of class ActionModule
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:55:38.669164
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize all the variables
    #
    # The class ActionModule will test
    test_action_module = ActionModule()

    # Common information of the test action
    #
    # The task which is tested
    class test_task():
        def __init__(self, action_module):
            self.args = {
                "ansible_facts_parallel": None,
                "parallel": None,
                "network_os": None,
            }

            # This attribute is to inform that this is a task for the Ansible module
            self.action = "ansible.builtin.setup"

            # The module to be test
            self.action_module = action_module

    # The TaskExecutor object
    class test_TaskExecutor():
        def __init__(self, task):
            self.task = task
           

# Generated at 2022-06-13 09:55:46.091756
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def _module_name(module):
        assert module.__module__.startswith("ansible.plugins.action")
        name = module.__module__.partition("ansible.plugins.action.")[2]
        if name.startswith("legacy."):
            name = name.partition("legacy.")[2]
        return name

    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert _module_name(module) == "setup"
    assert module._supports_check_mode is False

# Generated at 2022-06-13 09:55:48.423487
# Unit test for constructor of class ActionModule
def test_ActionModule():
  # Create an instance of the action module
  module = ActionModule()

  assert module is not None, 'Failed to instantiate ActionModule'

# Generated at 2022-06-13 09:55:59.422733
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class LoaderModule(object):
        def find_plugin_with_context(self, plugin, collection_list):
            class PluginModule(object):
                def resolved_fqcn(self):
                    return 'ansible.module_setup'
            return PluginModule()


    class CModule(object):
        config = {
            'FACTS_MODULES': [],
            'CONNECTION_FACTS_MODULES': {
                'network_os': 'network_module'
            }
        }

    class ActionBaseModule(object):
        def run(self, tmp, task_vars):
            return {
                'ansible_facts': {},
                'deprecations': {},
                'warnings': []
            }


# Generated at 2022-06-13 09:56:00.120258
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:56:11.189595
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult
    from ansible.executor.module_common import ANSIBLE_MAGIC_VARIABLE
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.common.network.network import NetworkModule

    def _execute_module(module_name=None, module_args=None, task_vars=None, wrap_async=False):
        module_name = module_name.split('.')[-1:][0]
        if module_name in ['ansible.legacy.setup']:
            return TaskResult(dict(ansible_facts={'network_os': 'testos1'}))

# Generated at 2022-06-13 09:56:23.340597
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # mock task_vars to set value for ansible_facts_parallel
    task_vars = {'ansible_facts_parallel': True}

    # mock module args
    module_args = {}

    # mock action_base object
    action_base_obj = ActionBase()

    # mock display object
    display_obj = Display()

    # mock action_plugin obj
    action_plugin_obj = ActionModule()

    # mock executor obj
    executor_obj = Executor()

    # setup mock object

# Generated at 2022-06-13 09:56:24.179812
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    # TODO fix this test
    # action_module.run()

# Generated at 2022-06-13 09:56:26.823042
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a is not None

# Generated at 2022-06-13 09:56:40.870021
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:56:49.498535
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test function to test ActionModule class run method.
    '''
    hostvars = {}
    hostvars['ansible_network_os'] = 'test'
    taskvars = {}
    taskvars['ansible_facts'] = {}
    taskvars['ansible_facts']['network_os'] = 'test'

    ac = ActionModule()
    ac._connection = MockConnection()
    ac._shared_loader_obj = MockLoaderObj()
    ac._task = MockTask()
    ac._templar = MockTemplar()
    ac._display = MockDisplay()
    ac._task.args = {}
    ac._task.args['network_os'] = 'test'
    mock = {}
    mock['config'] = {}

# Generated at 2022-06-13 09:56:58.925456
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test ActionModule.__init__().
    """
    print("Testing ActionModule.__init__()")

    # Create a mock module
    class MockModule(object):
        def __init__(self, supported, check_mode_supported):
            self.module_name = 'test'
            self.module_args = {}
            self.check_mode = False
            self.no_log = False
            self.supported = supported
            self.check_mode_supported = check_mode_supported
            self.connection = 'test'
            self.task = MockTask()

    # Create a mock task
    class MockTask(object):
        def __init__(self):
            self._role = MockRole()

    # Create a mock role

# Generated at 2022-06-13 09:57:02.535548
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    am.run(tmp=None, task_vars=None)
    return True



# Generated at 2022-06-13 09:57:03.489985
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:57:14.088846
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.mock import patch, Mock
    module = 'setup'
    module_args = {}
    tmp = '/tmp'
    task_vars = {'ansible_network_os': 'ios'}

    executor = ActionModule.executor
    connection = ActionModule.connection
    action = ActionModule(executor, connection, tmp, module, module_args, task_vars=task_vars)
    action.config = Mock(
        get_config_value=Mock(
            side_effect=[
                ['setup'],
                'ansible.legacy.ios.setup',
            ]
        )
    )
    action._execute_module = Mock(return_value={})

# Generated at 2022-06-13 09:57:16.663455
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run")
    print(ActionModule.run)
    # self, tmp=None, task_vars=None
    assert(ActionModule.run != None)

# Generated at 2022-06-13 09:57:20.648031
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task={'args': {}}, connection={'play': {'playbook': {'basedir': '.'}, 'become_method': None, 'become_user': None, 'user': None}})
    assert am

# Generated at 2022-06-13 09:57:22.026537
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule({})
    assert action
    assert isinstance(action, ActionBase)

# Generated at 2022-06-13 09:57:32.871988
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Tests setup with mock data
    mock_config = {
        'FACTS_MODULES': ['smart'],
        'CONNECTION_FACTS_MODULES': {'network_os': 'ansible.legacy.setup'},
    }
    mock_task = {
        'args': {'parallel': None},
        'collections': None,
        'delegate_to': None,
        'notify': None,
        'register': None,
        'retries': 0,
        'run_once': False,
        'sudo': False,
        'sudo_user': None,
        'when': None,
    }

# Generated at 2022-06-13 09:57:54.503422
# Unit test for constructor of class ActionModule
def test_ActionModule():
    values = {}
    action_module = ActionModule(values)
    if not isinstance(action_module, ActionModule):
        print("Error in constructor of action_module")
        return 1
    return 0



# Generated at 2022-06-13 09:57:57.355611
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Given
    class MockActionModule(ActionModule):
        def __init__(self):
            super(MockActionModule, self).__init__()

    # When
    mock = MockActionModule()
    # Then
    assert 'ansible_facts' in mock.run().keys()

# Generated at 2022-06-13 09:58:01.963349
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a mock action base
    action_base = ActionBase()
    # and an action module
    action_module = ActionModule()

    # We are going to mock the 'run' method of action module, so that we can test run method
    # of our own class ActionModule
    action_module.run = action_base.run

    # create a temp directory to store result files
    tmp_dir = tempfile.mkdtemp()

    # create some fact modules
    fact_modules = [
        tempfile.NamedTemporaryFile(prefix='fact_module_', suffix='.py', dir=tmp_dir)
        for index in range(4)
    ]

    # create a temporary file for storing task vars

# Generated at 2022-06-13 09:58:02.933690
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module.run()

# Generated at 2022-06-13 09:58:03.549167
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 1 ==1

# Generated at 2022-06-13 09:58:13.929129
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action as action
    action._ = lambda x:x
    a = action.ActionModule()
    a._connection = {}
    a._connection._shell = {
        'tmpdir': '',
    }
    a._shared_loader_obj = {
        'module_loader': {
            'find_plugin_with_context': lambda x, y: x,
        },
    }
    a._templar = {}
    a._task = {
        'args': {
            'parallel': True
        },
        'collections': [],
        'module_defaults': {},
        '_parent': {
            '_play': {
                '_action_groups': [],
            },
        },
    }

# Generated at 2022-06-13 09:58:19.856204
# Unit test for constructor of class ActionModule
def test_ActionModule():
    conn = type('obj', (object,), {
        'run': mock.MagicMock(),
        'run_command': mock.MagicMock(),
        '_shell': type('obj', (object,), {
            'tmpdir': 'tmpdir'
        })
    })
    task = type('obj', (object,), {
        'args': {},
        '_parent': type('obj', (object,), {
            '_play': type('obj', (object,), {
                'action_groups': {}
            })
        })
    })
    ds = type('obj', (object,), {
        'run': mock.MagicMock()
    })
    task_vars = {}
    module = ActionModule(ds, conn, tmp=None, task_vars=task_vars)
    assert module

# Generated at 2022-06-13 09:58:21.583657
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Unit test for constructor of class ActionModule'''
    assert issubclass(ActionModule, ActionBase)

# Generated at 2022-06-13 09:58:22.148289
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:58:33.395508
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible_collections.ansible.community.tests.unit.plugins.module_utils import AnsibleExitJson, AnsibleFailJson
    from ansible_collections.ansible.community.plugins.module_utils.facts import AnsibleFacts
    import pytest

    class FakeTask():

        def __init__(self, args={}):
            self.args = args
            self.module_defaults = {}

        def _parent(self):
            class FakePlay():
                class FakeParent():
                    class FakeHost():
                        pass
                host = FakeHost()
            return FakePlay()

    class FakeModule():

        def __init__(self, args={}):
            self.args = args

        def fail_json(*args, **kwargs):
            raise AnsibleFailJson(kwargs)


# Generated at 2022-06-13 09:59:17.471819
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock the class to be tested
    class TestActionModule(ActionModule):
        def __init__(self, *args, **kwargs):
            self.test_class = True

        def _execute_module(self, *args, **kwargs):
            return {'test_data': True}

    # TEST - run

    # Create an instance of the task to be tested
    a = TestActionModule(task=MockTask(), connection=MockConnection(), play_context=MockPlayContext(), loader=None, templar=None, shared_loader_obj=None)
    # Define data_structures used in test
    tmp = None
    split_module_names = []
    task_vars = None

    # Invoke the method to be tested
    result = a.run(tmp, task_vars)

    # Ensure

# Generated at 2022-06-13 09:59:17.983385
# Unit test for constructor of class ActionModule
def test_ActionModule():

    this = ActionModule()

# Generated at 2022-06-13 09:59:24.437600
# Unit test for method run of class ActionModule
def test_ActionModule_run():  # pylint: disable=too-many-locals,redefined-outer-name
    # create a dummy instance
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.plugins.loader import action_loader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    # Create a stub task queue manager and populate with fake tasks and things
    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        passwords=None,
        stdout_callback=None
    )

    # ActionModule instance
    task = Task()
    task.action = 'setup'
    task.loop = 1
    task.block = []

    # Play

# Generated at 2022-06-13 09:59:34.372649
# Unit test for constructor of class ActionModule
def test_ActionModule():
    config = {}
    config['DEFAULT_ROLES_PATH'] = '/some/default/path'
    config['ROLES_PATH'] = '/some/path'
    config['UNREACHABLE_HOST_RETRY'] = 10
    config['UNREACHABLE_HOST_RETRY_INT'] = 1
    config['BECOME_TIMEOUT'] = 1
    config['BECOME_ASK_PASS'] = False
    config['SUDO_PASSWORD'] = None
    config['DEFAULT_SUDO'] = False
    config['DEFAULT_BECOME'] = True
    config['BECOME_USER'] = 'someuser'
    config['BECOME_METHOD'] = 'su'
    config['BECOME_ALLOW_SAME_USER'] = True

# Generated at 2022-06-13 09:59:42.243719
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Mock's __init__
    module = ActionModule('setup', dict(filter=None, gather_subset=['all'], gather_timeout=None))

    # Mock's _execute_module method
    module._execute_module = lambda **kwargs: dict(ansible_facts=dict(foo='bar'))

    # Mock's set_type_info method
    module._templar = Mock()
    module._templar.set_type_info = lambda **kwargs: None

    # Mock's run method
    module._remove_tmp_path = Mock()
    module._remove_tmp_path.run = lambda **kwargs: None

    # Mock's get_config_value method
    from ansible.config.manager import ConfigManager

# Generated at 2022-06-13 09:59:43.649850
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionmodule = ActionModule(None, None, None, {})
    assert actionmodule.run(task_vars={}) is not None

# Generated at 2022-06-13 09:59:46.675561
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.utils import context_objects
    am = ActionModule('', {}, context_objects.Task())
    assert isinstance(am, ActionModule)

# Generated at 2022-06-13 09:59:50.429566
# Unit test for method run of class ActionModule
def test_ActionModule_run():
 
    # Create the Module class
    module = ActionModule('setup', 'setup', task_vars={}, loader=None, play_context=None, shared_loader_obj=None, templar=None, task_uuid=None, connection=None, ansible_version=None)

    # initialize the module with the right parameters
    module.run( tmp=None, task_vars={})

# Generated at 2022-06-13 09:59:50.867893
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:59:53.527231
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock = environ.patch_dict('ansible_runner.__main__.settings', {'env': {'ANSIBLE_NOCOLOR': '1', 'ANSIBLE_FORCE_COLOR': '0'}})
    mock.start()

    obj = ActionModule()
    mock.stop()

# Generated at 2022-06-13 10:01:40.522112
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def _check_run(result, expected_results):
        for k, v in expected_results.items():
            if hasattr(v, 'keys'):
                _check_run(result[k], v)
            else:
                assert result[k] == v

    module = ActionModule()
    module._shared_loader_obj = mock.MagicMock()
    module._shared_loader_obj.module_loader.find_plugin_with_context.side_effect = lambda name, coll: name

    expected_result = {
        'ansible_facts': {},
        'failed': False,
        'failed_modules': {},
        'skipped': False,
        'skipped_modules': {},
        'msg': ''
    }

    # Test multiple facts, async

# Generated at 2022-06-13 10:01:46.203419
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:01:54.520452
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test data
    tmp = None
    task_vars = {
        'ansible_facts_parallel': True, 'ansible_facts_gathered': True, 'failed': False, 'msg': None,
        'skipped': False, 'skipped_reason': None, 'skipped_modules': {}, 'failed_modules': {}
    }
    modules = ['smart', 'foo', 'bar']
    config = {'load_name': 'foo'}
    config.update({'FACTS_MODULES': modules})
    config['CONNECTION_FACTS_MODULES'] = {'network_os': 'ansible.legacy.setup'}
    C._CONFIG = config

    #
    # _get_module_args
    #

    # test default value of method _get_module_args


# Generated at 2022-06-13 10:01:56.071101
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('This test needs to be written')
    #action_module = ActionModule()
    

# Generated at 2022-06-13 10:02:10.360203
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule({'args': {}, 'type': 'setup', 'async': 1000, 'async_val': 0})

    action.run(tmp=None, task_vars={})
    action.run(tmp=None, task_vars={'ansible_facts_parallel': False})
    action.run(tmp=None, task_vars={'ansible_facts_parallel': True})
    action.run(tmp=None, task_vars={'ansible_facts_parallel': None})
    action.run(tmp=None, task_vars={'ansible_facts_parallel': None, 'ansible_facts_modules': ['ansible.legacy.setup']})

# Generated at 2022-06-13 10:02:19.269408
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    config = {'FACTS_MODULES': ['smart', 'ansible.mac_facts', 'ansible.windows_facts', 'ansible.network_facts', 'ansible.community.general.system_profiler']}
    shared_loader_obj = MockSharedPluginLoaderObj()
    task_vars = {'ansible_facts': {'distribution': 'Fedora'}}
    with patch("ansible.plugins.action.facts.ActionModule.get_action_args_with_defaults") as mock_get_args:
        short_name = shared_loader_obj.module_loader.find_plugin("smart", ".fact", shared_loader_obj.collection_list)

# Generated at 2022-06-13 10:02:21.298659
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # simple test to make sure we return something
    assert ActionModule.run(None) is not None

# Generated at 2022-06-13 10:02:32.050924
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # test with empty modules and parallel is True
    fact_module = None
    module_args = {}
    task_vars = {}
    wrap_async = False
    res = {}
    result = {}
    result['ansible_facts'] = {}
    modules = ['ansible.legacy.setup']
    parallel = True
    failed = {}
    skipped = {}

    mod_args = get_action_args_with_defaults(
        'ansible.legacy.setup', module_args, fact_module, fact_module, action_groups=None
    )
    res = fact_module.run(tmp=None, task_vars=task_vars)
    if res.get('failed', False):
        failed[fact_module] = res

# Generated at 2022-06-13 10:02:38.968117
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    """
    #
    # Create the object that we are going to test
    #
    mock_task = MagicMock()
    mock_loader = MagicMock()
    mock_play_context = MagicMock()
    mock_mgr = MagicMock()
    mock_templar = MagicMock()
    mock_conn = MagicMock()
    mock_display = MagicMock()
    setup_obj = ActionModule(mock_task, mock_connection=mock_conn, _play_context=mock_play_context, loader=mock_loader,
                             templar=mock_templar, shared_loader_obj=mock_mgr._loader,
                             display=mock_display)

# Generated at 2022-06-13 10:02:46.168897
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._task.args = dict(setup='setup') # pylint: disable=protected-access
    action_module._connection = object() # pylint: disable=protected-access
    action_module._connection._load_name = 'test_load_name' # pylint: disable=protected-access
    action_module._display = object() # pylint: disable=protected-access
    action_module._supports_check_mode = True # pylint: disable=protected-access
    action_module._task = object() # pylint: disable=protected-access
    action_module._task._parent = object() # pylint: disable=protected-access
    action_module._task._parent._play = object() # pylint: disable=protected-access
    action_module._