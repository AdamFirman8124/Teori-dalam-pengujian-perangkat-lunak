

# Generated at 2022-06-13 10:27:02.289640
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock, sys, collections
    sys.modules['ansible'] = mock.MagicMock()
    sys.modules['ansible.errors'] = mock.MagicMock()
    sys.modules['ansible.errors.AnsibleAction'] = mock.MagicMock()
    sys.modules['ansible.executor.module_common'] = mock.MagicMock()
    sys.modules['ansible.plugins.action'] = mock.MagicMock()
    from ActionModule import ActionModule
    from ansible.plugins.action import ActionBase
    import collections
    import ansible.executor.module_common

    AnsibleAction = sys.modules['ansible.errors.AnsibleAction']
    get_action_args_with_defaults = sys.modules['ansible.executor.module_common'].get_action_args_with_

# Generated at 2022-06-13 10:27:03.427877
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action is not None
    assert isinstance(action, ActionBase)


# Generated at 2022-06-13 10:27:11.498923
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Playbook
    from io import StringIO
    from collections import namedtuple
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 10:27:22.212353
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:27:24.482251
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(action=dict(), task=dict(), shared_loader_obj=None)
    # test action_type member
    assert action_module._action_name == 'service'

# Generated at 2022-06-13 10:27:32.408805
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible import context
    from ansible.plugins.loader import collection_loader

    # create a test action base
    test_action_base = ActionModule(
        task=dict(action='test_action_base'),
        connection=None,
        play_context=context.CLIARGS._store,
        loader=collection_loader,
        templar=None,
        shared_loader_obj=None)

    # create a test action base
    if test_action_base is not None:
        print("Vali Test Passed: ActionModule Created Sucessfully")

# Generated at 2022-06-13 10:27:33.401510
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, '')
    assert action.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:27:45.869940
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create instance fo class
    obj = ActionModule(
        task=dict(
            async_val=False,
            args=dict(),
            async_jid=None,
            async_seconds=0,
            delegate_to=None,
            delegate_facts=False,
            ignored_fields=[],
            loop=None,
            loop_args=None,
            loop_control=None,
            module_defaults=None,
            name="test module name",
            no_log=False,
            register=None,
            retries=0,
            throttling=0.0,
            until=None,
            when=None
        ),
        connection=None,
        _play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

   

# Generated at 2022-06-13 10:27:49.367725
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None
    )
    assert module.TRANSFERS_FILES is False

# Generated at 2022-06-13 10:27:50.846435
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module._shared_loader_obj != None
    return True


# Generated at 2022-06-13 10:28:10.498558
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule(task=dict(action=dict(module_name='service', module_args=dict(use='auto')), async_val=0, async_jid=None), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    a._shared_loader_obj.module_loader.has_plugin = lambda module: True
    a._shared_loader_obj.module_loader.find_plugin_with_context = lambda module, collection_list: module
    a._templar.template = lambda string, **kwargs: string
    a._display.debug = lambda msg: msg
    a._display.warning = lambda msg: msg
    a._display.vvvv = lambda msg: msg

# Generated at 2022-06-13 10:28:16.402611
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert am.task is not None
    assert am.connection is not None
    assert am.play_context is not None
    assert am.loader is not None
    assert am.templar is not None
    assert am.shared_loader_obj is not None


# Generated at 2022-06-13 10:28:24.912532
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test setup
    task_vars = dict(
        ansible_facts=dict(
            ansible_service_mgr='auto'
        ),
        hostvars=dict(
            host1=dict(
                ansible_facts=dict(
                    service_mgr='auto'
                )
            )
        )
    )

    # Test execution
    am = ActionModule(
        task=dict(
            args=dict(),
            delegate_to='host1'
        ),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert am.run(task_vars=task_vars)['ansible_facts'] == dict(service_mgr='auto')

# Generated at 2022-06-13 10:28:25.933535
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:28:26.771508
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:28:40.618539
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    import sys
    import os

    # Import the class to test
    from ansible.plugins.action.service import ActionModule
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_executor import TaskExecutor
    from ansible.plugins.loader import module_loader
    from ansible.module_utils.module_common import AnsibleModule


    # setup our test objects
    class Task(object):
        def __init__(self):
            self._parent = None    # _parent
            self.args = {}         # args
            self.action = u''      # action
            self.async_val = 500   # async_val


    class TaskExecutor(object):
        def __init__(self):
            self.module_loader = module_loader
            self

# Generated at 2022-06-13 10:28:42.404450
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(1,2,3) is not None

# Generated at 2022-06-13 10:28:45.120827
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module.TRANSFERS_FILES is False

# Generated at 2022-06-13 10:28:54.579514
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""

    mock_task = mock.MagicMock()
    mock_shared_loader_obj = mock.MagicMock()
    mock_connection = mock.MagicMock()
    mock_play_context = mock.MagicMock()
    mock_new_module_args = mock.MagicMock()
    mock_new_module_args['use'].lower.return_value = 'auto'
    mock_task.args = mock_new_module_args
    mock_task.delegate_to = False
    mock_shared_loader_obj.name = 'action'
    mock_shared_loader_obj.module_loader = mock.MagicMock()
    mock_shared_loader_obj.module_loader.has_plugin.return_value = True

# Generated at 2022-06-13 10:28:56.122138
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run(tmp=None,task_vars=None)

# Generated at 2022-06-13 10:29:19.516567
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:29:25.987112
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert 'Transfers files' in action_module.__doc__
    assert action_module.TRANSFERS_FILES == False
    assert action_module.UNUSED_PARAMS == {'systemd': ['pattern', 'runlevel', 'sleep', 'arguments', 'args']}

# Generated at 2022-06-13 10:29:33.205922
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {}
    module_args = {'name': 'test_test', 'state': 'test_test'}
    task = object()

    action_module = ActionModule(task, task_vars, module_args, 'test_test')

    # test for when tmp no longer has any effects
    action_module.run('test_test', task_vars)

    # test for when module_args.get('use', 'auto').lower() returns value other than 'auto'
    module_args = {'name': 'test_test', 'state': 'test_test', 'use': 'test_test'}
    action_module = ActionModule(task, task_vars, module_args, 'test_test')
    action_module.run('test_test', task_vars)
    assert action_module.run

# Generated at 2022-06-13 10:29:45.266497
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:29:50.331167
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with default kwargs
    x = ActionModule(None, {}, None, None)

    assert x._supports_check_mode is True
    assert x._supports_async is True
    assert x.CACHEABLE is False
    assert x.TRANSFERS_FILES is False
    assert x.UNUSED_PARAMS == {'systemd': ['pattern', 'runlevel', 'sleep', 'arguments', 'args'], }

# Generated at 2022-06-13 10:29:55.755764
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.TRANSFERS_FILES == False
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert type(action_module) == ActionModule

# Generated at 2022-06-13 10:29:58.236855
# Unit test for method run of class ActionModule
def test_ActionModule_run():

  from ansible.plugins.action.service import ActionModule

  action = ActionModule()

  assert action.run()

# Generated at 2022-06-13 10:29:59.939188
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'action_plugins.service' == ActionModule.__module__
    assert 'ActionModule' == ActionModule.__name__

# Generated at 2022-06-13 10:30:00.436821
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:30:01.197838
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ac = ActionModule(None, None, None, None)

# Generated at 2022-06-13 10:30:35.004388
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not (ActionModule is None)

# Generated at 2022-06-13 10:30:43.520565
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit test for the constructor of class ActionModule """

    # Test constructor
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Test variables
    assert module.TRANSFERS_FILES == False
    assert module.UNUSED_PARAMS == {
        'systemd': ['pattern', 'runlevel', 'sleep', 'arguments', 'args'],
    }
    assert module.BUILTIN_SVC_MGR_MODULES == set(['openwrt_init', 'service', 'systemd', 'sysvinit'])

    # Test methods
    assert module.run(tmp=None, task_vars=None) == None
    assert module._execute_module() == None
    assert module._remove

# Generated at 2022-06-13 10:30:54.965952
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import pytest

    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../ansible_collections/ansible/community/plugins/modules/")
    from ansible_collections.ansible.community.plugins.modules.service_common import execute_module
    from ansible_collections.ansible.community.plugins.modules.service_common import ActionModule
    from ansible_collections.ansible.community.plugins.modules.service_common import AnsibleActionFail
    from ansible_collections.ansible.community.plugins.modules.service_common import AnsibleAction


# Generated at 2022-06-13 10:31:05.660337
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''test_ActionModule_run'''
    import os
    import module_utils.facts.system
    import collections
    import ansible.utils.plugin_docs
    import ansible.plugins.loader
    import ansible.plugins.action
    import ansible.executor.module_common
    import ansible.template
    import ansible.plugins
    import ansible.executor.task_result
    module_utils.facts.system.LinuxDistribution()
    collections.abc
    ansible.executor.module_common
    ansible.utils.plugin_docs
    ansible.template
    ansible.plugins
    ansible.plugins.loader
    ansible.plugins.action
    ansible.executor.task_result
    os.getcwd()
    nothing = None

# Generated at 2022-06-13 10:31:11.917343
# Unit test for constructor of class ActionModule
def test_ActionModule():

    mock_action_base = ActionBase(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    a = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(a, ActionBase)


test_ActionModule()

# Generated at 2022-06-13 10:31:16.889856
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m_ActionBase = ActionBase()
    o_ActionModule = ActionModule(m_ActionBase._task, m_ActionBase._connection, m_ActionBase._play_context, m_ActionBase._loader, m_ActionBase._templar, m_ActionBase._shared_loader_obj)
    assert o_ActionModule.run() == None

# Generated at 2022-06-13 10:31:26.265741
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.normal import ActionModule
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.process.worker import WorkerProcess
    import ansible.constants as C
    import sys
    import json
    import os

    vault_ids = {}

    class MockVaultSecret:
        def __init__(self):
            self.vault_id = None

    class MockTask:
        def __init__(self):
            self.args = {}
            self.async_val = 0
            self.delegate_to = None
            self.action = 'auto'
            self.module_defaults = None
            self.collections

# Generated at 2022-06-13 10:31:26.716450
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:31:37.391429
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:31:45.667309
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Crear objeto FakeLoader, objeto de la clase ModuleLoader
    module_loader = FakeModuleLoader()

    # Crear objeto FakeTask, objeto de la clase Task
    task = FakeTask()

    # Crear objeto FakeTemplar, objeto de la clase Task
    templar = FakeTemplar()

    # Crear objeto FakeTaskExecutor, objeto de la clase TaskExecutor
    task_executor = FakeTaskExecutor()

    # Crear objeto FakeDisplay, objeto de la clase Display
    display = FakeDisplay()

    # Crear objeto FakeCommand, objeto de la clase Command
    command = FakeCommand()

    # Crear objeto FakeShell, objeto de la clase Shell
    shell = FakeShell(command)

    # Crear objeto FakeConnection, obj

# Generated at 2022-06-13 10:32:44.980401
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module.TRANSFERS_FILES == False
    assert module._supports_check_mode == True
    assert module._supports_async == True



# Generated at 2022-06-13 10:33:00.249996
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    import ansible
    import ansible.plugins
    import ansible.plugins.action
    #from ansible.executor.module_common import get_action_args_with_defaults
    #from ansible.plugins.action import ActionBase

    # We need to create object of class ActionModule to be able to test its method.
    # However, the constructor of class ActionModule requires the first argument to be a task object
    # that itself requires the arguments: delegate_to and delegate_facts.
    # Hence we create object of class Task and create a task object.

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.callback import CallbackBase

# Generated at 2022-06-13 10:33:01.318291
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'action plugin' in dir(ActionModule)

# Generated at 2022-06-13 10:33:10.642197
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import context
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    import ansible.constants as C

    context.CLIARGS = {}

    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 10:33:20.290024
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible import context
    import ansible.constants as C
    import pytest

    data_loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=data_loader, sources='localhost,')

    variable_manager.set_inventory(inventory)

    # Will need this context to access action base class
    context._init_global_context(variables=variable_manager)
    context.CLIARGS = {'module_path': C.DEFAULT_MODULE_PATH}

    t = Task()
    t.__class__ = 'service'
    t.action

# Generated at 2022-06-13 10:33:28.663418
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Note that the following test code does not use AnsibleActionFail. The assertion is used as an exception raising, which
    # is not considered as a fail. This test code is a dummy code for syntax check and coverage.

    # Dummy class of os.path
    class DummyPath:
        def __init__(self):
            pass

    # Dummy class of os
    class DummyOS:
        def __init__(self):
            pass

        path = DummyPath()

    # Dummy class of os.path.exists
    class DummyPathExists:
        def __init__(self, path):
            pass

    # Dummy class of os.mkdir
    class DummyMkdir:
        def __init__(self, path):
            pass

    # Dummy class of os.chmod

# Generated at 2022-06-13 10:33:39.248576
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.executor.task_result import TaskResult
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

    import json
    import unittest

    class ActionModuleUnitTest(unittest.TestCase):
        def setUp(self):
            import tempfile
            self.tmpdir = tempfile.mkdtemp()
            ServiceMgrFactCollector.module_name = 'ansible.module_utils.facts.system.service_mgr'

# Generated at 2022-06-13 10:33:53.328791
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class MockActionModule(ActionModule):
        def __init__(self, ansible_runner):
            self._task = ansible_runner.task
            self._display = ansible_runner.shared_loader.display
            self._connection = ansible_runner.connection
            self._shared_loader_obj = ansible_runner.shared_loader
            self._templar = ansible_runner.shared_loader.templar
            self._task_vars = ansible_runner.task_vars

        def _execute_module(self, module_name, module_args, task_vars, wrap_async=None):
            self._display.vv(u"EXECUTING...")
            self._display.display(u"MODULE_NAME", module_name)

# Generated at 2022-06-13 10:33:54.921065
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 10:33:59.302204
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(actionModule, ActionModule)

# Generated at 2022-06-13 10:36:12.030711
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = []
    tmp = None

    am = ActionModule()

    # test1: Unknown module
    am._task.args = {'use': 'nosuchmodule'}
    result = am.run(tmp, task_vars)
    assert result == {'failed': True, 'msg': 'Could not detect which service manager to use. Try gathering facts or setting the "use" option.'}

    # test2: Unknown module with fallback to ansible.legacy.service
    am._task.args = {'use': ''}
    result = am.run(tmp, task_vars)
    assert result == {'failed': True, 'msg': 'Could not detect which service manager to use. Try gathering facts or setting the "use" option.'}

    # test3: module = systemd, no use, gather_subset = '

# Generated at 2022-06-13 10:36:21.897198
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict())

    assert actionModule.TRANSFERS_FILES == False
    assert actionModule.UNUSED_PARAMS == {'systemd': ['pattern', 'runlevel', 'sleep', 'arguments', 'args']}
    assert actionModule.BUILTIN_SVC_MGR_MODULES == set(['openwrt_init', 'service', 'systemd', 'sysvinit'])

# Generated at 2022-06-13 10:36:24.062621
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(connection='connection',action='action',task=dict(name='name'),loader='loader',templar='templar',shared_loader_obj='shared_loader_obj') is not None



# Generated at 2022-06-13 10:36:34.343862
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # supply the test with a mocked ActionBase object and a mocked task object
    # ActionBase object has a _execute_module method
    # _execute_module is a mock for the actual method which we need to call
    # but don't want to actually call to avoid side-effects
    am_mock = ActionModule()
    am_mock._templar = MagicMock()
    am_mock._templar.template.side_effect = [ 'auto', 'auto' ]
    am_mock._shared_loader_obj = MagicMock()
    am_mock._shared_loader_obj.module_loader.has_plugin.return_value = True

    # test case 1: check if the run method detects a service manager
    # as it should in case the service manager is auto-detected

# Generated at 2022-06-13 10:36:39.877024
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ test __init__ of ActionModule """

    # build module
    module = ActionModule(load_privs=True, become_method=None, become_user=None)

    assert module._supports_check_mode is True
    assert module._supports_async is True

    # return an instance of our class
    return module

# Generated at 2022-06-13 10:36:45.868846
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import load_options_vars
    from ansible.plugins.callback import CallbackBase
    from ansible import context
    import pytest
    import os

    context.CL