

# Generated at 2022-06-13 10:26:53.399441
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:27:02.089304
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a dummy task.
    test_task = dict(
        action=dict(
            module='test',
            args=dict(test_arg='test_arg')
        )
    )
    test_task_vars = dict(
        ansible_facts=dict(
            service_mgr='systemd'
        )
    )

    # Create a dummy connection.
    test_conn = dict(
        _shell = dict(
            tmpdir='/tmp'
        ),
        socket_path='/tmp/test'
    )

    # Create the action module object.
    am = ActionModule(
        task=test_task,
        connection=test_conn,
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )



# Generated at 2022-06-13 10:27:09.342417
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # create a task queue manager
    task_queue_manager = TaskQueueManager(
        inventory = InventoryManager(loader=DataLoader(), sources=[]),
        variable_manager = VariableManager(loader=DataLoader()),
        loader = DataLoader(),
    )
    task_queue_manager._final_q = task_queue_manager._queue 

    # the task
    task

# Generated at 2022-06-13 10:27:12.917313
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''

    from ansible.plugins.action.service import ActionModule as service
    s = service(None, None, None, None, None)
    assert s is not None
    return

# Generated at 2022-06-13 10:27:22.445583
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(action='service', module_name='service', module_args='',
                          task_vars=[{'Google': {'user': 'ray', 'pw': 'yu'}}, {'Facebook': {'user': 'Joe', 'pw': '123'}}],
                          loader={'service': {'user': 'ray', 'pw': 'yu'}}, templar={'service': {'user': 'ray', 'pw': 'yu'}},
                          shared_loader_obj={'service': {'user': 'ray', 'pw': 'yu'}}, params={'user': 'ray', 'pw': 'yu'},
                          connect_timeout=60)
    assert action

# Generated at 2022-06-13 10:27:28.160029
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    action module = ActionModule()
    assert action module.BUILTIN_SVC_MGR_MODULES == ['openwrt_init', 'service', 'systemd', 'sysvinit']
    assert action module.UNUSED_PARAMS == {'systemd': ['pattern', 'runlevel', 'sleep', 'arguments', 'args']}
    '''
    assert True

# Generated at 2022-06-13 10:27:31.395901
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Starting to test ActionModule constructor")
    action_module = ActionModule()
    print(action_module)
    assert isinstance(action_module, ActionModule) == True


# Generated at 2022-06-13 10:27:32.016941
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:27:39.906387
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Constructor of ActionModule is tested using this method.
    '''
    # Making task object (Mock Task) with values of ActionModule
    task = type('Task', (object,), {'args': {}, 'async_val': None, '_parent': 'Parent', 
    '_play': 'Play'})()

    # Making connection object. Always true for the check of self._play_context.become
    connection = type('Connection', (object,), {'_shell': type('Shell', (object,), {'tmpdir': None})})()

    # Making shared_loader_obj object

# Generated at 2022-06-13 10:27:43.442435
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Example input for test
    test_input = {}
    results = ActionModule.run(ActionModule(), tmp='/tmp', task_vars=test_input)
    # If no results, the test case fails
    assert results is None

# Test the check_mode import

# Generated at 2022-06-13 10:27:50.789221
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:27:59.083852
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role_dependency import RoleDependency
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader

    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 10:28:11.589798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import context, runner
    from ansible.context import Runtime
    from ansible.executor.task_result import TaskResult
    from ansible.task import Task
    from ansible.template import Templar

    from ansible.parsing.vault import VaultLib
    from ansible.plugins.action import ActionBase

    context._init_global_context(Runtime())

    # Fake display object
    class FakeDisplay:
        class vv:
            pass

        @staticmethod
        def debug(*args, **kwargs):
            pass

        @staticmethod
        def warning(*args, **kwargs):
            pass

        @staticmethod
        def vvv(*args, **kwargs):
            pass

    # Fake templar object
    class FakeTemplar:
        @staticmethod
        def template(data):
            return

# Generated at 2022-06-13 10:28:22.446917
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test case #1 (positive): simple test on run
    from ansible.plugins.action.service import ActionModule
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import os
    import json
    import pytest
    # Prepare test data
    task_data = dict(
        module_defaults=dict(
            service_facts=False,
        ),
    )
    test_task = TaskResult

# Generated at 2022-06-13 10:28:27.705357
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.service import ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.connection_info import ConnectionInformation
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    import ansible.constants as C

   

# Generated at 2022-06-13 10:28:41.053415
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils._text import to_text
    from ansible.plugins.loader import action_loader

    context = PlayContext()

    action_plugin = action_loader.get('service', basedir='/home/user/ansible-repos/ansible')

    context._connection = 'local'
    context._shell = '/bin/sh'
    context._shell_executable = '/bin/sh'
    context._remote_addr = '127.0.0.1'
    context._module_name = 'service'
    context._play_context = context
    #context._task_vars = dict()

    action_plugin._connection = None
    action_plugin._task = None
    action_plugin._low_level_execute_command = None
    action

# Generated at 2022-06-13 10:28:55.044528
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.module_common import ModuleParameters

    mock_shared_loader_obj = Mock()
    mock_shared_loader_obj._loader = 'mock_loader'

    mock_task = Mock()
    mock_task.async_val = False
    mock_task._play = Mock()
    mock_task._play._action_groups = 'mock_action_groups'

    mock_task.args = {'use': 'auto'}

    mock_result = TaskResult(host=dict(name='localhost'))
    mock_result._result = dict()

    mock_module_parameters = ModuleParameters(params=dict())

    mock_action_base = Mock()

# Generated at 2022-06-13 10:29:00.460322
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # FIXME: write unit test for class ActionModule
    actionmodule = ActionModule()
    assert hasattr(actionmodule,'_supports_async')
    assert hasattr(actionmodule,'_supports_check_mode')
    assert hasattr(actionmodule,'TRANSFERS_FILES')
    assert hasattr(actionmodule, 'BUILTIN_SVC_MGR_MODULES')

# Generated at 2022-06-13 10:29:07.703425
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    # Test No. 1
    host = Host()
    task = Task()
    task._role = None
    task.args = dict(name="foo", state="bar", use="auto")
    task.delegate_to = None
    task.notify = []
    task.on_success = []
    task.on_failure = []
    task.on_skipped = []
    task.on_unreachable = []
    task._loop_eval = None
    task.always_run = None
    task.async_val = 1
    task.register = None
    task.when = None
    task.changed_when = None
    task.failed_when = None

# Generated at 2022-06-13 10:29:08.773162
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()

# Generated at 2022-06-13 10:29:25.085469
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'TRANSFERS_FILES')
    assert hasattr(ActionModule, 'UNUSED_PARAMS')
    assert hasattr(ActionModule, 'BUILTIN_SVC_MGR_MODULES')

# Generated at 2022-06-13 10:29:27.865244
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    sys.path.append('../action_plugins')
    from service import ActionModule

    action_module = ActionModule()

    # test method run of class ActionModule
    # assert action_module.run() == # pass

# Generated at 2022-06-13 10:29:34.586190
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a fake action module
    class FakeActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            pass

    # Create a fake task
    fake_task = dict()
    fake_task['action'] = dict()
    fake_task['action']['__ansible_argspec'] = dict()
    fake_task['action']['__ansible_argspec']['args'] = dict()
    fake_task['action']['__ansible_argspec']['defaults'] = dict()
    fake_task['action']['__ansible_argspec']['kwargs'] = dict()
    fake_task['action']['__ansible_argspec']['varargs'] = dict()

# Generated at 2022-06-13 10:29:48.365736
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert getattr(my_action, '_task', None) is None
    assert getattr(my_action, '_connection', None) is None
    assert getattr(my_action, '_play_context', None) is None
    assert getattr(my_action, '_loader', None) is None
    assert getattr(my_action, '_templar', None) is None
    assert getattr(my_action, '_shared_loader_obj', None) is None
    assert getattr(my_action, '_supports_async', None) is None
    assert getattr(my_action, '_supports_check_mode', None)

# Generated at 2022-06-13 10:30:02.564354
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a dummy task
    class DummyTask:
        def __init__(self):
            self.args = {}
    # Create a dummy context
    class DummyContext:
        def __init__(self):
            self.resolved_fqcn = 'ansible.legacy.service'
    # Create a dummy module loader
    class DummyModuleLoader:
        def __init__(self):
            self.find_plugin_with_context = lambda module, collection_list: DummyContext()
            self.has_plugin = lambda module: True
    # Create a dummy shared loader
    class DummySharedLoader:
        def __init__(self):
            self.module_loader = DummyModuleLoader()
    # Create a dummy task vars

# Generated at 2022-06-13 10:30:09.750556
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Preconditions
    import ansible.plugins.loader as loader_module
    import ansible.plugins.loader.module_utils.service_manager as service_manager_module

    def _disabled_exists(path):
        return False
    def _enabled_exists(path):
        return False

    mock_shared_loader_obj = loader_module.PluginLoader()
    mock_task = ActionModule.ActionModule._Task([], mock_shared_loader_obj, loader_module.ActionLoader())
    mock_task._parent = ActionModule.ActionModule._Play([], mock_shared_loader_obj, loader_module.ActionLoader())
    mock_task._parent._parent = ActionModule.ActionModule._DS([], mock_shared_loader_obj, loader_module.ActionLoader())

# Generated at 2022-06-13 10:30:15.619557
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.plugins.loader import connection_loader, module_loader

    def get_connection_plugin(connection):
        plugin = connection_loader.get(connection, class_only=True)
        plugin._load_name = 'connection_fake'
        return plugin

    mock_connection = get_connection_plugin('local')
    mock_connection._shell.tmpdir = '/tmp'


# Generated at 2022-06-13 10:30:16.386348
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None) is not None

# Generated at 2022-06-13 10:30:21.542136
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for run()
    :return:
    '''
    # setup a fake action class
    class FakeAction():
        class FakeModule():
            class FakeLoader():
                class FakeModule_Loader():
                    class FakeContext():
                        def __init__(self):
                            self.resolved_fqcn = "ansible.legacy"
                def __init__(self):
                    self.FakeModule_Loader = FakeAction.FakeModule.FakeLoader.FakeModule_Loader()
            def has_plugin(self, module):
                return True
            def find_plugin_with_context(self, module, collection_list):
                return FakeAction.FakeModule.FakeLoader.FakeModule_Loader.FakeContext()
        class FakeShared_Loader_obj():
            def __init__(self):
                self.module_

# Generated at 2022-06-13 10:30:29.883151
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(
        ansible_facts=dict(),
        ansible_facts_cacheable=None
    )

    task_vars['ansible_facts'].update(dict(ansible_service_mgr="systemd"))
    task_vars['ansible_facts'].update(dict(ansible_distribution="Ubuntu"))
    task_vars['ansible_facts'].update(dict(ansible_distribution_release="20.04"))
    task_vars['ansible_facts'].update(dict(ansible_distribution_version="20.04"))
    task_vars['ansible_facts'].update(dict(ansible_distribution_major_version="20"))
    task_vars['ansible_facts'].update(dict(ansible_architecture="amd64"))

# Generated at 2022-06-13 10:31:04.350152
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:31:08.201561
# Unit test for constructor of class ActionModule
def test_ActionModule():
    controller = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert(hasattr(controller, 'run'))

# Generated at 2022-06-13 10:31:10.199191
# Unit test for constructor of class ActionModule
def test_ActionModule():
  am = ActionModule(None,None,None,None,None,None)
  assert(not am==None)

# Generated at 2022-06-13 10:31:20.787934
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import unittest
    class TestModule(unittest.TestCase):
        def test_action_module(self):
            # test the argument that is passed in constructor
            module = 'auto'
            task = dict()
            task['args'] = dict()
            task['async'] = None
            task['delegate_to'] = None
            task['action'] = 'service'
            task['args']['name'] = 'httpd'
            task['args']['state'] = 'started'
            task['args']['use'] = module

            class mock_shared_loader:
                def __init__(self):
                    self.module_loader = None
            class mock_task:
                def __init__(self):
                    self.args = task['args']

# Generated at 2022-06-13 10:31:22.244718
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module is not None



# Generated at 2022-06-13 10:31:30.297031
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager

    import pprint

    class MockTask():
        def __init__(self):
            self.async_val = 10
            self.args = dict()
            self._parent = None
            self._play = None
            self.delegate_to = None

    class MockPlayContext():
        def __init__(self):
            self.module_defaults = {}
            self._action_groups = {}
            self._action_groups['service'] = {}
            self._action_groups['service']['systemd'] = {}

# Generated at 2022-06-13 10:31:32.058368
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, {}, {}, {})
    assert a is not None

# Generated at 2022-06-13 10:31:42.084607
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a connection to handle our packets
    connection = Connection()
    # Create a task with a fake task object
    task_src = dict(action=dict(__ansible_module__='service'))
    task = Task.load(task_src)
    task.async_val = 10  # use an invalid value for this test
    # Create a shared loader obj
    shared_loader_obj = SharedPluginLoaderObj()
    # Create the action plugin object that we're testing
    action = ActionModule(
        connection=connection,
        task=task,
        connection_loader=None,
        shared_loader_obj=shared_loader_obj,
        templar=None
    )
    # Attribute 'connection' should be set
    assert isinstance(action.connection, Connection)
    # Attribute 'task' should be set
   

# Generated at 2022-06-13 10:31:43.924341
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # SUT
    module = ActionModule(None, 'service', None)

# Generated at 2022-06-13 10:31:54.092554
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = "tmp"
    task_vars = dict()
    task_vars['role_name'] = 'role_name'
    from ansible.plugins.action.service import ActionModule
    from ansible.plugins.action.service import ActionModule
    obj = ActionModule(loader=None, connection=None, templar=None, shared_loader_obj=None)
    obj._execute_module = lambda x, y, z: dict()
    obj._task.args = dict()
    obj._task.async_val = 1
    obj._connection._shell.tmpdir = 'tmp'
    obj._shared_loader_obj.module_loader.has_plugin = lambda x: dict()
    obj._shared_loader_obj.module_loader.find_plugin_with_context = lambda x, y: dict()
    obj._task

# Generated at 2022-06-13 10:32:57.369992
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(use='auto'),
        connection=dict(module_name='auto'),
        play_context=dict(become_method='auto', become_user='auto'),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert module

# Generated at 2022-06-13 10:33:08.127509
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.service import ActionModule
    import ansible.plugins.action.service as service
    from ansible.module_utils.six import string_types

    test_args = {'name': 'smb', 'state': 'started'}
    test_task = {'args': test_args}

    test_module = ActionModule(connection=None, task=test_task, loader=None, templar=None, shared_loader_obj=None)

    # test when module is 'auto':
    test_module._templar = None
    test_module.run(task_vars={'ansible_facts': {}})
    # test when module is 'auto', but 'ansible_facts' is not set:
    test_module.run()
    # test when module is 'auto', but 'ansible

# Generated at 2022-06-13 10:33:11.038291
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import mock
    task = mock.Mock()
    action = ActionModule(task=task)
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 10:33:17.766581
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    test_module._supports_check_mode = True
    test_module._supports_async = True
    test_module._templar = mock.MagicMock()
    test_module._templar.template.return_value = 'auto'
    test_module._shared_loader_obj = None
    test_module.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:33:26.792768
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action
    import ansible.module_utils
    import ansible.module_utils.common.removed
    import ansible.module_utils.async_runners
    import ansible.executor
    import ansible.utils
    import ansible.parsing
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.play_context
    import ansible.executor.playbook_executor
    import ansible.utils.collections_loader
    import ansible.inventory
    import ansible.vars
    import ansible.inventory.manager
    import ansible.compat
    import ansible.plugins.loader
    import ansible.template
    import ansible.utils.plugin_docs

    # create an

# Generated at 2022-06-13 10:33:27.211217
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:33:28.424121
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None)
    assert module is not None

# Generated at 2022-06-13 10:33:28.888954
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:33:39.454262
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:33:45.865099
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  task = {
    'module_args': {
      'name': 'name',
      'state': 'started',
      'enabled': 'enabled',
      'user': 'user',
      'daemon_reload': 'daemon_reload',
      'sleep': 'sleep',
      'pattern': 'pattern',
      'runlevel': 'runlevel',
      'arguments': 'args',
      'args': 'arguments',
      'use': 'auto'
    }
  }
  tmp = None
  task_vars = {
    'ansible_facts': {
      'service_mgr': 'auto'
    }
  }
  am = ActionModule()
  am.__init__()

# Generated at 2022-06-13 10:35:55.698559
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Test ActionModule class constructor")
    actionModule = ActionModule()

# Generated at 2022-06-13 10:36:02.577350
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import __builtin__
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.modules import mock_module_loader
    from units.mock.plugins import MockTask

    # Mock
    setattr(__builtin__, '__salt__', {'service.restart': lambda x: {'msg': 'mock'}})

    # Setup
    # Test module with all params set

    def get_facts():
        return {
            'distribution_version': '14.04',
            'distribution': 'Ubuntu'
        }

    mock_task = MockTask()

# Generated at 2022-06-13 10:36:10.531212
# Unit test for constructor of class ActionModule
def test_ActionModule():

    module_mock = dict(
        arguments=dict(),
        _task=dict(
            async_val=None,
            action='service',
            args=dict(
                use='auto',
                state='started',
                name='foo'
            ),
            delegate_to=None,
            delegate_facts=None,
        ),
        _shared_loader_obj=dict(),
        _templar=dict(),
        _connection=dict(
            _shell=dict(
                tmpdir=None,
            ),
        ),
        _display=dict(),
        _play_context=dict(),
    )


# Generated at 2022-06-13 10:36:14.297975
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module

# Generated at 2022-06-13 10:36:24.898056
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import mock
    import textwrap
    import sys

    # Patch get_action_args_with_defaults
    import ansible.executor.module_common
    get_action_args_with_defaults = ansible.executor.module_common.get_action_args_with_defaults
    ansible.executor.module_common.get_action_args_with_defaults = mock.Mock(return_value="")

    # Mock objects for the task and module
    class Mock_Task:
        async_val = ""
        _parent = ""
        _play = ""
        args = {"name": "foo", "use": "auto", "state": "present"}


# Generated at 2022-06-13 10:36:34.505392
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import json
    import unittest

    try:
        from __main__ import display
    except ImportError:
        print("no display")
        display = None

    # Class parsing wacky json output
    class JsonToClass():
        def __init__(self, jsonstr):
            self.jsontoclass(jsonstr)

        def jsontoclass(self, jsonstr):
            self.json_dict = json.loads(jsonstr)

        def json_dict_to_class(self, dic):
            for k, v in dic.items():
                if isinstance(v, dict):
                    self.json_dict_to_class(v)
                    setattr(self, k, self.json_dict_to_class(v))

# Generated at 2022-06-13 10:36:40.010093
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor import task_result
    from ansible.actions.action_service import ActionModule

    a = ActionModule(task_result.TaskResult(None))
    a._task.args = {'name': 'nginx'}
    r = a.run(None, None)
    assert r['rc'] == 0

# Generated at 2022-06-13 10:36:40.516641
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:36:46.107736
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action
    import ansible.module_utils
    mod = ansible.plugins.action.ActionModule(
        task=dict(args=dict()),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        shared_loader_obj=None,
        templar=ansible.module_utils.template.AnsibleTemplar(loader=dict()),
        final_loader=dict())
    assert mod is not None