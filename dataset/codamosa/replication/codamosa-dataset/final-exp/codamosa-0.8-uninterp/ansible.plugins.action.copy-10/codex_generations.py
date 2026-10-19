

# Generated at 2022-06-13 09:35:05.824098
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_mock = MagicMock()
    config_mock = MagicMock()
    ansible_connection_mock = MagicMock()
    ansible_connection_mock.get_option.return_value = None
    ansible_connection_mock.close.return_value = None
    ansible_connection_mock.join_path.return_value = "path"
    ansible_connection_mock.remote_expand_user.return_value = "expand user"
    ansible_connection_mock.tmpdir = "tmp"
    ansible_connection_mock.shell.path_has_trailing_slash.return_value = True
    ansible_connection_mock.shell.join_path.return_value = "join path"
    ansible_connection_mock.create_remote_

# Generated at 2022-06-13 09:35:13.474524
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task import Task

    task = Task()
    task_include = TaskInclude()
    task_include.load(dict(tasks='some_list'))
    handler_task_include = HandlerTaskInclude()
    handler_task_include.load(dict(tasks='some_list'))

    action_module = ActionModule()

    # Verify that an error is raised when the task is neither an instance of
    # TaskInclude nor HandlerTaskInclude.
    try:
        action_module._task = task
        action_module.run()
    except AnsibleError:
        pass

# Generated at 2022-06-13 09:35:25.872284
# Unit test for constructor of class ActionModule
def test_ActionModule():

    try:
        # this was originally a dict, but we need to make it a class to set attributes on it
        # and they will then show up in the hash
        class MyTask(object):
            def __init__(self, args):
                self.args = args
        class MyVars(object):
            def get(self, key):
                return None

        my_task = MyTask({'content': 'test file', 'dest': '/tmp/test'})
        my_task.vars = MyVars()

        my_action = ActionModule(my_task, {})
        my_action.generate_checksum = lambda x: '123'
        my_action.transport = 'local'
        my_action.run()
        assert my_action.result['content'] == 'test file'

    finally:
        my

# Generated at 2022-06-13 09:35:35.263620
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup
    module_name         = 'ansible.legacy.copy'
    module_args         = "src=../file_path.txt dest=file_path.txt force=yes"
    module_args         = module_args.split(" ")
    module_args         = [s.split("=") for s in module_args]
    module_args         = dict(module_args)

    task = AnsibleTask(module_name, module_args, None)

    dest = "file_path.txt"
    remote_src = False
    local_follow = True

    # Test
    module_return = ActionModule.run(None, task)

    # Assert
    assert module_return == None

# Generated at 2022-06-13 09:35:45.236091
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection = ConnectionForTest()
    task_vars = dict(inventory_hostname='hostname')
    tmp = '$HOME/ansible/tmp'
    args = dict(
        content='content',
        dest='$HOME/ansible/tmp',
        follow=True,
        mode='777',
        original_basename='test_remote_copy_module.py',
        recurse=True,
        src='$HOME/ansible/tmp',
        validate='skip'
    )
    action_module = ActionModule(connection, task_vars, tmp, args, options=None)

    module_name = 'ansible.legacy.copy'
    module_args = dict()

# Generated at 2022-06-13 09:35:57.361672
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ansible_connection_mock = AnsibleConnectionMock()
    ansible_shell_mock = AnsibleShellMock()
    ansible_shell_mock.get_tmp_path = MagicMock(return_value='/tmp')
    ansible_shell_mock.get_option = MagicMock(return_value='/tmp')
    ansible_shell_mock.join_path = MagicMock(return_value='/tmp/test_tmp')
    ansible_shell_mock.path_has_trailing_slash = MagicMock(return_value=True)
    ansible_connection_mock._shell = ansible_shell_mock
    ansible_task_mock = AnsibleTaskMock()

# Generated at 2022-06-13 09:36:01.878325
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.play_iterator import PlayIterator
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.reserved import HostVars
    from ansible.vars.hostvars import HostVars
    from ansible.plugins.loader import connection_loader
    from ansible.config.manager import ConfigManager
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import module_loader
    from ansible.plugins.callback.default import CallbackModule
   

# Generated at 2022-06-13 09:36:12.340111
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    source = 'source'
    dest = 'dest'
    content = 'content'
    tmp = None
    remote_src = False
    local_follow = True

    with pytest.raises(AnsibleError) as excinfo:
        ActionModule(source, dest, content).run(tmp, task_vars)
    assert 'src (or content) is required' in str(excinfo.value)
    source = 'source'
    dest = None
    content = 'content'
    tmp = None
    remote_src = False
    local_follow = True
    with pytest.raises(AnsibleError) as excinfo:
        ActionModule(source, dest, content).run(tmp, task_vars)
    assert 'dest is required' in str(excinfo.value)


# Generated at 2022-06-13 09:36:13.636790
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True == False


# Generated at 2022-06-13 09:36:21.226597
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("testing ActionModule.run")

    src = "test/test_data/test-src-dir"
    dest = "test/test_data/test-dest-dir"

    # Create a module that we can use to test using...
    module = ActionModule()

    # Create some test args that we can pass to the module...
    module_args = dict(src=src, dest=dest)

    # Create a task to store in the module...
    task = Task()
    task.args = module_args

    # Store the task in the module...
    module._task = task

    # Create a connection to use in the module...
    connection = Connection("test-connection")

    # Store the connection in the module...
    module._connection = connection

    # Create a loader to use in the module...
    loader = DataLoader()

   

# Generated at 2022-06-13 09:37:14.975130
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' action_plugin/test_action_plugin_copy.py:test_ActionModule() '''

    from ansible.plugins.action.copy import ActionModule
    from ansible.parsing.dataloader import DataLoader

    module_loader = DataLoader()
    ansible_vars = {}

    task_t = dict()
    task_t['args'] = dict()

    # Test 1
    # Instantiate object and test module parameters

    # Test 1.1
    # Test constructor with valid module parameters
    actionModule = ActionModule(task_t, ansible_vars, module_loader)

    keys = actionModule.module_args.keys()
    assert 'content' in keys
    assert 'dest' in keys
    assert 'follow' in keys
    assert 'local_follow' in keys

# Generated at 2022-06-13 09:37:19.416369
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task as Task
    from ansible.playbook.play import Play as Play
    from ansible.playbook.play_context import PlayContext as PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager as TaskQueueManager
    from ansible.inventory.manager import InventoryManager as InventoryManager
    from ansible.vars.manager import VariableManager as VariableManager
    from ansible.parsing.dataloader import DataLoader as DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor as PlaybookExecutor
    from ansible.cli import CLI as CLI
    from ansible.utils.vars import combine_vars as combine_vars
    from ansible.plugins.strategy import StrategyBase as StrategyBase

# Generated at 2022-06-13 09:37:25.112553
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = AnsibleModule(
        argument_spec = dict(
            src = dict(required=True, type='str'),
            dest = dict(required=True, type='str'),
        ),
        supports_check_mode=True
    )
    task_vars = dict()
    am = ActionModule(module, 'files', None, None)
    result = am.run(tmp=None, task_vars=task_vars)
    print(result)


# Generated at 2022-06-13 09:37:31.030750
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_class = ActionModule('Action_copy', {})
    action_class.copy_info = dict()

    action_class.copy_info['remote_src'] = True
    assert action_class._get_copy_info()
    action_class.copy_info['no_checksum'] = True
    assert action_class._get_copy_info()
    action_class.copy_info['checksum'] = True
    assert action_class._get_copy_info()
    action_class.copy_info['no_follow'] = True
    assert action_class._get_copy_info()
    assert action_class._get_copy_info()

    action_class.copy_info['remote_src'] = True
    action_class.copy_info['no_checksum'] = True
    assert action_class._get_copy_

# Generated at 2022-06-13 09:37:33.190388
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:37:43.577896
# Unit test for constructor of class ActionModule
def test_ActionModule():
    hostname = 'hostname'
    runner_queue = 1
    connection = 'connection'
    task_uuid = 'task_uuid'
    task = 'task'
    task_vars = dict()
    loader = 'loader'
    templar = 'templar'
    shared_loader_obj = 'shared_loader_obj'

    action_module = ActionModule(hostname, runner_queue, connection, task_uuid, task, task_vars, loader, templar, shared_loader_obj)

    assert action_module._hostname == hostname
    assert action_module._runner_queue == runner_queue
    assert action_module._connection == connection
    assert action_module._task_uuid == task_uuid
    assert action_module._task == task
    assert action_module._task_vars

# Generated at 2022-06-13 09:37:50.251398
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # AnsibleFileVars
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    tmp = 'tmp'
    task_vars = None
    result = action_module.run(tmp, task_vars)
    assert result == None


# Generated at 2022-06-13 09:38:04.312350
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:38:14.239560
# Unit test for constructor of class ActionModule
def test_ActionModule():
    set_module_args(dict(
        source='/home/vagrant/file.txt',
        content=None,
        dest='/home/vagrant/file1.txt',
        remote_src=False,
        local_follow=False,
        state='file',
        force=True,
        follow=False
    ))

# Generated at 2022-06-13 09:38:19.617025
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Use nosetests to execute this testcase.
    """

    # The Module Type
    task_module = 'ansible.legacy.copy'

    # The Playbook
    playbook = Playbook()

    # The Data source
    task_source = "tests/unit/modules/data/source_tree.yml"
    source_data = Playbook.load_data_from_file(task_source)

    # The Task
    tasks = source_data[0].get('tasks')

    # The testcase to be tested
    testing_task = tasks[0]

    # Construct a ActionModule
    action_module = ActionModule(playbook, task_module, testing_task)

    # Create a tempdir
    tempdir = tempfile.mkdtemp()

# Generated at 2022-06-13 09:39:56.985365
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockModule:
        def __init__(self):
            self.params = {}

    class MockTask:
        def __init__(self):
            self.args = {}

    # prep
    mock_module = MockModule()
    mock_task = MockTask()
    mock_task.args = {'src': 'fake_src', 'dest': 'fake_dest', 'remote_src': True}
    mock_task_vars = {'fake_task_vars': 'fake_task_vars'}

    # test
    action_module = ActionModule(mock_module, mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 09:40:06.577663
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    tmp = tempfile.mkdtemp(dir=C.DEFAULT_LOCAL_TMP, prefix="ansible_file_")
    module.params = dict(
        src='/usr/bin/python',
        dest='%s/test_ActionModule' % tmp
    )

    copy = Connection({
        'basedir': tmp
    })
    module_context = make_context(copy, module)
    file_conn = ActionModule(module_context)

    assert isinstance(file_conn, ActionModule)
    shutil.rmtree(tmp)

# Generated at 2022-06-13 09:40:16.183697
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import RoleInclude
    from ansible.executor.task_result import TaskResult
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from collections import namedtuple

    module_args = {'content': None, 'src': 'src_value', 'dest':'dest_value', 'remote_src': False, 'local_follow': True}
    task_vars = dict()
    loader = DataLoader()
    task = Task()
    task._role = RoleInclude()
   

# Generated at 2022-06-13 09:40:17.592542
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule(None, None, None)
    result = actionModule.run()
    assert(result == None)

# Generated at 2022-06-13 09:40:26.371610
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:40:34.110099
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = {}
    connection = Connection(module_name='file', module_args='', task_uuid='0', become_method='sudo', become_user='root', become_password='foobar', become_exe='sudo')
    task = Task(task_vars, connection)
    action_module = ActionModule(task, connection, None)
    assert action_module._task == task
    assert action_module._connection == connection

# Generated at 2022-06-13 09:40:43.666383
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mytask = _create_task('test_task')
    myplay = _create_play(mytask)
    myplaycontext = _create_play_context(myplay)
    myconnection = Connection(myplaycontext)

    # test connection object
    assert myconnection.localhost
    assert myconnection.transport == 'local'
    assert myconnection.connected
    assert myconnection._shell.getcwd() is None
    _assert_mod_args_equal(myconnection, dict(path=None))
    _assert_mod_args_equal(myconnection, dict(path='/'))
    _assert_mod_args_equal(myconnection, dict(path='/tmp/'))
    _assert_mod_args_equal(myconnection, dict(path='/tmp'))

# Generated at 2022-06-13 09:40:57.433083
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Unit test for constructor of class ActionModule '''
    # Set a temporary connection.
    connection = Mock()
    connection.run = lambda *args, **kwargs: dict(rc=0, stdout='', stderr='')
    connection.put_file = lambda *args, **kwargs: None
    connection.run_command = lambda *args, **kwargs: dict(rc=0, stdout='', stderr='')

    # Construct the object.
    module = ActionModule(connection=connection, task=dict(action=dict()),
                          loader=dict(), play_context=dict(), shared_loader_obj=None)

    # Validate object attributes.
    assert module._connection == connection
    assert module._loader.__class__.__name__ == 'DataLoader'

# Generated at 2022-06-13 09:40:59.812019
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        import __main__ as main
    except ImportError:
        main = {}

    mock_loader = DictDataLoader({})
    mock_connection = Connection(mock_loader=mock_loader)
    mock_task = Task()
    assert isinstance(ActionModule(mock_task, mock_connection, main), ActionModule)

# Generated at 2022-06-13 09:41:01.186847
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule('mock', {})