

# Generated at 2022-06-13 10:16:18.147022
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.modules.system import ping
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_context import PlayContext
    from ansible.vars.hostvars import HostVars
    from collections import namedtuple
    from ansible import constants as C
    import os

    # Create temporary directories
    pickle_dir = os.path.join(C.DEFAULT_LOCAL_TMP, 'cbedb9db943c8bcbfbcef7b60d3ba3a7')
    module_dir = os.path.join

# Generated at 2022-06-13 10:16:24.630292
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # get an instance of the base class
    action_base = ActionBase()
    # create an instance of the ActionModule class using constructor of base class 
    action_module = ActionModule(task=action_base._task, connection=action_base._connection, play_context=action_base._play_context, loader=action_base._loader, templar=action_base._templar, shared_loader_obj=action_base._shared_loader_obj)
    # test the constructor 
    assert action_module != None

# Generated at 2022-06-13 10:16:35.141599
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create a fake task to pass on
    task = dict()
    task["action"] = dict()
    task["async_val"] = 0
    task["wrap_async"] = 0
    task["connection"] = dict()
    task["connection"]["has_native_async"] = 0

    # instantiate the class
    am = ActionModule(task=task)

    # create a fake connection

    class fakeConnection(object):
        def __init__(self):
            self.has_native_async = 0

    cnxn = fakeConnection()

    # create a temp directory that can be used
    import tempfile

    # TEMPFILE_DIR is set by the manage.py test command

# Generated at 2022-06-13 10:16:35.912794
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:16:49.588780
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test ActionModule constructor
    '''
    #
    # Tests of ActionModule.__init__()
    #

    # Invalid action definition
    def test_invalid_action_definition():
        '''
        Test constructor failure on invalid action definition
        '''
        import ansible.playbook
        task = ansible.playbook.task.Task()
        # invalid action
        action = 'invalid'
        task.action = action

# Generated at 2022-06-13 10:16:50.648419
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False



# Generated at 2022-06-13 10:16:52.489884
# Unit test for constructor of class ActionModule
def test_ActionModule():
    instance = ActionModule()
    assert (isinstance(instance, ActionModule))

# Generated at 2022-06-13 10:16:53.107219
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:16:55.441062
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create a ActionModule instance
    action_module_class = ActionModule()

    # Test the constructor of ActionModule
    assert action_module_class

# Generated at 2022-06-13 10:17:05.051405
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext

    role = Role()
    block = Block.load(dict(
        tasks=[dict(action="setup", debugmsg="test")],
        handlers=[],
        rescue=[],
        always=[]
    ), role=role)
    task = Task()
    task._role = role
    task._block = block
    play_context = PlayContext()
    task.set_loader(None)

    am = ActionModule(task, play_context, '/test/test')
    assert am._task == task
    assert am._loader == None
    assert am._templar == None

# Generated at 2022-06-13 10:17:17.070149
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # set up
    args = {'chdir': '/path/to/cwd', '_uses_shell': True, '_raw_params': 'ls', '_tmp_path': '/private/tmp/ansible_OZ6bEQ/command'}
    module_name = 'command'
    class_name = 'ActionModule'
    task_name = 'command'
    task_vars = {'ansible_check_mode': False, 'ansible_version': {'full': '2.4.2.0', 'major': 2, 'minor': 4, 'revision': 2, 'string': '2.4.2.0'}, 'ansible_diff': False}
    tmp = '/private/tmp'
    wrap_async = False

# Generated at 2022-06-13 10:17:18.141279
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = ActionModule()
    assert isinstance(result, ActionModule)


# Generated at 2022-06-13 10:17:18.790126
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:17:20.727924
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    a = ActionModule()
    assert a is not None

# Generated at 2022-06-13 10:17:30.474908
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Connection
    from ansible.plugins.connection.local import Connection
    from ansible.inventory.host import Host

    # Task
    from ansible.playbook.task import Task

    # ActionModule
    from ansible.plugins.action.ec2_remote_facts import ActionModule

    # playbook
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext

    # Mock modules
    module_loader = None
    def get_loader():
        return module_loader
    def set_loader(loader):
        global module_loader
        module_loader = loader
    from ansible.utils.module_docs import get_docstring


# Generated at 2022-06-13 10:17:40.158205
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for run method of class ActionModule
    """
    import ansible.plugins
    import ansible.plugins.action
    import ansible.utils.vars

    reload(ansible.plugins.action)
    reload(ansible.plugins)
    reload(ansible.utils.vars)

    class MockTask:
        """
        Mock class for task
        """
        pass

    class MockConnection:
        """
        Mock class for connection
        """
        pass

    class MockShell:
        """
        Mock class for shell
        """
        pass

    class MockAnsibleHost:
        """
        Mock class for AnsibleHost
        """
        pass

    class MockAnsibleModule:
        """
        Mock class for AnsibleModule
        """
        def __init__(self):
            pass



# Generated at 2022-06-13 10:17:54.296784
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import os
    import tempfile
    import json

    tmp_dir = tempfile.mkdtemp()
    print(tmp_dir)


# Generated at 2022-06-13 10:17:59.373281
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.normal

    obj = ansible.plugins.action.normal.ActionModule.ActionModule(
            {'args': dict(foo='bar')},
            '',
            '',
            {})
    assert obj.run(task_vars={'foo': 'notbar'}) == {'foo': 'notbar'}, 'ActionModule.run() Failed'

# Generated at 2022-06-13 10:18:03.130381
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    ActionModule(task, connection, play_context, new_stdin, loader, templar, shared_loader_obj)
    """
    pass


# Generated at 2022-06-13 10:18:16.036635
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    This is a unit test for the constructor of the class ActionModule.
    It will verify if the object was correctly instantiated and also that the super class constructor was called.
    """
    # Make sure that the constructor of the class ActionBase was called
    mocker.patch("ansible.plugins.action.ActionBase.__init__")
    a = ActionModule("connection", "inject", "tmp", "task_vars")
    assert ActionBase.__init__.called
    # Make sure that the object was correctly instantiated
    assert a._connection == "connection"
    assert a._task_executor == "inject"
    assert a._loader == "inject"
    assert a._shared_loader_obj == "inject"
    assert a._task == "task_vars"

# Generated at 2022-06-13 10:18:25.183437
# Unit test for constructor of class ActionModule
def test_ActionModule():
    args = {'foo':'bar'}
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None

# Generated at 2022-06-13 10:18:28.781040
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, PlayContext=None, loader=None, templar=None, shared_loader_obj=None)
    assert am is not None

# Generated at 2022-06-13 10:18:40.990764
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # A test case for creating an instance of the class ActionModule
    # and passing the test method 'run' of class ActionModule
    # in order to check its response

    # create an instance of the class ActionModule
    action = ActionModule()

    # creating fake object for passing to the method run of class ActionModule
    class fakeObj:
        def __init__(self, async_val):
            self.async_val = async_val
            self.action = 'setup'

    # creating fake object for passing to the method run of class ActionModule
    class fakeObj_1:
        def __init__(self):
            self.has_native_async = True

    # creating fake object for passing to the method run of class ActionModule
    class fakeObj_2:
        def __init__(self, tmpdir):
            self.tmpdir

# Generated at 2022-06-13 10:18:50.416082
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # If a module is specified, we execute that module and return
    # it's result. If module_name is missing and we have a local
    # action, we execute that local action instead.
    # When we have neither a module nor a local action to execute,
    # we return an error.
    module_name = 'shell'
    local_action = 'shell'
    to_remove_path = '/usr/tmp'
    task_vars = {'local_action': local_action}
    tmp = None
    task = ActionModule(tmp, task_vars)
    result = task.run(tmp, task_vars)
    assert result.get('skipped')

# Generated at 2022-06-13 10:18:57.729778
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor using default argument values
    ActionModule()

    # Constructor using named argument values
    ActionModule(task=None)
    ActionModule(connection=None)
    ActionModule(play_context=None)
    ActionModule(loader=None)
    ActionModule(shared_loader_obj=None)
    ActionModule(variable_manager=None)

    # Constructor using positional argument values
    ActionModule(None, None, None, None, None, None)

# Generated at 2022-06-13 10:18:58.876435
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('changed: True')

# Generated at 2022-06-13 10:19:02.512057
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Modules should skip if there is no module_args
    # Setup
    module_args = dict()
    task_vars = dict()

    # Test
    assert ActionModule.run(module_args,task_vars) == dict()

# Generated at 2022-06-13 10:19:03.358606
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run')

# Generated at 2022-06-13 10:19:11.968593
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    import copy
    from ansible.plugins.action import ActionBase
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.vars import merge_hash
    from ansible.utils.vars import combine_vars
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.block import Block

# Generated at 2022-06-13 10:19:14.833266
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule('test_playbook_path','test_play','test_task','test_basedir','test_loader','test_templar','test_shared_loader_obj','test_connection','test_ansible_module')

    assert actionmodule is not None

# Generated at 2022-06-13 10:19:27.262071
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:19:34.562781
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.utils.vars import load_extra_vars, load_options_vars, load_command_vars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host

# Generated at 2022-06-13 10:19:36.174541
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("constructor of class ActionModule")
    t = ActionModule()
    assert type(t) == ActionModule

# Generated at 2022-06-13 10:19:36.879898
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None)

# Generated at 2022-06-13 10:19:41.047215
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("This is a constructor test: \n")
    _task = None
    _connection = None
    _play_context = None
    _loader = None
    _templar = None
    _shared_loader_obj = None
    test_actionModule = ActionModule(_task, _connection, _play_context, _loader, _templar, _shared_loader_obj)
    assert test_actionModule

# Generated at 2022-06-13 10:19:42.833495
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am.ACTION_VERSION == "2.0"
    assert am.SHORT_DESCRIPTION == "runs a module without argument tweaking"
    assert am.LONG_DESCRIPTION == "runs a module without argument tweaking"

# Generated at 2022-06-13 10:19:44.550326
# Unit test for constructor of class ActionModule
def test_ActionModule():
  am = ActionModule()
  assert isinstance(am, ActionBase)

# Generated at 2022-06-13 10:19:45.112545
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:19:48.437388
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up a test object
    a = ActionModule(None, None)
    # Test run method
    res = a.run()
    assertTrue(isinstance(res, dict))

# Generated at 2022-06-13 10:19:50.874684
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # module = ActionModule({'foo': 'bar'})
    # assert module.res == {'foo': 'bar'}
    raise NotImplementedError

# Generated at 2022-06-13 10:20:22.947360
# Unit test for constructor of class ActionModule
def test_ActionModule():
    config = {
        'no_log': False
    }

    # Instantiate _ActionBase
    module_args = {
        'name': None,
        'free_form': None
    }

    action_base = ActionBase(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Instantiate ActionModule
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert action_module != None
    assert action_base != None

# Generated at 2022-06-13 10:20:30.969670
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Unit test for the action plugin
    ActionModule = make_action_plugin()
    connection = ConnectionMock()
    module = 'command'
    args = {'_ansible_poll_interval': 10, '_ansible_other_argument': 'blah'}
    task = TaskMock(action=module, module_args=args, async_val=False)
    result = connection._shell.run_command(task.module_args['_ansible_shell_executable'], args)
    task.async_val = False
    assert result == {'rc': 0, 'stderr': '', 'stdout': 'FUBAR'}

# Generated at 2022-06-13 10:20:33.507197
# Unit test for constructor of class ActionModule
def test_ActionModule():
    aModule = ActionModule()
    assert(aModule is not None)
    assert type(aModule) is ActionModule


# Generated at 2022-06-13 10:20:37.946325
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Initialise an action module.
    action_module = ActionModule(connection=None,
                                 task_queue_manager=None,
                                 loader=None,
                                 templar=None,
                                 shared_loader_obj=None)
    # Execute the run function.
    action_module.run(task_vars=None)

# Generated at 2022-06-13 10:20:39.135235
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO
    raise NotImplementedError()


# Generated at 2022-06-13 10:20:46.047079
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create mock injection
    mock_inject = dict(
        connection=dict(
            _shell=dict(tmpdir=None, _has_native_async=False)),
        task=dict(
            async_val=False,
            action='setup'))

    # create object that will be mocked
    connector = ActionModule()

    # mock object and return appropriate dicts for testing
    connector._remove_tmp_path = lambda x: x
    connector._execute_module = lambda x, wrap_async: dict(
        invocation=dict(
            module_name='setup',
            module_args='{}'),
        module_name="setup",
        module_args="{}",
        _ansible_verbose_override=True,
        _ansible_no_log=False)

    # create mocked task_vars


# Generated at 2022-06-13 10:20:46.622656
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:20:56.986741
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    ActionBase._configure_module = lambda x,y: True # skip setup of module

    action = ActionModule.load({})
    action._task._role = None
    action._task.action = 'copy'
    action._task.args = {}
    action._task.async_val=0
    action._task.notify=""
    action._task.environment=""
    action._task._role_name=""
    action._task._role_path=""
    action._task.loop=""
    action._task.when=""
    action._task.until=""
    action._task.retries=""
    action._task.register=""
    action._task.tags=""
    action._task.until=""
    action._task.run_once=False
    action._task.delegate_to=""

# Generated at 2022-06-13 10:21:09.281310
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.normal import ActionModule
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C
    import json
    from mock import MagicMock
    from io import StringIO
    import os

    # Set configuration defaults
    C.HOST_KEY_CHECKING = False
    C.DEFAULT_HOST_LIST = '/etc/ansible/hosts'

    # Ansible Inventory

# Generated at 2022-06-13 10:21:12.282967
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    task_vars = dict()
    tmp = dict()
    result = dict()
    action_module.run(tmp, task_vars)

# Generated at 2022-06-13 10:22:20.858004
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # modules() method of task is called
    # it returns a list of all the modules
    # here 2 modules are returned ['setup']
    mock_task = MagicMock()
    mock_task.action = 'setup'
    mock_task.action_loader = Mock()
    mock_task.tags = []
    type(mock_task.action_loader)._modules = PropertyMock(return_value={'setup': 'setup'})

    # connection is created
    mock_connection = Mock()

    # _task and _connection is set for ActionModule
    action_module = ActionModule(mock_task, mock_connection, 'setup', None, None)

    assert action_module._task == mock_task
    assert action_module._connection == mock_connection

# Generated at 2022-06-13 10:22:23.366097
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    # TODO: Add more testing here.
    assert module.SUPPORTED_FILTER_PLUGINS is not None
    assert module.SUPPORTED_FILTER_PLUGINS is not None



# Generated at 2022-06-13 10:22:26.324930
# Unit test for constructor of class ActionModule
def test_ActionModule():
    t1 = ActionModule()
    assert t1._supports_async == True
    assert t1._supports_check_mode == True

# Generated at 2022-06-13 10:22:32.002282
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:22:33.129429
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    assert True

# Generated at 2022-06-13 10:22:33.912848
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 10:22:35.406536
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # No constructor parameters to test
    actionmodule = ActionModule()
    assert isinstance(actionmodule, ActionModule)

# Generated at 2022-06-13 10:22:36.795480
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test ActionModule run method with a connection object
    return None

# Generated at 2022-06-13 10:22:38.671160
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:22:48.581063
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule._append_tags = lambda x, y: None
    ActionModule._log = lambda self, x, result: None
    ActionModule._low_level_execute_command = lambda x, y, z: {}
    ActionModule._execute_module = lambda x, y, z: {}
    ActionModule._remove_tmp_path = lambda x, y: None
    task_vars = {}
    module_return = {'status': 0, 'msg': 'ok'}
    module_executed = {'status': 0, 'msg': 'ok', 'invocation': {}}
    action_module = ActionModule(task=None, connection=None, play_context=None)
    assert action_module.run(task_vars=task_vars) == module_executed

# Generated at 2022-06-13 10:25:08.357264
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(
        ansible_connection = 'local',
        ansible_python_interpreter = '/usr/bin/python'
    )
    tmp = '/tmp'
    mock_task = dict(
        async_val = None,
        action = 'setup',
        module_name = 'setup',
        register = 'setup_result',
        _ansible_verbose_always = True,
        #nofilter = True,
    )
    mock_loader = None
    mock_templar = None
    mock_shared_loader_obj = None
    connection = None
    am = ActionModule(mock_task, connection, tmp, mock_loader, mock_templar, mock_shared_loader_obj)
    result = am.run(tmp, task_vars)

# Generated at 2022-06-13 10:25:14.981165
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.action_plugins import ActionModule as action_module
    assert type(action_module) is type, "ActionModule type is not type"
    assert action_module.__bases__ is (object,)
    assert getattr(action_module, "run" ) is not None, "ActionModule has no 'run' method"
    assert type(action_module.run) is instancemethod, "ActionModule's run method is not type instancemethod"

# Generated at 2022-06-13 10:25:17.022395
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None)
    assert am._supports_check_mode == True
    assert am._supports_async == True
    assert am._connection is None
    assert am._task is None

# Generated at 2022-06-13 10:25:26.632472
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import traceback
    test_dir = os.path.dirname(os.path.realpath(__file__))
    ansible_src_dir = os.path.dirname(os.path.dirname(os.path.dirname(test_dir)))
    test_module_location = os.path.join(ansible_src_dir, 'lib', 'ansible', 'modules')
    if test_module_location not in sys.path:
        sys.path.append(test_module_location)
    import test_module

    module = ActionModule(task=dict(action=dict(module='test_module')))
    module._shared_loader_obj = None
    module._task = module.task
    module._connection = None
    module._shell = None


# Generated at 2022-06-13 10:25:27.693306
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    action.__class__.__name__ == 'ActionModule'

# Generated at 2022-06-13 10:25:36.967317
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' unit test for construction of class ActionModule
    '''
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    inventory = InventoryManager(loader, [Host(name='ansible')])
    variable_manager = VariableManager(loader, inventory)

# Generated at 2022-06-13 10:25:37.612480
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:25:39.738994
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(connection=object, task=object)
    assert action_module._execute_module(object, object, wrap_async=object) == {}

# Generated at 2022-06-13 10:25:40.644886
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise Exception("No test_ActionModule_run is implemented")

# Generated at 2022-06-13 10:25:50.532221
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.vars.unsafe_proxy import wrap_var
    
    am = ActionModule()
    am._remove_tmp_path = lambda x: True

    # test result.get('skipped') == False
    result = TaskResult(host=wrap_var('localhost'), task=wrap_var('ping'), return_data=wrap_var({'rc': 0, 'stderr': '', 'changed': True, 'stdout': 'pong', 'stdout_lines': ['pong'], 'warnings': ['Consider using the ping module instead']}))

    am._execute_module = lambda x, wrap_async=False: wrap_var({'msg': 'fake'})

    # add _ansible_verbose_override to make sure we don't break this feature