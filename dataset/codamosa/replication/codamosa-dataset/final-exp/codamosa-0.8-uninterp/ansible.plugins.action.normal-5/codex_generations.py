

# Generated at 2022-06-13 10:16:11.666494
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 10:16:12.525472
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:16:23.723044
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook import Play
    from ansible.playbook.task import Task

    the_play = Play().load({
        'name' : "Ansible Play",
        'hosts': 'test',
        'tasks': [
            {
                'action': {
                    'module': 'ping',
                    'args': 'data=test'
                },
                'name': 'ping'
            }
        ]
    }, variable_manager={}, loader=None)
    the_task = Task().load(the_play.tasks()[0], the_play, variable_manager=None, loader=None)

    am = ActionModule(the_task, the_play._variable_manager, loader=None, templar=None, shared_loader_obj=None)
    assert(isinstance(am, ActionModule))

# Generated at 2022-06-13 10:16:24.675726
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()

    assert actionModule

# Generated at 2022-06-13 10:16:36.036453
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils import basic
    from ansible.module_utils.connection import ConnectionBase
    from ansible.plugins.connection import ConnectionBase as ConnectionBasePlugin
    from ansible.plugins.loader import module_loader
    from ansible.plugins.module_utils import basic as basic_module_utils
    import mock

    class MyActionModule(ActionModule):
        TRANSFERS_FILES = True
        _connection_plugins_path = [ConnectionBasePlugin]

    # Mock the basic and connection module utils that are used by action plugins
    with mock.patch.dict(module_loader._module_utils_loader.module_utils, basic=basic, connection=ConnectionBase):
        am = MyActionModule(mock.MagicMock())

    # Constructor sets instance variables
    assert am._shared_loader_obj is not None
    assert am

# Generated at 2022-06-13 10:16:36.823148
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:16:42.897392
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    m.ActionModule = (ActionModule, {})
    #m.ActionModule = True
    #assert(m.run() == {"failed": True, "msg": "ActionModule: called by test"})
    assert(m.run() == {"failed": True, "msg": "ActionModule: not implemented"})


# Generated at 2022-06-13 10:16:52.255353
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create test object
    a = ActionModule()

    # Create mock objects
    t = type('MockTask', (object,), {})
    setattr(t, 'async_val', 1)
    setattr(t, 'action', 'setup')
    s = type('MockConnection', (object,), {})
    setattr(s, '_shell', type('MockShell', (object,), {}))
    setattr(s._shell, 'tmpdir', '/tmp/')
    setattr(s, 'has_native_async', False)
    setattr(s, '_shell', type('MockShell', (object,), {}))
    setattr(s._shell, 'tmpdir', '/tmp/')
    setattr(s, '_shell', type('MockShell', (object,), {}))


# Generated at 2022-06-13 10:16:53.968201
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionBase('test', 'test_connection')
    assert True

# Generated at 2022-06-13 10:16:55.672761
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule()
    assert actionModule.run()

# Generated at 2022-06-13 10:17:05.159166
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    This is a unit test for constructor of ActionModule class
    """
    #call the constructor of class ActionModule
    action_mod = ActionModule()

    #check if the object created is not empty
    assert action_mod is not None, "ActionModule constructor failed"
    assert action_mod._supports_check_mode == True, "ActionModule check mode support not set"
    assert action_mod._supports_async == True, "ActionModule async support not set"

# Generated at 2022-06-13 10:17:08.416065
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    result = m.run()
    assert result['_ansible_verbose_override'] == True
    assert result['skipped'] == False
    assert result['changed'] == True
    assert result['failed'] == False

# Generated at 2022-06-13 10:17:13.067451
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # unit test for constructor
    a = ActionModule(None, None, None, None, None, None)
    assert not a is None
    assert a._supports_check_mode

    # test run
    a = ActionModule(dict(), dict(), dict(), dict(), dict(), dict())
    a._task = a
    a._supports_check_mode = True
    a._supports_async = True
    a.run('/tmp', dict())

# Generated at 2022-06-13 10:17:23.270746
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import os
    import json
    import tempfile

    mydir = os.path.dirname(__file__)
    sys.path.insert(0,mydir + "/../module_utils/")
    sys.path.insert(0,mydir + "/../modules/")
    mydir2 = os.path.dirname(__file__)
    sys.path.insert(0, mydir2 + "/../")

    from AnsibleModule import AnsibleModule

    #to make sure it can load required modules
    from ansible.module_utils.basic import AnsibleModule

    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, call, Mock
    from ansible.module_utils.six import PY3

    from ansible.plugins import action
   

# Generated at 2022-06-13 10:17:26.085926
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None) is not None

# Generated at 2022-06-13 10:17:37.092969
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_run = ActionModule(None, None, None, None, None)
    test_run._supports_async = True
    test_run._supports_check_mode = True
    test_run.run(None, None)
    test_run._supports_async = False
    test_run.run(None, None)
    test_run._connection.has_native_async = True
    test_run.run(None, None)
    test_run._connection.has_native_async = False
    test_run._task.async_val = None
    test_run.run(None, None)
    test_run._task.async_val = "0"
    test_run.run(None, None)
    test_run._task.async_val = "0.2"


# Generated at 2022-06-13 10:17:46.114051
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.normal import ActionModule
    import ansible.utils.json_encoder
    import ansible.plugins.connection.local
    import ansible.plugins.strategy.linear
    import ansible.plugins.loader
    class ClassModuleMock():
        def __init__(self, task_vars):
            self.task_vars = task_vars
    class ClassActionMock():
        def __init__(self, async_val):
            self.async_val = async_val
        def set_running_async(self, async_val):
            self.async_val = async_val
    class ClassConnectionMock():
        def __init__(self, has_native_async):
            self.has_native_async = has_native_async

# Generated at 2022-06-13 10:17:54.617264
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ssh = 'sshpass -p "password" ssh -o "StrictHostKeyChecking=no" -l "user" 127.0.0.1'

# Generated at 2022-06-13 10:17:55.060093
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  pass

# Generated at 2022-06-13 10:18:03.409608
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import json
    import sys
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    class ActionModule_run_Test(ActionModule):
        module_args = 'test_key=test_value'
        _uses_shell = False
        _uses_delegate = False
        filter_loader = False
        _supports_check_mode = True


# Generated at 2022-06-13 10:18:13.479963
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    am.task_vars = {}
    am.tmp = ""
    print(am.run())
#
#Unit test for method run of class ActionModule
#if __name__ == "__main__":
#    test_ActionModule_run()

# Generated at 2022-06-13 10:18:15.072337
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 10:18:22.905478
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.normal import ActionModule

    action_plugin = ActionModule()
    # Test with module return value
    result = { 'x': 1, 'y': 2, 'z': 3 }
    action_plugin._execute_module = lambda task_vars, wrap_async: result
    result = action_plugin.run(task_vars=dict(a=1, b=2, c=3))
    assert result == {'x': 1, 'y': 2, 'z': 3}
    # Test with async
    action_plugin._task.async_val = 10
    action_plugin._connection.has_native_async = True
    result = action_plugin.run(task_vars=dict(a=1, b=2, c=3))

# Generated at 2022-06-13 10:18:24.265650
# Unit test for method run of class ActionModule
def test_ActionModule_run():
        assert False #I don't know how to test this function


# Generated at 2022-06-13 10:18:25.660500
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass # TODO: write unit test

# Generated at 2022-06-13 10:18:27.902504
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule("/folder/action_plugins/action_module.py")
    assert action_module is not None

# Generated at 2022-06-13 10:18:30.573668
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a test ActionModule
    testaction = ActionModule()
    testaction.__init__()
    assert testaction != None

# Generated at 2022-06-13 10:18:38.604741
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Arrange
    tmp = None
    task_vars = None

    from ansible.plugins.action import ActionBase
    action_base = ActionBase()
    action_base._supports_check_mode = True
    action_base._supports_async = True
    action_base._task = {"action": "setup"}
    action_module = ActionModule()

    # Act
    action_module.run(tmp=tmp,task_vars=task_vars)

    # Assert

# Generated at 2022-06-13 10:18:43.646364
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    task_vars = {}
    tmp = '/tmp'
    module._supports_check_mode = True
    module._supports_async = True
    module._task.async_val = True
    module._connection.has_native_async = False
    result={'invocation': {'module_args': 'test'}}
    module.run(tmp, task_vars)

# Generated at 2022-06-13 10:18:51.605584
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Define test variables and constants
    task_vars = dict()
    wrap_async = True
    result = dict()
    # TODO: better to let _execute_module calculate this internally?
    wrap_async = True
    # Define expected values
    expected = dict()
    # Define action_object of class ActionModule
    action_object = ActionModule(connection=None, task_vars=task_vars)
    # Get method run of class ActionModule
    method = getattr(action_object, 'run')
    # Call method run of class ActionModule with arguments
    result = method(tmp=None, task_vars=task_vars)
    # Verify method run of class ActionModule
    assert result == expected

# Generated at 2022-06-13 10:19:11.340120
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import module_loader

    task_vars = dict(
        ansible_ssh_host='ssh.server.example.com',
        ansible_ssh_user='vagrant',
        ansible_ssh_port=22,
        ansible_ssh_private_key_file='/home/vagrant/.ssh/private_ssh_key',
        ansible_ssh_pass='vagrant',
        ansible_sudo_pass='vagrant',
    )
    tmp = '/tmp'
    m = module_loader._load_module_source('ping', '/usr/lib/python2.7/site-packages/ansible/modules/commands/ping.py')
    task = dict(action=dict(module='ping'), args={})
    action = ActionModule(task, m, connection=None)
    result

# Generated at 2022-06-13 10:19:12.916018
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    x = ActionModule()
    # As class ActionModule does not implement method run, this test should raise an error
    raise NotImplementedError(3)

# Generated at 2022-06-13 10:19:23.697617
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.utils.vars import merge_hash
    from ansible.context import AnsibleContext
    from ansible.plugins import module_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.action.normal import ActionModule as NormalActionModule
    from ansible.executor.task_result import TaskResult

# Generated at 2022-06-13 10:19:33.539529
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an ActionModule object
    action_module = ActionModule('/path/file', 'play', 'task', None, None, None, None)

    # Compare the values of the attributes of the class
    assert action_module._task_name == 'task'
    assert action_module._task == 'task'
    assert action_module._role_name == ''
    assert action_module._loader == '/path/file'
    assert action_module._shared_loader_obj == '/path/file'
    assert action_module._play_context == ''
    assert action_module._new_stdin == None
    assert action_module._task_vars == {}
    assert action_module._templar == None
    assert action_module._connection == None
    assert action_module._tmp == None
    assert action_module._module_name == None

# Generated at 2022-06-13 10:19:34.657179
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    a.run()

# Generated at 2022-06-13 10:19:42.112736
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys

    sys.path.append("~/PycharmProjects/ansible/test")
    from unit.mock.loader import DictDataLoader

    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager


# Generated at 2022-06-13 10:19:53.739455
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
        Test run method of class ActionModule
    """
    uuid = 'mocked_uuid'
    task_vars = dict(foo='bar')
    connection = object()
    module_name = 'ping'
    module_args = dict(a='b')
    async_val = 1

    m = ActionModule()
    # direct call of method run
    m.run(task_vars=task_vars)
    # test call of method run with mocked run method
    m2 = ActionModule()
    m2.run = lambda self, tmp=None, task_vars=None: dict(foo='bar')
    m2.run(task_vars=task_vars)
    # test call of method run with mocked run method with raised exception
    m3 = ActionModule()

# Generated at 2022-06-13 10:19:54.765329
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "Test not implemented"



# Generated at 2022-06-13 10:20:04.180096
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  from ansible.plugins.action import ActionModule
  from ansible.module_utils._text import to_native
  import os
  import pytest
  from collections import namedtuple
  from ansible.playbook.task import Task
  from ansible.playbook.task_include import TaskInclude
  from ansible.executor.task_result import TaskResult
  from ansible.executor.play_context import PlayContext
  # create connection object
  Connection = namedtuple('Connection', ('_shell',))
  class Shell:
    tmpdir = 'tmpdir'
  connection = Connection(Shell())
  # create task result object
  task_result = TaskResult()
  task_result.host = 'blah'
  # create task object
  task = Task()
  task.action = 'include_role'

# Generated at 2022-06-13 10:20:07.385797
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    action_mod   = ActionModule()
    assert action_mod is not None

# Generated at 2022-06-13 10:20:32.390048
# Unit test for constructor of class ActionModule
def test_ActionModule():

    actionmodule = ActionModule()
    assert bool(actionmodule)
    assert bool(actionmodule.run())

# Generated at 2022-06-13 10:20:42.764742
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import copy
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    task = Task()
    context = PlayContext()
    context.connection = 'smart'

    # test for method run()
    task.module_name = 'command'
    task.async_val = False
    task.module_args = {'_raw_params': 'echo "Hello World!', '_uses_shell': True}
    task.action = 'command'

    obj_ActionModule = ActionModule(task, context)
    obj_ActionModule._supports_async = True
    obj_ActionModule._connection = 'smart'
    obj_ActionModule._task = obj_ActionModule._task

    # call method run()
    result = obj_ActionModule.run(task_vars={})

# Generated at 2022-06-13 10:20:47.472194
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of ActionModule that inherits the mock class 'ActionBase'
    actionModule = ActionModule()

    # Test the '_supports_async' and 'supports_check_mode' attributes for the ActionModule class
    assert actionModule._supports_async == True
    assert actionModule._supports_check_mode == True

# Generated at 2022-06-13 10:20:52.099450
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(
        task=dict(args=dict(foo='bar')),
        connection=dict(host='localhost', port=1, user='joe', password='test'),
        play_context=dict(remote_addr='test', remote_user='test'),
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )

# Generated at 2022-06-13 10:21:04.923141
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = Task()
    task._supports_async = True
    task._supports_check_mode = True
    task._supports_subset = True
    task._supports_subset = True
    task._supports_subset = True
    task._supports_subset = True
    task._supports_subset = True
    task._supports_subset = True
    action = ActionModule()
    task_vars = {}
    tmp = "path"

    x = task.async_val
    y = action._connection.has_native_async
    wrap_async = (x and not y)

    result = action.run(tmp, task_vars)
    print(result)

# Generated at 2022-06-13 10:21:15.423389
# Unit test for constructor of class ActionModule
def test_ActionModule():

    def _execute_module(self, task_vars=dict(), wrap_async=False):
        return {'_ansible_verbose_override': True}

    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.default import ActionModule

    ActionBase.CONNECTION_PLUGIN_CLASS = 'ansible.plugins.connection.local.Connection'

    x = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    x._execute_module = _execute_module
    y = x.run({}, {})
    assert y['_ansible_verbose_override']

# Generated at 2022-06-13 10:21:17.782893
# Unit test for constructor of class ActionModule
def test_ActionModule():
    args = dict(foo='bar')
    action = ActionModule(None, args)
    assert action._task._attributes['action'] == 'bar'

# Generated at 2022-06-13 10:21:29.342893
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.cli.playbook import PlaybookCLI
 
    # Create loader object 
    loader = DataLoader()

    # Create the inventory, use path to host config file as source or hosts in a comma separated string
    inventory = Inventory(loader=loader, 
                          sources=['localhost'])

   

# Generated at 2022-06-13 10:21:36.527720
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Run a unit test on class ActionModule
    """
    # Get instance of task
    task = {}
    # Get instance of connection
    connection = object
    # Get instance of loader
    loader = object
    # Get instance of templar
    templar = object
    # Get instance of shared loader
    shared_loader = object
    # Make the instance of class ActionModule
    obj = ActionModule(task, connection, loader, templar, shared_loader)

    # Check if instance is of type ActionModule
    assert isinstance(obj, ActionModule)

# Generated at 2022-06-13 10:21:42.929790
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an object of the class under test.
    # This is the call to the constructor.
    act_mod = ActionModule(task=object(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # Make assertions about the constructed object.
    assert isinstance(act_mod, ActionBase)
    assert isinstance(act_mod, ActionModule)


# Generated at 2022-06-13 10:22:42.020953
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "Test not implemented"

# Generated at 2022-06-13 10:22:43.144620
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module,ActionModule)


# Generated at 2022-06-13 10:22:48.387845
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Constructor ActionModule test"""
    import ansible.plugins.loader
    import sys
    import ansible.playbook
    import ansible.inventory

    action_plugin = ansible.plugins.action.ActionModule(
        task=ansible.playbook.Task(),
        connection=ansible.plugins.loader.connection_loader.get('local', class_only=True)()
    )
    assert isinstance(action_plugin, ActionModule)

# Generated at 2022-06-13 10:22:48.922262
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:23:00.382634
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import os
    import tempfile
    from ansible.module_utils.basic import AnsibleModule, _load_params
    from ansible.module_utils.six.moves import StringIO
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    my_args = {
        '_ansible_verbosity': 4,
        '_ansible_no_log': False,
        '_ansible_debug': True
    }

    def dummy_load_params():
        pass

    def dummy_run_command(*args, **kwargs):
        return 0, '', ''
   

# Generated at 2022-06-13 10:23:07.062563
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.playbook.task
    import ansible.utils.vars
    import ansible.template
    import ansible.executor.task_queue_manager

    my_task = ansible.playbook.task.Task()
    my_task_vars = ansible.utils.vars.VariableManager()
    my_loader = ansible.template.AnsibleBaseLoader()

    my_module = ActionModule(my_task, my_task_vars, my_loader)
    assert my_module._task == my_task
    assert my_module._task_vars == my_task_vars
    assert my_module._loader == my_loader

    my_task._role = ansible.playbook.role.Role()
    my_task.role._role_path = "/does/not/exist"

# Generated at 2022-06-13 10:23:08.637012
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    runner = ActionModule()
    result = runner.run()
    assert result == {}

# Generated at 2022-06-13 10:23:21.264658
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    This is a Unit Test for ActionModule constructor
    """
    #Creating Mock for the ActionBase
    class mock_action_base(object):
        def __init__(self,task,connection,play_context,loader,templar,shared_loader_obj):
            self._task = task
            self._connection = connection
            self._play_context = play_context
            self._loader = loader
            self._templar = templar
            self._shared_loader_obj = shared_loader_obj
            self.action_plugins_path = None
            self._config_module = None
    class mock_task(object):
        def __init__(self):
            self.action = "setup"
            self.async_val = False

# Generated at 2022-06-13 10:23:23.366904
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO(szuecs): test with real object
    pass

# Generated at 2022-06-13 10:23:23.941116
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule != None

# Generated at 2022-06-13 10:25:43.485130
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Pseudo args which would come in through the cli
    pseudovars = {}
    pseudovars['action'] = 'ActionModule'
    pseudovars['actionplugin'] = 'ActionModule'
    pseudovars['actionpluginname'] = pseudovars['actionplugin']
    pseudovars['playbook'] = 'ActionModule'
    pseudovars['task'] = 'ActionModule'

    # Initialize the class
    test_action_module = ActionModule(pseudovars, {})

# Generated at 2022-06-13 10:25:44.097554
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:25:47.189267
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule({})
    assert(a._supports_async)
    assert(a._supports_check_mode)
    assert(a._connection)
    assert(a._task)

# Generated at 2022-06-13 10:25:49.018922
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None,None)
    assert action != None

# Generated at 2022-06-13 10:25:51.542418
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule('setup', 'localhost', 'root', 'setup', 'setup', 'setup', 'setup', 'setup')

# Generated at 2022-06-13 10:25:55.545363
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    from ansible.plugins.loader import action_loader
    a = ActionModule(action_loader, 'fake', {}, {})
    assert a.action_name == 'fake'

# Generated at 2022-06-13 10:25:56.064967
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:25:57.314062
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule('/tmp', 'inventory', 'connection')
    assert mod is not None


# Generated at 2022-06-13 10:26:06.404507
# Unit test for method run of class ActionModule