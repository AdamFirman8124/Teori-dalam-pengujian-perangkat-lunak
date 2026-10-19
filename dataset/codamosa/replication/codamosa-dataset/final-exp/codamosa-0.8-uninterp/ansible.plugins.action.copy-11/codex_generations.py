

# Generated at 2022-06-13 09:34:53.758549
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.path import mock_unfrackpath_success

    from ansible import context
    from ansible.utils.boolean import boolean
    from ansible.plugins.loader import action_loader

    # Arrange
    action_plugin = action_loader.get('copy', class_only=True)
    task = Task()
    task_result = TaskResult(host=None, task=task)
    play_context = PlayContext()


# Generated at 2022-06-13 09:35:01.479333
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Arguments
    tmp = tempfile.mkdtemp()

    # Return value
    ret = None

    # Returned values
    # module_return = None
    # changed = False
    # module_executed = False
    # result = {}
    # source_files = {}
    # paths = None
    # dest_path = None
    # src = None

    action_copy = ActionModule()
    action_copy.run(tmp)

# Generated at 2022-06-13 09:35:10.910077
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:35:20.632364
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection = MockConnection()
    task = MockTask()
    task.args = dict(
        content=None,
        dest=None,
        src=None,
        force=None,
        backup=None,
        mode=None,
        newline=True,
        validate=None,
        validate_certs=True,
        selevel=None,
        serole=None,
        setype=None,
        seuser=None,
        owner=None,
        group=None,
        remote_src=None,
        local_follow=None,
        follow=None,
        checksum=None,
    )

    action_module = ActionModule(connection, task)
    assert isinstance(action_module._connection, MockConnection)
    assert isinstance(action_module._task, MockTask)
    assert action_

# Generated at 2022-06-13 09:35:25.175871
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.plugins.action.copy import ActionModule
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    import ansible.constants as constants
    import os
    import shutil
    import tempfile
    # import plugins.action.copy

    #@classmethod
    #def run(cls, tmp=None, task_vars=dict()):
    tmp = None
    task_vars = dict()
    # handler for file transfer operations
    #

# Generated at 2022-06-13 09:35:27.193151
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    assert action.run() == 'entering run'


# Generated at 2022-06-13 09:35:31.055568
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    invoke_load_module(ActionModule)
    action = ActionModule(task=dict())
    action._set_connection(Connection(None))

    # currently this method is empty.  Let us know if there is something to test
    assert True

# Generated at 2022-06-13 09:35:34.505449
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task=dict(action=dict(args=dict(src=os.path.abspath(__file__), dest=os.path.abspath(__file__)))))
    module.run()


# Generated at 2022-06-13 09:35:35.428973
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ac = ActionModule()
    ac.run()

# Generated at 2022-06-13 09:35:39.578292
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(dict(a=5, b=10), task_vars=None)
    assert am._task.args.get('a') == 5
    assert am._task.args.get('b') == 10


# Generated at 2022-06-13 09:36:22.018200
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Add your unit test here
    pass


# Generated at 2022-06-13 09:36:22.681584
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass


# Generated at 2022-06-13 09:36:27.269622
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule._HAVE_PUSHY.get() is True
    action_module = ActionModule()
    assert action_module.noop_on_check(True) is True
    assert action_module.noop_on_check(False) is False
    assert callable(action_module.run) is True
    assert_equal(action_module.run.__name__, 'run')


# Generated at 2022-06-13 09:36:34.644840
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # AdhocActionModule was deprecated in Ansible 2.7, so we need a way to
    # construct an instance of ActionModule without a deprecation warning.
    action_module = ActionModule(ActionModule.name,
                                 load_action_plugin(ActionModule.name, action_tempdir),
                                 module_loader=None,
                                 task_loader=None,
                                 connection_loader=None)
    assert action_module

# Generated at 2022-06-13 09:36:43.941443
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # task object to pass to action module
    task = FakeTask()
  
    # host object to pass to action module
    host = FakeHost()

    # connection object to pass to action module
    connection = FakeConnection()

    # We are passing a fake task object to action module
    # The object would be of type ansible.parsing.yaml.objects.Task
    # Contents of task object would be like this
    # module_args={"dest": "/home/my_user/mytestfile", "remote_src": False, "content": "This is a test file", "src": "/home/my_user/test.txt"}

    # We are passing a fake host object to action module
    # The object would be of type ansible.inventory.host.Host
    # Contents of host object would be like this
    # vars={'ans

# Generated at 2022-06-13 09:36:54.529646
# Unit test for constructor of class ActionModule
def test_ActionModule():
    A = ActionModule(task=Task(), connection=None, play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None)
    module_return = dict(failed=False, changed=False)
    final_result = A._execute_module(module_return=module_return, task_vars=dict())
    assert final_result.get('invocation') is not None, 'Invocation was not set in _execute_module'
    assert 'module_stderr' not in final_result, 'module_stderr was set in _execute_module'
    assert 'module_stdout' not in final_result, 'module_stdout was set in _execute_module'


# Generated at 2022-06-13 09:37:06.893274
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    playbook_context = PlayContext()
    inventory = MockInventory()
    connection = MockConnection('/usr/local')
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback='default',
    )
    transfer = ActionModule(
        tqm=tqm,
        connection=connection,
        play_context=playbook_context,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert transfer._connection is connection
    assert transfer._queue_manager is tqm
    assert transfer

# Generated at 2022-06-13 09:37:10.741950
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    module = ActionModule()
    print(module.run())


if __name__ == '__main__':
    # Unit test for method run of class ActionModule
    test_ActionModule_run()

    module = None

# Generated at 2022-06-13 09:37:14.682433
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection = Connection(None)
    task = Task(None)
    # Instantiate class
    am = ActionModule(task, connection, play_context=None, loader=None, templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 09:37:19.143976
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with a control connection
    obj = dummy_type('test_ActionModule_obj')

    obj.args = dict(
        content='abc',
        dest='/path/to/destination',
        state='directory',
    )
    obj.action = 'file'
    obj.task_vars = dict()
    obj.tmpdir = '/tmp'

    obj.backup_dir = '/tmp'
    obj.nocache = False

    obj.connection = dummy_type('test_ActionModule_obj_connection')
    obj.connection.shell = dummy_type('test_ActionModule_obj_shell_paramiko')
    obj.connection.shell.expand_user = lambda x: x
    obj.connection.shell.join_path = lambda x, y: x + '/' + y

# Generated at 2022-06-13 09:38:14.341472
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Task(object):
        def __init__(self, action):
            self.action = action

        def __getattr__(self, name):
            return self.action[name]

    class Play(object):
        def __init__(self, connection, base_vars):
            self.connection = connection
            self.basedir = '/playbook'
            self.basedir_relative = '/playbook'
            self.basedir_has_subdir = False
            self.vars = base_vars

    class Connection(object):
        def __init__(self, tmpdir):
            self.tmpdir = tmpdir


# Generated at 2022-06-13 09:38:19.743693
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = json.dumps({'dest': '/etc/security/limits.conf', 'src': '/etc/security/limits.conf'})

# Generated at 2022-06-13 09:38:24.318706
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    if sys.version_info >= (3, 0):
        from io import StringIO
    else:
        from StringIO import StringIO
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.process.worker import WorkerProcess
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins import module_loader, callback_loader
    from ansible.template import Templar

# Generated at 2022-06-13 09:38:33.907289
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with only required arguments
    action_module = ActionModule('hostname', 'connection')
    assert action_module is not None

    # Test required arguments + optional arguments
    action_module = ActionModule('hostname', 'connection', module_name="test", module_args="test")
    assert action_module is not None

    # Test with all possible arguments
    action_module = ActionModule('hostname', 'connection', module_name="test", module_args="test", task_vars="test",
                                 tmp="test", delegate_to="test", no_log="test", check_mode="test")
    assert action_module is not None


# Generated at 2022-06-13 09:38:40.907564
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # set-up
    from ansible.plugins.action.copy import ActionModule
    from ansible.module_utils.basic import AnsibleModule
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.display import Display
    from ansible.plugins.callback.default import CallbackModule
    from ansible.executor.task_executor import TaskExecutor

# Generated at 2022-06-13 09:38:51.764705
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Maybe we could add some unit tests for this.
    '''
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager

    an_inventory = Inventory(host_list=[])
    an_inventory.add_group('my_group')
    an_inventory.add_host(Host(name='localhost', port=12345))
    a_variable_manager = VariableManager(an_inventory)
    a_variable_manager.set_inventory(an_inventory)



# Generated at 2022-06-13 09:38:55.477314
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Unit test of action module'''
    action_module = ActionModule(
        task=dict(action=dict(module_name='dummy'), args=dict()),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert type(action_module) == ActionModule

# Generated at 2022-06-13 09:39:10.210014
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test constructor of class ActionModule."""

    def test_object_creation(shell):
        task_vars = dict()
        action_module = ActionModule(dict(), dict(), tmp_path='/tmp')
        action_module._execute_module = FakeModuleExecutor(0, dict(), dict(), 'success', False).execute_module
        action_module._remove_tmp_path = lambda x: x

        module_return = action_module.run(task_vars=task_vars)
        assert 'changed' not in module_return

    def test_object_creation_with_deferred_open_shell(shell):
        task_vars = dict(ansible_shell_type='powershell')
        action_module = ActionModule(dict(), dict(), tmp_path='/tmp')
        action_module._execute_module = FakeModule

# Generated at 2022-06-13 09:39:17.993859
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    # Invalid input parameters
    params = { 'dest' : 'destination', 'src' : "source" }
    ansible_module_run_result = {}
    ansible_module_run_result['failed'] = True
    ansible_module_run_result['msg'] = 'src (or content) is required'
    mock_ansible_module_run_result = Mock()
    mock_ansible_module_run_result.configure_mock(**ansible_module_run_result)

    with patch.object(ActionModule, 'run', return_value=mock_ansible_module_run_result):
        result = module._execute_module(module_name='ansible.legacy.copy', module_args=params, task_vars=None)
        assert result['failed']


# Generated at 2022-06-13 09:39:23.411450
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test with invalid transport
    action_module = ActionModule(dict(), dict(), dict(), 'bad', 'ansible_connection')
    assert action_module.transport != 'bad'

    # test with valid transport(s)
    action_module = ActionModule(dict(), dict(), dict(), 'local', 'ansible_connection')
    assert action_module.transport == 'local'
    action_module = ActionModule(dict(), dict(), dict(), 'paramiko', 'ansible_connection')
    assert action_module.transport == 'paramiko'

# Generated at 2022-06-13 09:40:57.365361
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = {}
    connection = {}
    play_context = {}

    at = ActionModule(connection=connection, play_context=play_context, loader=None, templar=None, shared_loader_obj=None)
    assert at._connection == connection
    assert at._play_context == play_context
    assert at._loader is None
    # at.collections is a dummy value for testing.
    assert at.collections == {}
    assert at._templar is None

# Generated at 2022-06-13 09:40:58.180036
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:40:59.255189
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass # TODO: write this test



# Generated at 2022-06-13 09:41:00.861206
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test ActionModule
    assert True

# Generated at 2022-06-13 09:41:14.817108
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    test_ActionModule_run()
    """
    module = Mock()
    connection = Mock()
    display = Mock()
    loader = Mock()

    task = Mock(
        _ds={},
        _legacy_play=True,
        _play_context=None,
        _task_vars={},
        args=dict(
            content=None,
            copy=None,
            dest='foo'
        )
    )

    action = ActionModule(
        task=task,
        connection=connection,
        play_context=Mock(),
        loader=loader,
        templar=Mock(),
        shared_loader_obj=Mock()
    )

    assert action.run() == {'failed': True, 'msg': 'src (or content) is required'}

    task.args.update

# Generated at 2022-06-13 09:41:16.492945
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert (ActionModule(connection=None, play_context=None, loader=None,
                         templar=None, shared_loader_obj=None) is not None)

# Generated at 2022-06-13 09:41:23.591406
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    host_list = [
        'localhost',
    ]

    inventory = InventoryManager(loader=InventoryManager.loader_for('local'))
    inventory.add_host('myhost', 'local://')
    variable_manager = VariableManager(loader=VariableManager.loader_for('yaml'), inventory=inventory)

# Generated at 2022-06-13 09:41:28.726358
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    with patch.object(ActionModule, '_execute_module') as mock_execute_module:
        action_module = ActionModule()
        action_module._task.args = {'src': 'foo', 'dest': 'bar'}
        action_module.run(None, None)
        mock_execute_module.assert_called_with('ansible.legacy.copy', task_vars=None)
    with patch.object(ActionModule, '_execute_module', return_value={'changed': False}):
        action_module = ActionModule()
        action_module._task.args = {'src': 'foo', 'dest': 'bar'}
        action_module.run(None, None)
        assert action_module.run(None, None) == {'changed': False}

# Generated at 2022-06-13 09:41:38.736665
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule.
    """

# Generated at 2022-06-13 09:41:47.069369
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ansible_connection = Mock()
    ansible_connection.transfer_file = MagicMock()
    ansible_connection.change_file_mode = MagicMock()
    ansible_module = ActionModule(ansible_connection)
    ansible_module.runner = Mock()
    ansible_module.runner._connection = ansible_connection
    ansible_module.runner._shell = ansible_connection.shell_class
    ansible_module.runner._shell.join_path = MagicMock(return_value='some_path')
    ansible_module._remote_expand_user = MagicMock(return_value='some_path')
    ansible_module._execute_module = MagicMock()
    ansible_module._remove_tmp_path = MagicMock()

    ansible_module._task = Mock()
    ans