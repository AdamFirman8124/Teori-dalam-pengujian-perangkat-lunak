

# Generated at 2022-06-13 10:16:16.026680
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("\nTest constructor of class ActionModule")
    task = dict(action="test", async_val=50)
    task_vars = dict(task=task)

    # Constructor of class ActionBase(self, task, connection, play_context, loader, templar, shared_loader_obj)
    actionbase = ActionBase(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # Constructor of class ActionModule(self, task, connection, play_context, loader, templar, shared_loader_obj)
    actionmodule = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # test constructor of class ActionModule()

# Generated at 2022-06-13 10:16:16.674918
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:16:19.025748
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # use a mock to get the class to initialize
    # assert variables are returned as expected
    # assert exception thrown if expected
    return True


# Generated at 2022-06-13 10:16:29.072799
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import sys
    import os
    import configparser
    import tempfile
    import shutil
    import json
    import itertools

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create mock_tqm class
    class mock_tqm:
        def __init__(self):
            pass

    # Create mock_task class
    class mock_task:
        def __init__(self):
            self.args = dict()
            self.action = 'setup'
            self.async_val = 0

    # Create mock_play_context class
    class mock_play_context:
        def __init__(self):
            self.check_mode = False

    # Create mock_connection class
    class mock_connection:
        def __init__(self):
            self._shell

# Generated at 2022-06-13 10:16:31.710038
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:16:33.946226
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule,object)

# Generated at 2022-06-13 10:16:47.574547
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a fake connection plugin
    class ConnectionPlugin(object):
        def __init__(self):
            self.has_native_async = False

    # create a fake task
    class Task(object):
        def __init__(self):
            self.async_val = False
            self.action = "setup"

    # create a fake result object
    class Result(object):
        def __init__(self):
            self.get = {
                'invocation': {
                    'module_args': True
                }
            }

    # create a fake actionbase
    class ActionBase(object):
        def __init__(self):
            self._task = Task()
            self._connection = ConnectionPlugin()

        def run(self, tmp=None, task_vars=None):
            return Result()


# Generated at 2022-06-13 10:16:55.179329
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(
        ansible_facts=dict(
            os_facts=dict(
                distro='redhat',
                lsb='certainly',
            ),
            ansible_lsb='certainly',
        )
    )

    from ansible.plugins.action.normal import ActionModule as OrigActionModule
    action_mod = OrigActionModule(dict(), dict(), dict())
    action_mod._task = dict()
    action_mod._task_vars = task_vars
    action_mod._shared_loader_obj = dict()
    action_mod._templar = dict()
    action_mod._connection = dict()

    try:
        action_mod.run()
    except NotImplementedError:
        pass

# Generated at 2022-06-13 10:16:55.918943
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:17:00.194478
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test constructor of class ActionModule"""

    # If you want to assert that actions or plugins are loaded, you can simply:
    assert ActionModule

    # Constructor of class ActionModule can be called without arguments.
    ActionModule()

# Generated at 2022-06-13 10:17:05.505701
# Unit test for constructor of class ActionModule
def test_ActionModule():
    success = False
    try:
        action_module = ActionModule()
        success = True
    except Exception as e:
        print(e)
    assert success

# Generated at 2022-06-13 10:17:10.031251
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible
    task_vars = dict()
    tmp = None
    mock_action = ansible.plugins.action.ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
    mock_action.run(tmp=tmp, task_vars=task_vars)

# Generated at 2022-06-13 10:17:12.152605
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    task_vars = {}
    tmp = "/var/tmp"
    action_module.run(tmp, task_vars)


# Generated at 2022-06-13 10:17:13.721341
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global c
    c = ActionModule(None, None, None)

# Generated at 2022-06-13 10:17:16.758312
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test load module
    module = ActionModule(load_module_imp=lambda *args, **kwargs: None)
    assert module is not None

if __name__ == '__main__':
    testActionModule()

# Generated at 2022-06-13 10:17:17.332744
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:17:21.136080
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  print(ActionModule.run.__doc__)
  m = ActionModule()
  task_vars = {"a":1}
  m.run(task_vars=task_vars)

if __name__ == '__main__':
  test_ActionModule_run()

# Generated at 2022-06-13 10:17:21.736785
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:17:30.710322
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m=ActionModule()
    m.set_task_and_connection(task_vars=dict(), connection="test")
    m.task_vars = dict()
    m.connection = "test"
    r = m.run(task_vars=dict())
    assert r.get('invocation', {}).get('module_args') == None
    assert r.get('stdout') == ""
    assert r.get('stdout_lines') == []
    assert r.get('failed') == False
    assert r.get('changed') == False
    assert r.get('_ansible_verbose_override') == False
    assert r.get('module_stderr') == ""
    assert r.get('module_stdout') == ""

# Generated at 2022-06-13 10:17:31.472901
# Unit test for constructor of class ActionModule
def test_ActionModule():
    asserEqual(ActionModule())

# Generated at 2022-06-13 10:17:46.077481
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import copy
    if sys.version_info.major == 3:
        from unittest import mock as mock
    else:
        import mock

    m_task_vars = {'foo': 'bar'}
    m_tmp = '/some/tmp/path'
    m_tmpdir = '/tmpdir'

    m_action_base = mock.MagicMock()
    m_action_base._supports_check_mode = True
    m_action_base._supports_async = True
    m_action_base.task_vars = m_task_vars
    m_action_base._task = mock.MagicMock()
    m_action_base._task.action = 'setup'
    m_action_base._task.async_val = None
    m_action_base._connection

# Generated at 2022-06-13 10:17:47.145881
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test variable access
    assert True

# Generated at 2022-06-13 10:17:55.197519
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {"some_var": "bar"}
    mock_task = {
        "args": {
            "foo": "{{some_var}}",
            "_raw_params": "task data",
            "_uses_shell": False,
            "_binary_arguments": None
        },
        "action": "ping",
        "async": 42,
        "async_val": True,
        "delegate_to": None
    }
    mock_connection = {
        "_shell": {
            "tmpdir": "/tmp/"
        },
        "has_native_async": False
    }

    # Test our run() method's happy path
    mock_module = ActionModule(mock_connection, mock_task, '/path/to/ansible/lib/ansible/modules/ping.py')
    result

# Generated at 2022-06-13 10:17:57.442239
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(['test'], {'hello': 'world'}, {})
    assert module._connection.connection.connection == 'local'

# Generated at 2022-06-13 10:18:11.928549
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    from ansible.errors import AnsibleFilterError
    from ansible.executor.task_result import TaskResult
    from ansible.parsing.vault import VaultLib
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.loader import get_all_plugin_loaders

    module_loader = get_all_plugin_loaders()[0]


# Generated at 2022-06-13 10:18:14.172951
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(self, connection, play_context, loader, templar, shared_loader_obj)
    assert_equals(action_module, id)

# Generated at 2022-06-13 10:18:20.736093
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module = ActionModule()

    # Testing with no parameters - exception expected
    params = []
    res_args = (params, )
    module.run.when.called_with(*res_args).should.throw(Exception)

    # Testing with parameters
    params = ['value1', 'value2']
    res_args = (params,)
    result = module.run.when.called_with(*res_args).should.return_value()
    result.should.be.dictionary().having.key('invocation').being.dictionary().having.key('module_args').being.equal(params)

# Generated at 2022-06-13 10:18:24.378940
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test run method of class ActionModule."""
    ActionModule_obj = ActionModule('data')
    result = ActionModule_obj.run(tmp='testdata', task_vars={'data': True})
    assert result == {}
    assert result == {'invocation': {'module_name': 'setup'}}

# Generated at 2022-06-13 10:18:30.764471
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import constants as C
    from ansible.utils.vars import merge_hash
    from ansible.plugins.action import ActionBase
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    import sys
    import os
    import tempfile
    module_name = "test_module.py"
    module_args = "test"
    action = "test_action"
    console= Display()
    tmpdir = tempfile.mkdtemp()
    filename = os.path.join(tmpdir, module_name)

# Generated at 2022-06-13 10:18:42.411885
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test with async_val = True but without a shell module
    class ActionModule_minimal(ActionModule):
        pass
    module = ActionModule_minimal(
        task=dict(async_val=1),
        connection=dict(has_native_async=0))
    result = module.run()
    assert result['_ansible_async'] == 1

    # Test with async_val = True and a shell module
    class ActionModule_minimal(ActionModule):
        pass
    module = ActionModule_minimal(
        task=dict(async_val=1),
        connection=dict(has_native_async=1))
    result = module.run()
    assert result['_ansible_async'] == 1

    # Test with async_val = False and a shell module

# Generated at 2022-06-13 10:18:59.755570
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test `ActionModule` class
    """
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # `_supports_check_mode` is a instance attribute of class ActionBase
    assert module._supports_check_mode == True
    # `_supports_async` is a instance attribute of class ActionBase
    assert module._supports_async == True

# Generated at 2022-06-13 10:19:01.348110
# Unit test for constructor of class ActionModule
def test_ActionModule():
	action_module = ActionModule()
	assert action_module._supports_check_mode == True
	assert action_module._supports_async == True

# Generated at 2022-06-13 10:19:09.343677
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.normal as normal
    import ansible.plugins.connection.connection as connection
    import ansible.plugins.loader as loader
    import ansible.task.task as task
    import ansible.template.template as template

    # Setup data for test
    connection._load_plugins()
    task_ds = dict()
    loader._module_cache = dict()

    # Test constructor of ActionModule
    action = normal.ActionModule(task.Task(task_ds, connection.Connection('', '', 0), template.Template()), loader)
    assert action.task._ds == task_ds
    assert action.task.template is not None
    assert action._shared_loader_obj.module_cache == dict()

# Generated at 2022-06-13 10:19:18.588695
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook_yaml import YAMLPlaybook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.include import Include
    from ansible.constants import DEFAULT_HANDLER_NAME
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.vars.resolver import TaskVars
    from ansible.module_utils.facts import Facts
    from ansible.utils.vars import combine_vars

# Generated at 2022-06-13 10:19:27.899825
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule
    # Finally create and return an ansible module instance
    module = AnsibleModule(argument_spec=dict())
    #print(module.__class__)

    #from ansible.playbook.play_context import PlayContext
    #play_context = PlayContext()

    action_module = ActionModule(module, "", "", module.params, "", {}, {}, {})
    #print(action_module.__class__)

    assert action_module.run(module.params) is not None

# Generated at 2022-06-13 10:19:37.031098
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup object
    task_vars = {'foo': 'bar'}
    wrap_async = True
    action = 'genericwin_something'

    # Create mock objects and set return values
    tmp = None
    result = {'skipped': False, 'invocation': {'module_args': {}}}

    # Set up Mock objects
    mock_execute_module = mocker.MagicMock(return_value = {'ansible_result': 'something'})
    mocker.patch('ansible.plugins.action.ActionModule._execute_module', mock_execute_module)
    mock_remove_tmp_path = mocker.MagicMock()
    mocker.patch('ansible.plugins.action.ActionModule._remove_tmp_path', mock_remove_tmp_path)
    mock_new_module_result = mocker

# Generated at 2022-06-13 10:19:37.553397
# Unit test for constructor of class ActionModule
def test_ActionModule():
      assert ActionModule

# Generated at 2022-06-13 10:19:39.226545
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # this doesn't have to actually test anything,
    # just make sure it never crashes.
    a = ActionModule(None, None, None)

# Generated at 2022-06-13 10:19:40.384959
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am.get_action() == 'generic'

# Generated at 2022-06-13 10:19:47.081284
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  ## Initial setup
  # Create dummy variables
  task_vars = {}
  host = ""
  task = ""
  connection = ""

  # Setup test object
  test_object = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

  # Run test
  result = test_object.run(task_vars=task_vars)

  # Assert Test
  assert result == expected_result


# Generated at 2022-06-13 10:20:16.451714
# Unit test for constructor of class ActionModule
def test_ActionModule():

    import ansible.plugins
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.stats import AggregateStats
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.ssh_functions import load_ssh_conn_config

# Generated at 2022-06-13 10:20:18.243817
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None, None)
    assert module is not None
    assert module.supports_check_mode is True
    assert module.supports_async is True

# Generated at 2022-06-13 10:20:22.967185
# Unit test for constructor of class ActionModule
def test_ActionModule():
    instantiate = ActionModule(ActionBase._task, ActionBase._connection, ActionBase._play_context, ActionBase._loader, ActionBase._templar, ActionBase._shared_loader_obj)
    assert instantiate is not None


# Generated at 2022-06-13 10:20:23.918102
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:20:26.374191
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test for default constructor
    assert ActionModule()

    # test for constructor with arguments
    assert ActionModule(1)


# Generated at 2022-06-13 10:20:27.131736
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:20:29.456488
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:20:30.983620
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None, {}), ActionModule)


# Generated at 2022-06-13 10:20:33.544602
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module._supports_check_mode == True
    assert module._supports_async == True

# Generated at 2022-06-13 10:20:44.229833
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.module_utils.common.removed import removed
    # Test to check the constructor and other variables
    action_module = ActionModule()
    assert action_module._supports_async is True
    assert action_module._connection._shell.tmpdir is not None
    assert action_module._uses_shell is False
    assert action_module._uses_unsafe_shell is False

    # Test to check _action_module_compat_checks and ActionModuleDeprecationWarning
    with removed(version="2.10"):
        action_module_compat_checks = action_module._action_module_compat_checks()
        assert type(action_module_compat_checks) is ActionModuleDeprecationWarning
        assert action_module_compat_checks.version == "2.10"

# Generated at 2022-06-13 10:21:31.052205
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: Write unit tests
    assert True, "TODO: Write unit tests"

# Generated at 2022-06-13 10:21:31.701348
# Unit test for constructor of class ActionModule
def test_ActionModule():
    Am=ActionModule()
    Am.run()

# Generated at 2022-06-13 10:21:37.395376
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

    from ansible.plugins import module_loader
    import ansible.constants as C

    ActionModule.__dict__['_get_task_context'](ActionModule)
    module_loader.find_plugin('debug')
    action_module = module_loader.find_plugin('action')
    action_module._load_params()
    action_module._display.verbosity = 0
    #m = ActionModule()
    #m.initialize(Task(), Play())
    #result = m.run(task_vars={})
    #print(result)

# Generated at 2022-06-13 10:21:39.014760
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    """
    assert False


# Generated at 2022-06-13 10:21:49.103517
# Unit test for constructor of class ActionModule
def test_ActionModule():
    sample_task = {
        'async': 1,
        'connection': 'local',
        'delegate_to': 'localhost',
        'name': 'task6',
        'action': 'moduletest',
        'args': {
            'foo': 'bar'
        },
        'register': 'result6'
    }

    # Need one of the following to be true. If both are true, then we need to create a scenario where
    # async is set to a value but the connection is not local.
    if False and False:
        assert False, "Async is not set to true. Setting async to true."
        sample_task['async'] = True
    elif False and False:
        assert False, "Async is set to true but connection is not local. Setting connection to local."

# Generated at 2022-06-13 10:21:57.064561
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display

    display = Display()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 10:21:58.025207
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:22:11.217509
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)
    test_task = Task()
    test_task.action = 'setup'
    test_task._uuid = 'bogus'

# Generated at 2022-06-13 10:22:13.426603
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    print(module)
    assert module

if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 10:22:21.450792
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.errors import AnsibleActionModuleFailed
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action import ActionBase
    from ansible.utils import context_objects as co
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.vars.persistentvars import PersistentVars

    class TestActionModule(ActionModule):
        pass

    class TestActionBase(ActionBase):
        def _execute_module(self, module_name=None, module_args=None, task_vars=None, wrap_async=None):
            return {
                'changed': False,
                'ping': 'pong'
            }


# Generated at 2022-06-13 10:24:18.691440
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action
    A = ansible.plugins.action.ActionModule('action','local','127.0.0.1','/bin','/usr/bin/ansible','file','script')
    A.run()

# Generated at 2022-06-13 10:24:28.222117
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.connection import ConnectionBase
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars
    import json
    import unittest

# Generated at 2022-06-13 10:24:29.467967
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert type(am).__name__ == 'ActionModule'

# Generated at 2022-06-13 10:24:37.895410
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._task = {}
    module._task["async_val"] = 0 
    module._task["action"] = "setup"
    module._supports_check_mode = True
    module._supports_async = True
    module._connection = {}
    module._execute_module = lambda x,y,z: 0
    module._remove_tmp_path = lambda x: 0
    module._connection._shell = {}
    module._connection._shell.tmpdir = 1
    result = module.run(task_vars = 0, tmp = 0)

# Generated at 2022-06-13 10:24:39.481494
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("In test_ActionModule")
    my_actionmodule = ActionModule()


# Generated at 2022-06-13 10:24:48.659879
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = "127.0.0.1"
    port = 80
    user = "root"
    password = "password"
    connection = "smart"
    tmp = "/usr/tmp"
    task_vars = {}
    Inven = {}
    module_name = "shell"
    module_args = "ls -al"
    invalid_attribute = "invalid_attribute"

    obj = ActionModule()

    print("unit test started!")

    print("Test 1: initialize the object")
    result = obj
    assert result is not None
    assert isinstance(result, ActionModule)

    print("Test 2: set connection")
    result = obj._set_connection(host, port, user, password, connection)
    assert result is None

    print("Test 3: set temp path")
    result = obj._set_tmp

# Generated at 2022-06-13 10:24:49.754651
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not ActionModule()

# Generated at 2022-06-13 10:24:54.287181
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    cls = ActionModule('ActionModule')
    cls._task = {'action': 'setup'}
    cls._connection = {'has_native_async': True}
    assert cls.run()

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:24:55.168711
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == 'ActionModule'

# Generated at 2022-06-13 10:24:55.816745
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass