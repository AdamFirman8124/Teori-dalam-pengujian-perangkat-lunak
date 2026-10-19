

# Generated at 2022-06-13 10:52:48.206923
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule()
    actionModule._shared_loader_obj = None
    actionModule._task = None
    actionModule._connection = None
    actionModule._play_context = None
    actionModule._loader = None
    actionModule._templar = None
    actionModule._shared_loader_obj = None
    result = actionModule.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:52:48.812885
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:52:49.708509
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:53:01.275078
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.command import ActionModule
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import builtins

    # build a class that has the properties we need for command_action below
    class FakeActionBase(ActionBase):
        def __init__(self):
            self.loader = None
            self.task = None
            self.connection = None
            self.play_context = None
            self.templar = None
            self.shared_loader_obj = None

    # build a class that has the properties we need for task below
    class FakeArgs(object):
        def __init__(self):
            self.cmd = "adduser"

# Generated at 2022-06-13 10:53:02.504199
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_action_run('ActionModule')

# Generated at 2022-06-13 10:53:08.249876
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_module = ActionModule(runner=None)
    test_module._task.args['_uses_shell'] = True
    test_module._task.args['_raw_params'] = 'pwd'
    from ansible.module_utils.common.process import get_bin_path
    from ansible.utils.display import Display
    display = Display()
    bins = get_bin_path(display, 'pwd', None)
    test_module._task.args['_raw_params'] = bins
    test_module._task.action = 'shell'
    result = test_module.run()
    assert result['cmd'] == bins

if __name__ == "__main__":
    test_ActionModule_run()

# Generated at 2022-06-13 10:53:09.707810
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:23.121834
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six.moves.builtins import exec_module
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.six import PY2

    _module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
        add_file_common_args=True,
    )
    _connection = 'local'

# Generated at 2022-06-13 10:53:29.358746
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_task = { 'args' : {}}
    mock_args = {}
    mock_loader = {}
    mock_shared_loader_obj = { 'action_loader' : {'ansible.legacy.command' : { 'run' : MockActionModule.run }}}
    mock_play_context = {'_shell_executable' : None}
    mock_connection = {}
    mock_task_vars = None

    a = ActionModule(mock_task, mock_args, mock_loader, mock_shared_loader_obj, mock_play_context, mock_connection)

    # Using regular function
    result = a.run(task_vars=mock_task_vars)
    assert result['changed'] == False
    assert result['msg'] == 'Command run'

    # Using mock

# Generated at 2022-06-13 10:53:33.327508
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    assert action_module is not None

    result = action_module.run(None, None)
    assert result == {'stdout': '', 'stderr': '', 'stdout_lines': [], 'stderr_lines': [], 'rc': 0}

# Generated at 2022-06-13 10:53:37.486114
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # See the following code for an example of how to define
    # run() in an action plugin:
    #  ansible/plugins/action/command.py
    assert True

# Generated at 2022-06-13 10:53:39.254923
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    result = mod.run(None, None)
    assert result['rc'] == 0

# Generated at 2022-06-13 10:53:39.802761
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  pass

# Generated at 2022-06-13 10:53:41.244141
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    print("\nTEST01: Method run from class ActionModule")

    print("\nTEST END \n")

# Generated at 2022-06-13 10:53:51.665087
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import types
    import os
    from ansible.errors import AnsibleError
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import connection_loader, module_loader, action_loader
    from ansible.plugins.connection import local
    import ansible.parsing.dataloader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.color import ANSIBLE_COLOR, stringc
    from ansible.utils.path import unfrackpath
    from ansible.module_utils._text import to_bytes, to_text

    test_args = {}

# Generated at 2022-06-13 10:53:52.804213
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run"""


# Generated at 2022-06-13 10:53:53.779590
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

# Generated at 2022-06-13 10:54:00.281572
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.plugins.action import ActionModule
    from ansible.module_utils.six import PY3

    # XXX: The following fails with a AttributeError: 'NoneType' object has no attribute 'find_plugin'
    #action_module = ActionModule()

    # Call with mandatory argument and keyword arguments
    #print('tmp:\n{0}'.format(tmp))
    #print('task_vars:\n{0}'.format(task_vars))
    #if PY3:
    #    assert isinstance(action_module.run(tmp, task_vars), dict)
    #else:
    #    assert isinstance(action_module.run(tmp, task_vars), unicode)

    return True


# Generated at 2022-06-13 10:54:10.665016
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # This test is using the public API but it's fine to do so because we are
    # testing the API as part of the role.  It's not a part of Ansible.
    from ansible.plugins.action import ActionBase
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.path import mock_unfrackpath_warndirnotfound

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-13 10:54:11.270034
# Unit test for method run of class ActionModule
def test_ActionModule_run():

	assert False

# Generated at 2022-06-13 10:54:28.798297
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test ActionModule.run method"""

    # Mock the task object
    base_task = mock.Mock()
    base_task._connection = None
    base_task._play_context = None
    base_task.args = {}
    base_task.module_args = {}

    # Mock the ActionModule object
    action_module = ActionModule(base_task, None)
    action_module._shared_loader_obj = mock.Mock()
    action_module._shared_loader_obj.action_loader = mock.Mock()
    action_module._shared_loader_obj.action_loader.get.return_value = mock.Mock()
    action_module._templar = mock.Mock()

    # Execute the action module run method
    action_module.run(None, None)

    assert action_module._

# Generated at 2022-06-13 10:54:40.095288
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockActionModule(ActionBase):
        pass
    mock_ActionBase_returned_obj = MockActionModule()
    mock_ActionBase_returned_obj.action_loader = object
    mock_ActionBase_returned_obj._shared_loader_obj = object
    mock_ActionBase_returned_obj._task = object
    mock_ActionBase_returned_obj._connection = object
    mock_ActionBase_returned_obj._play_context = object
    mock_ActionBase_returned_obj._loader = object
    mock_ActionBase_returned_obj._templar = object
    ActionBase_get_patch = patch('ansible.plugins.action.ActionBase.get', return_value=mock_ActionBase_returned_obj)

# Generated at 2022-06-13 10:54:40.603711
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:41.841583
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    """
    pass

# Generated at 2022-06-13 10:54:42.350174
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:49.356641
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # GIVEN
    import ansible.plugins.action.command
    module = ansible.plugins.action.command
    module._setup_task_args = lambda self: None
    module._task = lambda self: None
    module._templar = lambda self: None
    module._shared_loader_obj = lambda self: None
    module._loader = lambda self: None
    module._connection = lambda self: None
    module._play_context = lambda self: None
    # WHEN
    action = module.ActionModule()
    # THEN
    assert action is not None

# Generated at 2022-06-13 10:54:50.602286
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule

    obj = ActionModule('', '', '', '', {'_uses_shell': True}, '', '')
    obj.run('tmp', {})

# Generated at 2022-06-13 10:55:00.674144
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initializing action module with necessary values
    # Adding values for required keys for ansible-playbook run
    action_record = {
        "action": {
            "__ansible_module__": "ansible.legacy.shell"
        },
        "ansible_loop_var": "item",
        "changed": False,
        "failed": False,
        "invocation": {
            "module_args": {
                "argv": "ps -ef | grep -- --version",
                "_raw_params": "ps -ef | grep -- --version"
            }
        },
        "item": "/home/ansible/anaconda3/bin/python",
        "playbook_dir": "/home/ansible",
        "skip_reason": "Conditional result was False",
        "skipped": True
    }


# Generated at 2022-06-13 10:55:10.230443
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from unit.mock.loader import DictDataLoader
    from ansible import context
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.plugins.task_vars import TaskVars
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.action.command import ActionModule as command_ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import load_extra_vars

    #
    # Create objects
    #
    # Create task queue manager.
    loader = DictDataLoader({})

    context.CLIARGS = {}

# Generated at 2022-06-13 10:55:20.457846
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of ActionModule class
    # (as if Ansible ran a module through a plugin)
    am = ActionModule()
    # Create a mock task instance
    task_instance = MockTask()
    # Set am._task to the mock task instance
    am._task = task_instance
    # Create a mock shared loader object instance
    shared_loader_obj = MockSharedLoaderObj()
    # Set the _shared_loader_obj attribute of am to the mock shared loader object instance
    am._shared_loader_obj = shared_loader_obj
    # Create a mock connection object instance
    connection = MockConnection()
    # Set am._connection to the mock connection object instance
    am._connection = connection
    # Create a mock play context instance
    play_context = MockPlayContext()
    # Set am._play_context to the mock play context instance

# Generated at 2022-06-13 10:55:29.619388
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_object = ActionModule({},{},[])
    try:
        test_object.run()
    except Exception as e:
        assert(str(e) == 'A module loader is required to execute this Action')

# Generated at 2022-06-13 10:55:35.688023
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.six import PY2

    action = ActionModule(loader=None,
                          shared_loader_obj=None,
                          connection=None,
                          play_context=None,
                          new_stdin=None,
                          task=None,
                          executor=None,
                          templar=None,
                          loader_cache=None)

    tmp = 'test'
    task_vars = dict(a=123, b=456)
    result = action.run(tmp=tmp, task_vars=task_vars)


# Generated at 2022-06-13 10:55:36.530923
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 1 == 1

# Generated at 2022-06-13 10:55:50.160825
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  from ansible.plugins.action.command import ActionModule
  from ansible.vars.unsafe_proxy import AnsibleUnsafeText
  from ansible.inventory.host import Host
  from ansible.playbook.play import Play
  
  from ansible.playbook.task import Task
  from ansible.plugins.task import TaskBase
  from ansible.plugins.action import ActionBase

  from ansible.plugins.loader import find_plugin
  command_action = find_plugin(ActionBase, 'command')
  command_action = command_action()

  shell_action = find_plugin(ActionBase, 'shell')
  shell_action = shell_action()
  task = Task(
        action=dict(
            module='shell',
            args={'_uses_shell': True},
            ), 
        )


# Generated at 2022-06-13 10:55:51.474739
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    assert(True)

# Generated at 2022-06-13 10:55:59.268370
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(
        task=dict(action=dict(module='shell')),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    result = module.run(tmp=None, task_vars=None)
    assert result is not None
    assert result['failed'] == True

# Generated at 2022-06-13 10:56:10.519588
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import tempfile

    fake_task_path = tempfile.mkdtemp()
    sys.modules['ansible.plugins.action.copy'] = __import__('ansible.plugins.action.copy')
    sys.modules['ansible.plugins.action.file'] = __import__('ansible.plugins.action.file')
    sys.modules['ansible.plugins.action.lineinfile'] = __import__('ansible.plugins.action.lineinfile')
    sys.modules['ansible.plugins.action.patch'] = __import__('ansible.plugins.action.patch')
    sys.modules['ansible.plugins.action.script'] = __import__('ansible.plugins.action.script')

# Generated at 2022-06-13 10:56:13.448093
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule('shell')
    result = action.run({'tmp': ''}, {'tasks':[]})
    assert result['failed'] == False

# Generated at 2022-06-13 10:56:23.468451
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a test connection
    # We need to set up a connection to ansible in order to create a task object
    # In the test case, we want to make sure that shell module can be used as a command action
    # We first make sure that ansible.legacy.command has a proper implementation of method run
    # Then we use an ActionModule object (with shell module) to test if the connection is created properly
    from ansible.plugins.loader import action_loader
    command_action = action_loader.get('ansible.legacy.command', None)
    assert command_action.run != None
    assert command_action != None

    # Create a ActionModule object with shell module
    # In order to create an ActionModule object we need to first create a task object
    # We make sure ansible.legacy.build_module is a proper implementation by using it

# Generated at 2022-06-13 10:56:32.610250
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Patch ActionModule._display.warning() so it does not print
    from ansible.plugins.action import ActionModule
    ActionModule._display.warning = lambda *args, **kwargs: None

    task = {'args': {'_uses_shell': True},
            'delegate_to': None,
            'environment': None,
            'register': None,
            'tags': None,
            'run_once': False,
            'name': 'shell module'}
    task_vars = {}
    action_module = ActionModule(task,
                                 connection=None,
                                 play_context=None,
                                 loader=None,
                                 templar=None,
                                 shared_loader_obj=None)

    # Expected: None is returned

# Generated at 2022-06-13 10:56:53.779406
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import unittest
    import tempfile

    def create_fake_ansible_module(result):
        class FakeAnsibleModule(unittest.TestCase):
            def __init__(self, *args, **kwargs):
                self.params = {}
            def fail_json(self, *args, **kwargs):
                raise AssertionError('module failure')
            def exit_json(self, *args, **kwargs):
                if result == 'success':
                    pass
                elif result == 'failure':
                    raise AssertionError('module failure')
        return FakeAnsibleModule()

    def create_fake_loader_obj(result):
        class LoaderModule(unittest.TestCase):
            def get(self, *args, **kwargs):
                self.params = {}

# Generated at 2022-06-13 10:57:02.614115
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(loader=None, task=None, connection=None, play_context=None,
                                 data=None, templar=None, shared_loader_obj=None)

    result = action_module.run()

    assert result['changed'] == False
    assert result['msg'] == "pong"
    assert result['rc'] == 0
    assert result['start'] == '2019-02-13 10:07:41.129397'
    assert result['delta'] == '0:00:00.011514'
    assert result['end'] == '2019-02-13 10:07:41.140911'

# Generated at 2022-06-13 10:57:03.673872
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 0

# Generated at 2022-06-13 10:57:05.688288
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    assert module.run() == True

# Generated at 2022-06-13 10:57:06.451016
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:15.126405
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    print("\n\nTESTING run() for class ActionModule")
    print("\nCreating instance of class ConnectionBase")
    connection_base = ConnectionBase()

    print("\nCreating instance of class ModuleBase")
    module_base = ModuleBase()

    print("\nCreating instance of class Task")
    task = Task()

    print("\nSetting task.args to COMMANDS")
    task.args['COMMANDS'] = "ls"

    print("\nCreating instance of class ActionModule")
    action_module = ActionModule()
    print("\nCalling action_module.run()")
    result = action_module.run(task_vars=None)
    print("\nResult of call to action_module.run(): {}".format(result))
    # print("\nExiting from action_module.run()

# Generated at 2022-06-13 10:57:24.626654
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("testing method run of class ActionModule")

    from collections import namedtuple
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.dataloader import DataLoader

    FakeLoader = namedtuple('FakeLoader', ['action_loader'])
    FakeLoader.action_loader = namedtuple('FakeActionLoader', ['get'])

    module = AnsibleModule('test', '',
                           )
    module.no_log = False
    module.connection = 'test-connection'
    module.params = {'test':'test'}

    loader = DataLoader()
    connection = 'test-connection'
    play_context = 'test-play_context'
    templar = 'test-templar'

    shared_loader_obj = FakeLoader()
    task_vars

# Generated at 2022-06-13 10:57:25.455504
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:57:35.691448
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback import CallbackBase
    from ansible.plugins.action import ActionBase
    from ansible import context
    from io import StringIO
    import yaml


# Generated at 2022-06-13 10:57:36.283244
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:58:12.227215
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.shell as shell

    shell.ActionModule = ActionModule

    action = shell.ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert action.run(
        tmp=None,
        task_vars=None)

# Generated at 2022-06-13 10:58:19.236320
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tester = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )

    tester._task.args = {'_uses_shell': True}
    tester._shared_loader_obj.action_loader.get.return_value.run.return_value = True

    assert tester.run(
        task_vars=dict()
    ) is True

# Generated at 2022-06-13 10:58:33.246129
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import ImmutableDict

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.action import ActionBase
    from ansible.utils.display import Display
    display = Display()
    class FakeModule(object):
        def __init__(self, params):
            self.params = params

        def _debug(self, *args, **kwargs):
            display.vvv(args)

    class FakeTask(object):
        def __init__(self, args):
            self.args = args

        def set_loader(self, loader):
            self._loader = loader


# Generated at 2022-06-13 10:58:35.336060
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actual = ActionModule.run()
    expected = None
    assert actual == expected

# Test of function test_ActionModule_run

# Generated at 2022-06-13 10:58:36.017688
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:58:49.498255
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize ActionModule instance
    action_module = ActionModule(
      None,
      {},
      {},
      'action_module.py',
      {
        'module_args': {},
        '_uses_shell': True,
      },
      None,
      None,
      {},
      '',
      '',
      '',
      None,
      '',
      '',
      '',
      None,
      '',
      '',
      '',
      None,
      '',
      '',
      '',
      None
    )

    # Initialize result
    result = action_module.run(
      tmp=None,
      task_vars={}
    )

    # Assert result and action_module.run returned value type

# Generated at 2022-06-13 10:58:58.131563
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import json
    import unittest
    import unittest.mock as mock
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.legacy import ActionModule

    fake_shell_module = os.path.join(os.path.dirname(__file__), 'fake_shell_module')

    # Create an action module
    action_module = ActionModule(task=None,
                                 connection=None,
                                 play_context=None,
                                 loader=None,
                                 templar=None,
                                 shared_loader_obj=None)

    # Create the command action plugin
    command_action = mock.Mock(spec=ActionBase)

# Generated at 2022-06-13 10:59:00.814907
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    loader, p, templar, shared_loader_obj = get_test_objects() # noqa

# Retrieve objects for testing

# Generated at 2022-06-13 10:59:01.486831
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:59:10.928668
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = 'ansible.legacy.shell'
    args = {'_uses_shell': True}
    mocker = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    task = MagicMock()
    task.immutable = False

    action_module = ActionModule(task=task, connection=connection, play_context=play_context,
                                 loader=loader, templar=templar, shared_loader_obj=shared_loader_obj)
    action_module.run(tmp=None, task_vars=None)
    module_class = mocker.ansible.legacy.command

# Generated at 2022-06-13 11:00:32.514677
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule
    from ansible.errors import AnsibleError
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from aicore.utils.testing.process import AnsibleProcess

    class MockedLoader(object):
        def __init__(self, loader, action_loader):
            self.loader = loader
            self.action_loader = action_loader


# Generated at 2022-06-13 11:00:42.501486
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    req_in = {
        'action': {
            'module_args': {
                '_uses_shell': True,
                '_raw_params': 'some_raw_params',
                'chdir': 'some_chdir',
                'creates': 'some_creates',
                'executable': None,
                'free_form': 'some_free_form',
                'removes': 'some_removes',
                'warn': True,
            },
            'module_name': 'shell',
            'name': 'some_name',
        },
    }

# Generated at 2022-06-13 11:00:43.245744
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:00:51.586744
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Arrange
    task_vars = {'cmd': 'ls -la'}
    tmp = '/tmp'
    loader = None
    play_context = None
    task_ds = {'shell': 'ls -la'}

    # Action base object
    action_base_obj = ActionBase(task=task_ds, connection=None, play_context=play_context, loader=loader, templar=None, shared_loader_obj=None)

    # Action module object
    action_module_obj = ActionModule(task=task_ds, connection=None, play_context=play_context, loader=loader, templar=None, shared_loader_obj=None)

    # patching ActionBase.run

# Generated at 2022-06-13 11:00:58.791576
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import unittest
    from unittest.mock import patch


    from ansible.module_utils.basic import AnsibleModule

    mock_ansible_module = AnsibleModule
    mock_ConnectionBase = unittest.mock.MagicMock()
    mock_TaskVars = unittest.mock.MagicMock()
    mock_task = unittest.mock.MagicMock()


# Generated at 2022-06-13 11:01:02.295174
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ansible.plugins.action.ActionModule(connection=None,
                                          play_context=play_context,
                                          loader=loader,
                                          templar=None,
                                          shared_loader_obj=None)

    pass

# Generated at 2022-06-13 11:01:04.573731
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module.run('tmp', 'task_vars')

# Generated at 2022-06-13 11:01:05.482714
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run(ActionBase, task_vars = None)

# Generated at 2022-06-13 11:01:09.194301
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import types
    import unittest

    import ansible
    import ansible.plugins.action

    class TestActionModule(unittest.TestCase):

        def test_run_default(self):
            pass

    # Run unit test
    unittest.main()

# Generated at 2022-06-13 11:01:20.602939
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = 'shell'
    path = 'test_path'
    args = 'test args'

    def _shared_loader_obj():
        return None

    def _get_action(module, task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
        assert module == 'ansible.legacy.command'
        assert task.args['_uses_shell']
        assert task.args['chdir'] == path
        assert task.args['_raw_params'] == args

        def _run(task_vars):
            return task_vars

        return _run
